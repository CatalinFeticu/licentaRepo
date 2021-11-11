import serialToPort
from openCVbackend import openCV

import tkinter as tk


class loopToSend():
    def __init__(self):
        
        #region tkinter
        root = tk.Tk()
        root.title("Camera tracker")

        textWidth = 15
        #port defining
        portIdText = tk.Label(text = 'insert portID')
        portIdText.grid(row = 1, column= 0, padx= textWidth)
        self.portID  = tk.Entry(root)
        self.portID.grid(row = 0, column = 0, padx= 10)
        self.portID.insert(0,"COM1")

        #baudRate defining
        baudRateText = tk.Label(text = 'insert BaudRate')
        baudRateText.grid(row = 1, column= 1, padx= textWidth)
        self.baudRate  = tk.Entry(root)
        self.baudRate.grid(row = 0, column = 1, padx= 10)
        self.baudRate.insert(0, 9600)

        #timeOut defining
        timeOutText = tk.Label(text = 'insert timeout')
        timeOutText.grid(row = 1, column= 2, padx= textWidth)
        self.timeOut  = tk.Entry(root)
        self.timeOut.grid(row = 0, column = 2, padx= 10)
        self.timeOut.insert(0, 0.1)

        cautarePersoana = tk.Button(root, text = "Start", padx = 10, pady = 5, fg = "white", bg = "gray",command = lambda : openCV.mockMethod() )  #mockMethodneedstochange
        cautarePersoana.grid(row = 2, column = 1)
        
        #print(f"%s %s %s"%(portID.get(),baudRate.get(),timeOut.get()))

        root.mainloop()
        ###
    
    def camToArduino(cameraDirection):
        sendData = serialToPort.sendInfo()
        

        
if __name__ == "__main__":
    a = loopToSend()
    
