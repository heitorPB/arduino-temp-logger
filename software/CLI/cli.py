import serial
import struct


class TempLogger():
    def __init__(self, port, baudrate = 115200):
        self.arduino_port = port
        self.arduino_baudrate = baudrate

        self.device = serial.Serial(port, baudrate, timeout = 2)
        if self.testConnection():
            print("Connected to", port, "at", baudrate, "bits/sec")
        else:
            raise ValueError("Arduino didn't anwser the call. Check firmware.")


    def testConnection(self):
        self.device.write(b'e')
        ehlo1 = self.device.read(1)
        ehlo2 = self.device.read(1)
        ehlo3 = self.device.read(1)

        if ehlo1 == b'1' and ehlo2 == b'2' and ehlo3 == b'3':
            print("Right arduino connected.")
            return True
        else:
            return False


    def getTemperature(self):
        self.device.write(b'T')
        ehlo1   = self.device.read(1)
        datalen = self.device.read(1)
        data    = self.device.read(int(datalen))
        ehlo2   = self.device.read(1)

        if ehlo1 == b't' and ehlo2 == b'T':
            return float(data)
        else:
            return None


    def getHumidity(self):
        self.device.write(b'H')
        ehlo1   = self.device.read(1)
        datalen = self.device.read(1)
        data    = self.device.read(int(datalen))
        ehlo2   = self.device.read(1)

        if ehlo1 == b'h' and ehlo2 == b'H':
            return float(data)
        else:
            return None