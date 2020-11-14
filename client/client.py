import json
import socket
import sys, os, time
import winshell
from PyQt5 import QtWidgets
import threading
if '\\client' not in (cwd:=os.getcwd()):
    os.chdir(f"{cwd}\\client")
from login import Login
from mainPage import MainPage
from endScreen import EndScreen
import settings

class Client:
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'
    LOGIN_MESSAGE = 'sendInfo'
    def __init__(self) :
        self.SERVER = settings.SERVER
        self.PORT = settings.PORT
        self.ADDR = (self.SERVER, self.PORT)
        self.available = True
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.app = QtWidgets.QApplication(sys.argv)
        while 1:
            try:
                self.client.connect(self.ADDR)
                break
            except ConnectionRefusedError:
                print('Looking for servers')
        self.start_login()

    def send(self, msg):
        message = str(msg).encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        msg = self.client.recv(2048).decode(self.FORMAT)
        self.available = True
        if msg.split(self.SEPARATOR)[0] not in ['None', 'fetch']:
            print(f"[SERVER] {msg}")
        return msg

    def send_file(self, path):
        self.available = False
        with open(path, 'r') as file:
            self.send(f'file{self.SEPARATOR}{self.username}.py{self.SEPARATOR}{file.read()}')

    def start_login(self):
        LoginWindow = QtWidgets.QMainWindow()
        self.app_info = {
                "app": self.app,
                "DISCONNECT_MESSAGE": self.DISCONNECT_MESSAGE,
                "SEPARATOR": self.SEPARATOR,
                "LOGIN_MESSAGE": self.LOGIN_MESSAGE,
                "send-func": self.send,
                "file-func": self.send_file
            }
        login_page = Login(**self.app_info)
        login_page.setupUi(LoginWindow)
        LoginWindow.show()
        if not self.app.exec_():
            self.app.closeAllWindows()

        sucessful, self.username = login_page.result

        if not sucessful:
            self.send(self.DISCONNECT_MESSAGE)
            exit()
        else:
            self.get_info()
            self.start_mainPage()

    def get_info(self):
        self.info = json.loads(self.send(self.LOGIN_MESSAGE))
        example_file = self.send('example_file').split(self.SEPARATOR)

        file_path = f"{winshell.desktop()}\\{example_file[0]}"
        with open(file_path, 'w') as file:
            file.write(example_file[1])

    def show_info(self):
        self.main_page.task = self.info["task"]
        self.main_page.ex = self.info["examples"]
        self.main_page.update()

    def start_check(self):
        while 1:
            time.sleep(0.2)
            if self.available:
                fetched = self.send("fetch").split(self.SEPARATOR)
                if fetched[1] == "True":
                    if not self.main_page.start:
                        self.show_info()
                        self.main_page.count = int(fetched[3])
                    self.main_page.start_timer()
                self.main_page.participants = json.loads(fetched[2])
                self.main_page.update_board()

    def start_mainPage(self):
        MainPageWindow = QtWidgets.QMainWindow()
        self.main_page = MainPage(**self.app_info, **self.info)
        self.main_page.task = ""
        self.main_page.ex = {}
        self.main_page.setupUi(MainPageWindow)
        MainPageWindow.show()

        time_thread = threading.Thread(target=self.start_check)
        time_thread.daemon = True
        time_thread.start()

        if not self.app.exec_():
            self.send(self.DISCONNECT_MESSAGE)
            sys.exit()
    
    def show_EndScreen(self):
        pass

if __name__ == "__main__":
    Client()
 