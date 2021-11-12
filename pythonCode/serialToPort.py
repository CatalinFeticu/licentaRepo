import serial
import time

# crearea clasei -> se face prin sendInfo(numele portulu ex:COM4, baudRate ex pt Arduino: 9600, timout timer ex 0.1)
# apelare activate -> scrie ce vrei sa trimiti catre clasa 

class sendInfo():
    def __init__(self,portCode,baudRate,beforeTimeout):
        self.portCode = portCode
        self.baudRate = baudRate
        self.timeout = beforeTimeout
        self.microController = serial.Serial(port = portCode, baudrate = baudRate, timeout = beforeTimeout)

    def writeData(self,toWrite):
        self.microController.write(bytes(toWrite,"utf-8"))
        time.sleep(.05)
        data = self.microController.readline()
        return data

    def activate(self,x):
        value = self.writeData(x)


    def transformForWriting(self, direction):
        result = {
            "left": "leftPlaceholder",
            "right": "rightPlaceholder",
            "up" : "upPlaceholder",
            "down" : "downPlaceholder",
            "upright": "uprightPlaceholder",
            "upleft": "upleftPlaceholder",
            "downright":"downrightPlaceholder",
            "downleft":"downleftPlaceholder"
        }.get(direction)
        return result

if __name__ == "__main__":
    a = sendInfo('COM1',9600,0.1)
    a.activate("0xff")
    print(a.transformForWriting("upright"))
