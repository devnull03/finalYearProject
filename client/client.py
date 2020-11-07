import json
import socket
import sys, os, time
from PyQt5 import QtWidgets
import threading
if '\\client' not in (cwd:=os.getcwd()):
    os.chdir(f"{cwd}\\client")
from login import Login
from mainPage import MainPage

class Client:
    HEADER = 64
    PORT = 6969
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SEPARATOR = '<SEP>'
    LOGIN_MESSAGE = 'sendInfo'
    def __init__(self) :
        self.SERVER = "192.168.29.105"
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
        time.sleep(0.5)
        self.client.send(message)
        msg = self.client.recv(2048).decode(self.FORMAT)
        self.available = True
        if msg != 'None':
            print(msg)
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

        print('------------test------------')

        if not sucessful:
            self.send(self.DISCONNECT_MESSAGE)
            exit()
        else:
            self.get_info()
            self.start_mainPage()

    def get_info(self):
        self.info = json.loads(self.send(self.LOGIN_MESSAGE))
        user = os.path.abspath('client.py').split('\\')[2]
        file_path = f"C:\\Users\\{user}"
        example_file = self.send('example_file').split(self.SEPARATOR)
        if "Desktop" not in os.listdir(file_path):
            file_path = f"{file_path}\\Onedrive\\Desktop\\{example_file[0]}"
        else:
            file_path = f"{file_path}\\Desktop\\{example_file[0]}"
        with open(file_path, 'w') as file:
            file.write(example_file[1])

    def start_check(self):
        while 1:
            time.sleep(0.2)
            if self.available:
                if self.send("start?") == "yes":
                    self.main_page.start_timer()
                    return

    def start_mainPage(self):
        MainPageWindow = QtWidgets.QMainWindow()
        self.main_page = MainPage(**self.app_info, **self.info)
        self.main_page.setupUi(MainPageWindow)
        MainPageWindow.show()

        thread = threading.Thread(target=self.start_check)
        thread.daemon = True
        thread.start()

        if not self.app.exec_():
            self.send(self.DISCONNECT_MESSAGE)
            sys.exit()

if __name__ == "__main__":
    Client()
