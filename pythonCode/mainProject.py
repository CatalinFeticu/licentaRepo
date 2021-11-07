import serialToPort
from openCVbackend import openCV

import tkinter as tk


class loopToSend():
    def __init__(self):
        root = tk.Tk()

        cautarePersoana = tk.Button(root, text = "Cauta persoana dorita", padx = 10, pady = 5, fg = "white", bg = "black",command = lambda : openCV.mockMethod() )
        cautarePersoana.pack()
        
        root.mainloop()
                

if __name__ == "__main__":
    a = loopToSend()
    
