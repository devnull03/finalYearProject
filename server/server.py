import sys
import json
import socket
import threading
from database import checkUser


class Server:
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'
    LOGIN_MESSAGE = 'sendInfo'

    def __init__(self, **kwargs):
        self.PORT = kwargs["PORT"]
        self.files = kwargs["file"]["server_files"]
        self.challenge = kwargs["file"]["challenge_info"]
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.login = False


    def send(self, conn, msg):
        FORMAT = self.FORMAT
        HEADER = self.HEADER

        message = str(msg).encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        conn.send(send_length)
        conn.send(message)
        msg = conn.recv(2048).decode(FORMAT)
        print(msg)
        return msg

    def handle_client(self, conn, addr):
        HEADER = self.HEADER
        FORMAT = self.FORMAT
        SEPARATOR = self.SEPARATOR
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                info = msg.split(SEPARATOR)

                if info[0] == 'login':
                    user = checkUser(SEPARATOR.join((info[1], info[2])))
                    if user == f'True{SEPARATOR}True':
                        self.login = True
                    conn.send(user.encode(FORMAT))
                    print(info)
                elif info[0] == self.LOGIN_MESSAGE:
                    # conn.send(json.dumps(self.challenge).encode(FORMAT))
                    with open(sys.argv[1]) as file:
                        conn.send(file.read().encode(FORMAT))
                elif info[0] == 'file':
                    with open(f"solutions\\{info[1]}",'w') as file:
                        file.write(info[2])
                    conn.send('Done'.encode(FORMAT))
                elif info[0] == 'example_file':
                    with open(self.files["default_file"], 'r') as file:
                        conn.send(
                            f"challange.py{SEPARATOR}{file.read()}".encode(FORMAT)
                        )

                if msg == self.DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
        conn.close()

    def start(self):
        server = self.server
        server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if len(sys.argv) > 1:
    try:
        with open(sys.argv[1], 'r') as json_file:
            json_file = json.load(json_file)
    except FileNotFoundError:
        json_file = None
        print('File not found')
        sys.exit()
else:
    json_file = None
    print('No file specified')
    sys.exit()

print("[STARTING] server is starting...")
s = Server(PORT=5050, file=json_file)
s.start()
