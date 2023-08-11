from tkinter import *
from tkinter import Tk, Entry, messagebox
from client import *

GRAY = "#ABB2B9"
BLUE = "0000FF"
RED = "FF0000"

FONT = "Helvetica"

class chatBoxGUI:
    def __init__(self):
        self.chatWindow = Tk()
        #main
        self.chatWindow.title("Chat Box")
        self.chatWindow.resizable(width=FALSE, height=FALSE)
        self.chatWindow.configure(width=700, height=800)
        #end main

        self.chatWindow.mainloop()


start = chatBoxGUI()