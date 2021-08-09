import matplotlib.pyplot as plt
import socket
import threading
from tkinter import *
from matplotlib import style
import os.path

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
file_name = "FileData.txt"

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

data = []


def handle_client(conn, addr):
    print(f"NEW CONNECTION: {addr} connected to the server")
    connected = True

    if not os.path.exists(file_name):
        f = open(file_name, "x")
        f.close()
    else:
        file = open(file_name, "r+")
        file.truncate(0)
        file.close()

    upload_data = 0
    upload_time = 0
    store_data = []
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            f = open(file_name, "a")
            f.write(msg + "," + str(upload_time) + "\n")
            upload_time += 0.5
            f.close()
            conn.send("Msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"Server is listening from {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    ani = FuncAnimation(plt.gcf(), animate(data), interval=1000)


print("[SERVER IS STARTING]")
start()
