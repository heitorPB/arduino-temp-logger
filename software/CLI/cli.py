import serial


class TempLogger():
    def __init__(self, port, baudrate = 115200):
        self.t = 0
        self.h = 0
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
        self.t += 0.02
        return 666 + self.t


    def getHumidity(self):
        self.h += 0.02
        return 42 + self.h