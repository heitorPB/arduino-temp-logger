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
            raise ValueError("Arduino didn't anwser the call. Check firmware and connection. Make sure no other software is using the port", port)


    def testConnection(self):
        self.device.write(b'e')
        ehlo0 = self.device.read(1)
        ehlo1 = self.device.read(1)
        ehlo2 = self.device.read(1)
        ehlo3 = self.device.read(1)
        ehlo4 = self.device.read(1)

        if ehlo0 == b'e' and ehlo1 == b'1' and ehlo2 == b'2' and ehlo3 == b'3' and ehlo4 == b'E':
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

        if ehlo1 == b't' and ehlo2 == b'T' and float(data) != -50:
            return float(data)
        else:
            return None


    def getHumidity(self):
        self.device.write(b'H')
        ehlo1   = self.device.read(1)
        datalen = self.device.read(1)
        data    = self.device.read(int(datalen))
        ehlo2   = self.device.read(1)

        if ehlo1 == b'h' and ehlo2 == b'H' and float(data) != -50:
            return float(data)
        else:
            return None