from typing import Text
import serialToPort
from openCVbackend import openCV

import tkinter as tk


class loopToSend():
    def __init__(self):
        
        #region tkinter
        root = tk.Tk()

        textWidth = 15
    
        portIdText = tk.Label(text = 'insert portID')
        portIdText.grid(row = 1, column= 0, padx= textWidth)
        portID  = tk.Entry(root)
        portID.grid(row = 0, column = 0, padx= 10)

        baudRateText = tk.Label(text = 'insert BaudRate')
        baudRateText.grid(row = 1, column= 1, padx= textWidth)
        baudRate  = tk.Entry(root)
        baudRate.grid(row = 0, column = 1, padx= 10)
        baudRate.insert(0, "9600")

        timeOutText = tk.Label(text = 'insert timeout')
        timeOutText.grid(row = 1, column= 2, padx= textWidth)
        timeOut  = tk.Entry(root)
        timeOut.grid(row = 0, column = 2, padx= 10)
        timeOut.insert(0, "0.1")

        cautarePersoana = tk.Button(root, text = "Start", padx = 10, pady = 5, fg = "white", bg = "black",command = lambda : openCV.mockMethod() )
        cautarePersoana.grid(row = 2, column = 1)
        
        root.mainloop()
        ###
    
    def camToArduino(cameraDirection):
        sendData = serialToPort.sendInfo()

                

if __name__ == "__main__":
    a = loopToSend()
    
