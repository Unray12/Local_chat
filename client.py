import socket
import threading

HEADER = 1024
PORT = 5070
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!BYE"
SERVER = "172.28.144.1" #IP of server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sock stream is TCP protocol
client.connect(ADDR)

nickname = input("Enter a nickname: ")

connected = True

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
            connected = False
            client.close()
                
def send(msg): # not use
        message = msg.encode(FORMAT)
        messageLength = len(message)
        sendLength = str(messageLength).encode(FORMAT)
        sendLength += b' ' * (HEADER - len(sendLength)) #for sending different packets
        client.send(sendLength)
        client.send(message)

def write():
    global connected
    while connected:
        try:
            message = str(input())
            client.send(message.encode(FORMAT))
            if message == DISCONNECT_MESSAGE:
                connected = False
        except:
            print("Errors occured !!!")
            connected = False
            client.close()

recieveThread = threading.Thread(target = recieve)
recieveThread.start()

writeThread = threading.Thread(target = write)
writeThread.start()

    
     