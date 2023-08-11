import socket
import threading
from tkinter import *
from tkinter import Tk, Entry, messagebox
from client import *

GRAY = "#ABB2B9"
BLUE = "0000FF"
RED = "FF0000"

FONT = "Helvetica"

class GUI:
    def __init__(self):
        self.chatWindow = Tk()
        self.chatWindow.withdraw()

        #log in
        self.login = Toplevel()
        self.login.resizable(
            width=False, 
            height=False
        )
        self.login.title("Login")
        self.login.configure(width=400, height=400)

        self.enterMsg = Label(
            self.login, 
            text="ENTER THE CHAT ROOM",
            justify=CENTER, 
            font=FONT + " 14 bold"
        )
        self.enterMsg.place(
            relheight=0.15, 
            relx=0.2, 
            rely=0.04
        )

        #input name
        self.labelName = Label(
            self.login, 
            text="Name", 
            font=FONT + " 12 bold"
        )
        self.labelName.place(
            relheight=0.2, 
            relx=0.1, 
            rely=0.15
        )

        self.inputName = Entry(
            self.login, 
            font=FONT + " 14", 
            border=2, 
            justify=CENTER
        )
        self.inputName.place(
            relwidth=0.8, 
            relheight=0.10, 
            relx=0.1,
            rely=0.3
        )

        #input IP of server
        self.labelServer = Label(
            self.login, 
            text="IP of server", 
            font=FONT + " 12 bold"
        )
        self.labelServer.place(
            relheight=0.2, 
            relx=0.1, 
            rely=0.4
        )

        self.inputServer = Entry(
            self.login, 
            font=FONT + " 14", 
            border=2, 
            justify=CENTER
        )
        self.inputServer.place(
            relwidth=0.8, 
            relheight=0.10, 
            relx=0.1,
            rely=0.55
        )
        
        #login button
        self.loginBtn = Button(
            self.login, 
            text="LOG IN",
            font=FONT + " 12 bold",
            command=lambda: self.checkNullVal(self.inputName.get(), self.inputServer.get())
        )
        self.loginBtn.place(relx=0.4, rely=0.7)
        
        
        self.chatWindow.mainloop()



    def checkNullVal(self, name, serverIP):
        if (name == '' or serverIP == ''):
            messagebox.showerror("Error !!!", "Please enter a name and server IP.")
        else:
            self.goToChat(name, serverIP)


    def goToChat(self, name, serverIP):
        self.login.destroy()
        setName(name)
        setServer(serverIP)
        self.chatBox(name)

        #start a thread
        connectToServer()
        recieveThread = threading.Thread(target = recieve)
        recieveThread.start()

        writeThread = threading.Thread(target = write)
        writeThread.start()


    def chatBox(self, name):
        self.chatWindow.deiconify()
        self.chatWindow.title("Chat Box")
        self.chatWindow.resizable(width=FALSE, height=FALSE)
        self.chatWindow.configure(width=700, height=800)

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


start = GUI()
