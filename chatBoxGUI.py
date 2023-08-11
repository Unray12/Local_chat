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
        self.chatWindow.configure(width=700, height=700)

        self.contactListLabel = Label(
            self.chatWindow,
            text = "Contact list",
            font = FONT + " 12 bold"
        )
        self.contactListLabel.place(
            relheight = 0.1,
            relwidth = 0.25,
            relx = 0,
            rely = 0
        )

        self.contactList = Label(
            self.chatWindow,
            bg = "grey"
        )
        self.contactList.place(
            relx = 0,
            rely = 0.1,
            relheight = 0.9,
            relwidth = 0.25
        )

        self.friendName = Label(
            self.chatWindow,
            text = "Name of yout friend",
            bg = "lightblue",
        )
        self.friendName.place(
            relx = 0.25,
            rely = 0,
            relheight = 0.1,
            relwidth = 0.75
        )

        self.textBox = Text(
            self.chatWindow,
            bg = "white",
        )
        self.textBox.place(
            relx = 0.25,
            rely = 0.1,
            relheight = 0.8,
            relwidth = 0.75
        )
        self.textBox.config(state=DISABLED)

        self.inputChat = Label(
            self.chatWindow,
            bg = "grey"
        )
        self.inputChat.place(
            relx = 0.25,
            rely = 0.9,
            relheight = 0.1,
            relwidth = 0.75
        )

        self.entryChat = Entry(
            self.chatWindow,
            font = FONT + " 14"
        )
        self.entryChat.place(
            relx = 0.25,
            rely = 0.9,
            relheight = 0.1,
            relwidth = 0.6
        )

        self.sendBtn = Button(
            self.inputChat,
            text = "send",
            font = FONT + " 10"
        )
        self.sendBtn.place(
            relx = 0.8,
            rely = 0,
            relheight = 1,
            relwidth = 0.2
        )

        textScrollbar = Scrollbar(self.textBox)
        textScrollbar.place(
            relx = 0.9738,
            rely = 0,
            relheight = 1,
            #relwidth = 0.01
        )
        textScrollbar.config(command=self.textBox.yview)
        #end main

        self.chatWindow.mainloop()


start = chatBoxGUI()