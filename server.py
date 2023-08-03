import socket
import threading

HEADER = 1024
PORT = 5070
SERVER = socket.gethostbyname(socket.gethostname()) #get server IP
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!BYE"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clientsList = []
nicknames = []

def broadcast(message):
    for clients in clientsList:
        clients.send(message)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    index = clientsList.index(conn)
    nickname = nicknames[index]

    connected = True
    while connected:
        try:
            #messageLength = conn.recv(HEADER).decode(FORMAT)
            #if messageLength:
                #messageLength = int(messageLength)
            message = conn.recv(HEADER).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
            if message != "":
                print(f"[{addr}] ({nickname}): {message}")
                broadcast(f"{nickname}: {message}".encode(FORMAT))
        except:
            connected = False
    conn.close()
    nicknames.remove(nickname)
    clientsList.remove(conn)
    broadcast(f"{nickname} has left the chat!".encode(FORMAT))
        
def start():
    print("[STARTING] Server is starting ...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        conn.send("!NICK".encode(FORMAT))
        nickname = conn.recv(HEADER).decode(FORMAT)
        
        nicknames.append(nickname)
        clientsList.append(conn)
       
        conn.send("Connected to server!".encode(FORMAT))
        broadcast(f"{nickname} joined the chat!".encode(FORMAT))

        thread = threading.Thread(target = handleClient, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

start()
