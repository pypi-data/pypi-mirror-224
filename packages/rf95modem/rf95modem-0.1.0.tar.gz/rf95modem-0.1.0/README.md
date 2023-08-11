# rf95modem-py

Python library to send and receive data over LoRa PHY via a serial connection to a [rf95modem].

This library was tested against the rf95modem commit [`8f163aa`][rf95modem-commit], slightly after version 0.7.3.


## Library

The primary focus of this library is to send and receive data via LoRa's physical layer, LoRa PHY, with the help of a [rf95modem].

Therefore the `rf95modem.reader.Rf95Reader.` allows direct interaction with a connected rf95modem, including configuration changes, sending, and receiving raw LoRa PHY messages.
This `Rf95Reader` extends `serial.threaded.LineReader` from [pySerial][pyserial].

The following short code example demonstrates how to use this library.

```python
import serial
import serial.threaded
import sys
import time

import rf95modem


if __name__ == '__main__':
    ser = serial.serial_for_url('/dev/ttyUSB1', baudrate=115200, timeout=1)
    with serial.threaded.ReaderThread(ser, rf95modem.Rf95Reader) as rf95:
        rf95.rx_handlers.append(lambda rx: print(rx))

        rf95.mode(rf95modem.ModemMode.FAST_SHORT_RANGE)
        rf95.frequency(868.23)

        rf95.transmit(b"hello world")

        print(rf95.fetch_status())

        while True:
            # Wait for incoming messages to be printed by our handler.
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                sys.exit(0)
```


[pyserial]: https://github.com/pyserial/pyserial/
[rf95modem]: https://github.com/gh0st42/rf95modem
[rf95modem-commit]: https://github.com/gh0st42/rf95modem/commit/8f163aa23e6f0c1ca7403c13b0811366e40b7317

