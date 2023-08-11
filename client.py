import socket
import threading
from time import sleep

HEADER = 1024
PORT = 5070
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!BYE"
SERVER = "172.28.144.1" #IP of server


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sock stream is TCP protocol
nickname = ""#input("Enter a nickname: ")

connected = True

def disconnect():
    global client
    global connected
    connected = False
    client.close()

def setName(name): #must have to rename in gui.py
    global nickname
    nickname = name

def setServer(IP):
    global SERVER
    SERVER = IP

def connectToServer():
    ADDR = (SERVER, PORT)   
    client.connect(ADDR)

def recieve():
    global connected
    while connected:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            if message == "!NICK":
                client.send(nickname.encode(FORMAT))
            elif message != "":
                print(message)
        except:
            print("Errors occured !!!")
            disconnect()
                
def send(msg): # not use
        message = msg.encode(FORMAT)
        messageLength = len(message)
        sendLength = str(messageLength).encode(FORMAT)
        sendLength += b' ' * (HEADER - len(sendLength)) #for sending different packets
        client.send(sendLength)
        client.send(message)

def write(message):
    try:
        client.send(message.encode(FORMAT))
    except:
        print("Errors occured !!!")
    if message == DISCONNECT_MESSAGE:
        connected = False

# def write():
#     global connected
#     while connected:
#         try:
#             message = str(input())
#             client.send(message.encode(FORMAT))
#             if message == DISCONNECT_MESSAGE:
#                 connected = False
#         except:
#             print("Errors occured !!!")
#             disconnect()

# recieveThread = threading.Thread(target = recieve)
# recieveThread.start()

# writeThread = threading.Thread(target = write)
# writeThread.start()

    
     