import json
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
if '\\client' not in (cwd:=os.getcwd()):
    os.chdir(f"{cwd}\\client")



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
    

loginPage = Login()
colors = (loginPage.red, loginPage.green)


def login_screen():
    while 1:
        loginPage.mainScreen.fill((170, 170, 170))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                send(DISCONNECT_MESSAGE)
                pygame.quit()
                return False
            if loginPage.done:
                pygame.quit()
                time.sleep(1)
                return True, loginPage.userName.get_text()
        if loginPage.password_Box(events) or loginPage.userName_Box(events) or loginPage.login_Box(events):
            returned = send(
                SEPARATOR.join(('login', loginPage.userName.get_text(), loginPage.password.get_text()))
            ).split(SEPARATOR)
            loginPage.userColor, loginPage.passColor = colors[returned[0] == 'True'], colors[returned[1] == 'True']
            if returned.count('True') == 2:
                loginPage.done = True
            elif returned[0] == 'No':
                loginPage.cmd = 'Account already in use'
        
        text = loginPage.theOtherFont.render(loginPage.cmd, True, (170, 0, 0))
        loginPage.mainScreen.blit(text, (2, 280))
        pygame.display.update()
        loginPage.clock.tick(30)

sucessful, username = login_screen()

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
