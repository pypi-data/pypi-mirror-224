import binascii
import enum
import queue
import re
import typing

import serial.threaded


class Rf95Exception(Exception):
    """The exception to be thrown for rf95modem logic errors."""

    pass


class Rf95TransmitLengthException(Exception):
    """An rf95modem exception for mismatching lengths."""

    def __init__(self, sent_len, exp_len):
        super(Exception, self).__init__(
            f"Sent only {sent_len} bytes instead of {exp_len} bytes"
        )
        self.sent_len = sent_len
        self.exp_len = exp_len


class ModemMode(enum.Enum):
    """Selection of rf95modem modes of operation."""

    MEDIUM_RANGE = 0
    """MediumRange is the default mode for medium range. Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on."""

    FAST_SHORT_RANGE = 1
    """FastShortRange is a fast and short range mode. Bw = 500 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on."""

    SLOW_LONG_RANGE = 2
    """SlowLongRange is a slow and long range mode. Bw = 31.25 kHz, Cr = 4/8, Sf = 512chips/symbol, CRC on."""

    SLOW_LONG_RANGE2 = 3
    """SlowLongRange2 is another slow and long range mode. Bw = 125 kHz, Cr = 4/8, Sf = 4096chips/symbol, CRC on."""

    SLOW_LONG_RANGE3 = 4
    """SlowLongRange3 is another slow and long range mode. Bw = 125 kHz, Cr = 4/5, Sf = 2048chips/sym, CRC on."""


class RxMessage(typing.NamedTuple):
    """Received message from the rf95modem."""

    payload: bytes
    """Binary payload as received on the air."""

    rssi: int
    """RSSI, received signal strength indicator"""

    snr: int
    """SNR, signal-to-noise ratio"""

    @classmethod
    def from_modem_line(cls, line):
        """Instantiate a new RxMessage based on an rf95modem line.

        Parameters
        ----------
        line: An +RX line received from the rf95modem.

        See Also
        --------
        rf95modem.reader.Rf95Reader
        """
        match = re.match(r"^\+RX \d+,([0-9A-Fa-f]+),([-0-9]+),([-0-9]+)$", line)
        if match is None:
            raise Rf95Exception(f"Line {line} does not match RX regex")
        return cls(bytes.fromhex(match[1]), int(match[2]), int(match[3]))


class Rf95Reader(serial.threaded.LineReader):
    """Serial reader to interact with the rf95modem.

    Incoming messages can be processed by a handler function (RxMessage -> ())
    by appending the handler to the class' rx_handlers field.

    Technically this class borrows lots of its logic from the LineReader.

    Examples
    --------
    >>> ser = serial.serial_for_url('/dev/ttyUSB0', baudrate=115200, timeout=1)
    >>> with serial.threaded.ReaderThread(ser, rf95modem.Rf95Reader) as rf95:
    >>>     rf95.rx_handlers.append(lambda rx: print(rx)) # print to stdout
    >>>     rf95.mode(rf95modem.ModemMode.FAST_SHORT_RANGE)
    >>>     rf95.frequency(868.23)
    >>>     rf95.transmit(b"hello world")
    """

    TERMINATOR = b"\n"

    SERIAL_TIMEOUT_SEC = 3

    def __init__(self):
        """Instantiate a new Rf95Reader.

        However, such a class should be instantiated by serial.threaded.ReaderThread.
        Do not use this constructor directly!
        """
        super(Rf95Reader, self).__init__()
        self.rx_handlers = []
        self._msg_queue = queue.Queue()

    def handle_line(self, line):
        """Works on read lines; inherited by serial.threaded.LineReader.

        Do not use this method directly!
        """
        if line.startswith("+RX "):
            rx = RxMessage.from_modem_line(line)
            for rx_handler in self.rx_handlers:
                rx_handler(rx)
        else:
            self._msg_queue.put(line)

    def _at_cmd(self, cmd, stop_fn):
        """Internal method to execute commands and parse their feedback.

        Parameters
        ----------
        cmd : `str`
            AT command to be sent to the rf95modem.
        stop_fn : `str` -> `bool`
            Function, str -> bool, to say when stop reading feedback lines.

        Returns
        -------
        _at_cmd : `list` [`str`]
            List of returned lines until stop_fn became True.
        """
        self.write_line(cmd)

        lines = []
        while True:
            try:
                line = self._msg_queue.get(timeout=self.SERIAL_TIMEOUT_SEC)
                lines.append(line)

                if stop_fn(line):
                    break
            except queue.Empty:
                raise Rf95Exception(f"Feedback for rf95modem command {cmd} timed out")

        return lines

    def transmit(self, payload):
        """Transmits the given payload over the LoRa PHY.

        Parameters
        ----------
        payload : `bytes`
            Payload as bytes.

        Raises
        ------
        Rf95Exception
            Raised if sending fails or internal errors.
        Rf95TransmitLengthException
            Raised if the length of sent data does not equals the given data's length.
            If this happens, manual fragmentation might become necessary.
        """
        cmd = "AT+TX=" + binascii.hexlify(payload).decode("utf-8")
        resp = self._at_cmd(cmd, lambda _: True)

        match = re.match(r"^\+SENT (\d+) bytes\.$", resp[0])
        if match is None:
            raise Rf95Exception(f"Line {line} does not match +SENT regex")

        sent_len, exp_len = int(match[1]), len(payload)
        if sent_len != exp_len:
            raise Rf95TransmitLengthException(sent_len, exp_len)

    def mode(self, mode):
        """Set the rf95modem's mode.

        Parameters
        ----------
        mode : `rf95modem.reader.ModemMode`
            The mode to be used as a kind of the ModemMode.

        Raises
        ------
        Rf95Exception
            Raised on internal errors.
        """
        cmd = f"AT+MODE={mode.value}"
        resp = self._at_cmd(cmd, lambda _: True)

        if resp[0] != "+OK":
            raise Rf95Exception(f"Mode {mode} failed: {resp[0]}")

    def frequency(self, freq):
        """Set the rf95modem's frequency.

        Parameters
        ----------
        freq : `float`
            The frequency as a floating point number.

        Raises
        ------
        Rf95Exception
            Raised on internal errors.
        """
        cmd = f"AT+FREQ={freq:.2f}"
        resp = self._at_cmd(cmd, lambda _: True)

        match = re.match(r"^\+FREQ: (\d+\.\d+)$", resp[0])
        if match is None:
            raise Rf95Exception(f"Frequency change to {freq} failed: {resp[0]}")

        if abs(float(match[1]) - freq) > 0.01:
            raise Rf95Exception(f"Frequency changed to {match[0]} instead of {freq}")

    def fetch_status(self):
        """Fetch the rf95modem's status.

        Returns
        -------
        fetch_status : `dict` [`str`, `str`]
            Dictionary mapping all fetched values from key to value.
        """
        cmd = "AT+INFO"
        resp = self._at_cmd(cmd, lambda l: l.startswith("+OK"))

        return {
            kv[0]: kv[1].strip()
            for kv in (line.split(":") for line in resp)
            if len(kv) == 2 and kv[0] != "+STATUS"
        }
