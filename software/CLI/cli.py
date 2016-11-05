class TempLogger():
    def __init__(self):
        self.t = 0
        self.h = 0

    def getTemperature(self):
        self.t += 0.02
        return 666 + self.t

    def getHumidity(self):
        self.h += 0.02
        return 42 + self.h