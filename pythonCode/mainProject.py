from pythonCode.serialToPort import sendInfo
from pythonCode.handTracking import handTracking

import time
import cv2
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

        cautarePersoana = tk.Button(root, text = "Start", padx = 10, pady = 5, fg = "white", bg = "gray",command = lambda : loopToSend.startCamera(self) )  #mockMethodneedstochange
        cautarePersoana.grid(row = 2, column = 1)
        
        #print(f"%s %s %s"%(portID.get(),baudRate.get(),timeOut.get()))

        root.mainloop()
        ###
    def startCamera(self):
        pTime = 0
        cTime = 0
        cap = cv2.VideoCapture(0)
        tracking = handTracking()
        serialWrite = sendInfo('COM1', 9600, 0.1)  # needs replacement

        while True:
            success, img = cap.read()
            img = tracking.handDetect(img)
            lmList = tracking.handPos(img)
            direction = ""


            if len(lmList) != 0:
                h, w, c = img.shape

                if lmList[0][1] < h/2 - 45:
                    direction += "up"
                if lmList[0][1] > h/2 + 45:
                    direction += "down"
                if lmList[0][0] < w/2 - 45:
                    direction += "left"
                if lmList[0][0] > w/2 + 45:
                    direction += "right"

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)


            finalDirection = serialWrite.transformForWriting(direction)

            print(finalDirection)

            # serialWrite.activate(finalDirection)

            if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
                break
        cv2.destroyAllWindows()

        
if __name__ == "__main__":
    a = loopToSend()
    
