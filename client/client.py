import json
import socket
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
if '\\client' not in (cwd:=os.getcwd()):
    os.chdir(f"{cwd}\\client")
from login import Login
from mainPage import MainPage

HEADER = 64
PORT = 6969
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SEPARATOR = '<SEP>'
SERVER = "192.168.29.105"
ADDR = (SERVER, PORT)
LOGIN_MESSAGE = 'sendInfo'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    try:
        client.connect(ADDR)
        break
    except ConnectionRefusedError:
        print('Looking for servers')

def send(msg):
    message = str(msg).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    msg = client.recv(2048).decode(FORMAT)
    if msg != 'None':
        print(msg)
    return msg

def send_file(path):
    with open(path, 'r') as file:
        send(f'file{SEPARATOR}{username}.py{SEPARATOR}{file.read()}')

app = QtWidgets.QApplication(sys.argv)
LoginWindow = QtWidgets.QMainWindow()
app_info = {
        "app": app,
        "DISCONNECT_MESSAGE": DISCONNECT_MESSAGE,
        "SEPARATOR": SEPARATOR,
        "LOGIN_MESSAGE": LOGIN_MESSAGE,
        "send-func": send,
        "file-func": send_file
    }
login_page = Login(**app_info)
login_page.setupUi(LoginWindow)
LoginWindow.show()
if not app.exec_():
    app.quit()

sucessful, username = login_page.result

print('------------test------------')

if not sucessful:
    send(DISCONNECT_MESSAGE)
    exit()

d = {
    "mode": "Shortest",
    "time": 15,
    "task": "Test"*10
}

info = json.loads(send(LOGIN_MESSAGE))
user = os.path.abspath('client.py').split('\\')[2]
file_path = f"C:\\Users\\{user}"
example_file = send('example_file').split(SEPARATOR)
if "Desktop" not in os.listdir(file_path):
    file_path = f"{file_path}\\Onedrive\\Desktop\\{example_file[0]}"
else:
    file_path = f"{file_path}\\Desktop\\{example_file[0]}"
with open(file_path, 'w') as file:
    file.write(example_file[1])
# time.sleep(3)

app = QtWidgets.QApplication(sys.argv)
MainPageWindow = QtWidgets.QMainWindow()
main_page = MainPage(**app_info, **info)
main_page.setupUi(MainPageWindow)
MainPageWindow.show()
if not app.exec_():
    send(DISCONNECT_MESSAGE)
    sys.exit()
