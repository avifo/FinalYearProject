import socket
import csv
import time

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

file_name = "FileData.txt"

with open('Book1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    header_names = ''
    store_data = []
    for row in csv_reader:
        if line_count == 0:
            # print(f'Columns are {", ".join(row)}')
            line_count += 1
        else:
            # print(row['Thumb'], row['Index'], row['Ring'])
            line_count += 1
            time.sleep(0.00001)
            x = row['Thumb']
            store_data.append(float(x))
            if len(store_data) > 100:
                sum_ = sum(store_data)
                len_ = len(store_data)
                avgMsg = sum_ / len_
                rouMsg = round(avgMsg, 5)
                send(str(rouMsg))
                store_data.clear()

send(DISCONNECT_MESSAGE)
