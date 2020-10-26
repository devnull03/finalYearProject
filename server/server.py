import os, sys, json
import socket
import threading
from database import checkUser
import settings
from impoter import checker


class Server:
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'
    LOGIN_MESSAGE = 'sendInfo'

    def __init__(self, **kwargs):
        self.PORT = kwargs["PORT"]
        self.challenge = {
            "mode": settings.MODE,
            "time": settings.TIME,
            "task": settings.TASK,
            "examples": settings.EXAMPLES
        }
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        # self.login = False
        self.participants = []

    def handle_client(self, conn, addr):
        HEADER = self.HEADER
        FORMAT = self.FORMAT
        SEPARATOR = self.SEPARATOR
        print(f"[NEW CONNECTION] {addr} connected.")
        USER = ''

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                info = msg.split(SEPARATOR)

                if info == 'ping':
                    conn.send('pong'.encode(FORMAT))

                if info[0] == 'login':
                    user = checkUser(SEPARATOR.join((info[1], info[2])))
                    if user == f'True{SEPARATOR}True':
                        # self.login = True
                        print(self.participants)
                        if info[1] not in self.participants:
                            conn.send(user.encode(FORMAT))
                            USER = info[1]
                            self.participants.append(USER)
                        else:
                            conn.send(f'No{SEPARATOR}No'.encode(FORMAT))
                    print(info)

                elif info[0] == self.LOGIN_MESSAGE:
                    conn.send(json.dumps(self.challenge).encode(FORMAT))

                elif info[0] == 'file':
                    with open(f"solutions\\{info[1]}",'w') as file:
                        file.write(info[2])
                    conn.send('Done'.encode(FORMAT))

                elif info[0] == 'example_file':
                    with open(settings.EXAMPLE_FILE, 'r') as file:
                        conn.send(f"challange.py{SEPARATOR}{file.read()}".encode(FORMAT))

                else: 
                    conn.send("None".encode(FORMAT))

                if msg == self.DISCONNECT_MESSAGE:
                    try:
                        self.participants.remove(USER)
                    except:
                        pass
                    connected = False
                if msg != 'start?' and info[0] != 'file':
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


if __name__ == "__main__":
    cwd = os.getcwd()
    if not cwd.endswith('\\server'):
        os.chdir(f"{cwd}\\server")

    print("[STARTING] server is starting...")
    s = Server(PORT=6969)
    s.start()
