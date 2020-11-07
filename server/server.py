import os, json, sys
import socket
import threading
from PyQt5 import QtWidgets
from database import checkUser
import settings
from impoter import Checker
from serverGui import ServerGui


class Server:
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'
    LOGIN_MESSAGE = 'sendInfo'
    PORT = 6969

    def __init__(self):
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
        self.participants = {}
        self.game_start = False
        self.checker = Checker(
            f"{os.getcwd()}\\solutions",
            settings.SOLUTION_FILE,
            settings.TEST_CASES
        )

        self.start()

    def check_files(self):
        checked = self.checker.check_files()
        for i in checked:
            self.participants[i[0]]['%'] = i[1]
            self.participants[i[0]]['len'] = i[2]
        self.ui.participants = self.participants
        self.ui.update_board()
        print(checked)

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

                if info[0] == 'login':
                    user = checkUser(SEPARATOR.join((info[1], info[2])))
                    if user == f'True{SEPARATOR}True':
                        print(self.participants)
                        if info[1] not in self.participants:
                            conn.send(user.encode(FORMAT))
                            USER = info[1]
                            self.participants.update({USER: {"time": None, "%": None, "len": None, "logged": True}})
                            self.ui.participants = self.participants
                            self.ui.update_board()
                        elif self.participants[info[1]]["logged"] == False:
                            conn.send(user.encode(FORMAT))
                            USER = info[1]
                            self.participants[info[1]]["logged"] = True
                            self.ui.participants = self.participants
                            self.ui.update_board()
                        else:
                            conn.send(f'No{SEPARATOR}No'.encode(FORMAT))
                    else:
                        conn.send(user.encode(FORMAT))
                
                elif info[0] == "fetch":
                    conn.send(
                        SEPARATOR.join(('fetch',str(self.ui.start),json.dumps(self.participants),str(self.ui.count))).encode(FORMAT)
                    )

                elif info[0] == self.LOGIN_MESSAGE:
                    conn.send(json.dumps(self.challenge).encode(FORMAT))

                elif info[0] == 'file':
                    with open(f"solutions\\{info[1]}", 'w') as file:
                        file.write(info[2])
                    conn.send('Done'.encode(FORMAT))
                    t = settings.TIME * 60 - self.ui.count
                    self.participants[USER]["time"] = f"{t // 60}:{'0' * ((s := t % 60) < 10) + str(s)}"
                    self.check_files()

                elif info[0] == 'example_file':
                    with open(settings.EXAMPLE_FILE, 'r') as file:
                        conn.send(f"challange.py{SEPARATOR}{file.read()}".encode(FORMAT))
                else:
                    conn.send("None".encode(FORMAT))

                if msg == self.DISCONNECT_MESSAGE:
                    if self.participants[USER]["time"] is None:
                        self.participants.pop(USER)
                    else:
                        self.participants[USER]["logged"] = False
                    connected = False
                if info[0] not in ('start?','file','fetch'):
                    print(f"[{addr}] {msg}")
        conn.close()

    def start_server(self):
        server = self.server
        server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 2}")

    def start(self):
        self.checker.clean_folder()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ServerGui(**self.challenge, participants=self.participants)
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        thread = threading.Thread(target=self.start_server)
        thread.daemon = True
        thread.start()
        if app.exec_():
            sys.exit()


if __name__ == "__main__":
    cwd = os.getcwd()
    if not cwd.endswith('\\server'):
        os.chdir(f"{cwd}\\server")
    print("[STARTING] server is starting...")
    Server()
 