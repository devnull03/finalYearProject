import socket
import threading
from database import checkUser


class Server:
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'

    def __init__(self, **kwargs):
        self.PORT = kwargs["PORT"]
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

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
                    conn.send(user.encode(FORMAT))
                    print(info)
                    # conn.send(checkUser().encode(FORMAT))

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


print("[STARTING] server is starting...")
Server(PORT=5050).start()
