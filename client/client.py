import socket
import pygame
import time
from login import Login

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SEPARATOR = '<SEP>'
SERVER = "192.168.29.105"
ADDR = (SERVER, PORT)

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
    print(msg)
    return msg


pygame.init()
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
                return True

        if loginPage.password_Box(events) or loginPage.userName_Box(events) or loginPage.login_Box(events):
            returned = send(
                SEPARATOR.join(('login', loginPage.userName.get_text(), loginPage.password.get_text()))
            ).split(SEPARATOR)

            loginPage.userColor, loginPage.passColor = colors[returned[0] == 'True'], colors[returned[1] == 'True']
            if returned.count('True') == 2:
                loginPage.done = True

        text = loginPage.theOtherFont.render(loginPage.cmd, True, (170, 0, 0))
        loginPage.mainScreen.blit(text, (2, 280))

        pygame.display.update()
        loginPage.clock.tick(30)


print(login_screen())
print(
    '------------test------------'
)
send(DISCONNECT_MESSAGE)
