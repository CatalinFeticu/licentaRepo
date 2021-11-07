import serial
import time

class sendInfo():
    def __init__(self,portCode,baudRate,beforeTimeout):
        self.portCode = portCode
        self.baudRate = baudRate
        self.timeout = beforeTimeout
        self.microController = serial.Serial(port = portCode, baudrate = baudRate, timeout = beforeTimeout )
    def writeData(self,toWrite):
        self.microController.write(bytes(toWrite,"utf-8"))
        time.sleep(.05)
        data = self.microController.readline()
        return data
    def activate(self,x):
        while True:
            value = self.writeData(self.writeData(x))
            print(value)

if __name__ == "__main__":
    a = sendInfo('COM4',9600,0.1)    
    a.activate("string")

