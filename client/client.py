import json
import socket
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
if '\\client' not in (cwd:=os.getcwd()):
    os.chdir(f"{cwd}\\client")
from pyqt5_stuff.login import Login


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

def send_file(path, file_name):
    with open(path, 'r') as file:
        send(f'file{SEPARATOR}{file_name}{SEPARATOR}{file.read()}')

app = QtWidgets.QApplication(sys.argv)
LoginWindow = QtWidgets.QMainWindow()
info = {
        "app": app,
        "DISCONNECT_MESSAGE": DISCONNECT_MESSAGE,
        "SEPARATOR": SEPARATOR,
        "LOGIN_MESSAGE": LOGIN_MESSAGE,
        "send-func": send
    }
login_page = Login(**info)
login_page.setupUi(LoginWindow)
LoginWindow.show()
if not app.exec_():
    app.quit()

sucessful, username = login_page.result

print('------------test------------')

if not sucessful:
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

main_page = MainPage(**info, default_path=file_path)

def main_screen():
    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                send(DISCONNECT_MESSAGE)
                return False

        main_page.mainScreen.blit(main_page.back, (0, 0))
        main_page.display_info()
        # main_page.dev_button(events)
        if not main_page.timerBool:
            if send("start?") == "True":
                main_page.timerBool = True
        main_page.timer()

        if a:=main_page.finish_gui(events):
            send_file(a, f'{username}.py')

        pygame.display.update()
        main_page.clock.tick(30)

main_screen()
