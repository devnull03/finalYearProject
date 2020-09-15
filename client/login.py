import pygame
import sys, os
curPath = os.getcwd()
sys.path.append(curPath)
from modules.pygame_textinput import TextInput
from client.echo_client import sendCred

pygame.init()
mainScreen = pygame.display.set_mode((550,300))
clock = pygame.time.Clock()

userName,userBool = TextInput(font_size=25,max_string_length=16),False
password,passBool = TextInput(font_size=25,max_string_length=16),False

theFont = pygame.font.SysFont('Times New Roman',20)
theOtherFont = pygame.font.SysFont('Times New Roman',17)

def userName_Box(events) :
    mouse = pygame.mouse.get_pos()
    global userBool
    pos = (170,110)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                userBool = True
            else : userBool = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                userBool = False
    if userBool :
        a = userName.update(events)

    text = theFont.render("Username :",True,(0,0,0))
    mainScreen.blit(text,(pos[0],pos[1]-25))

    hover = pygame.Surface((200,30), pygame.SRCALPHA)
    hover.fill((100,100,100,90))
    mainScreen.blit(hover,pos)
    mainScreen.blit(userName.get_surface(), (pos[0]+10,pos[1]+5))

def password_Box(events) :
    mouse = pygame.mouse.get_pos()
    global passBool
    pos = (170,180)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                passBool = True
            else : passBool = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                passBool = False
    if passBool :
        a = password.update(events)

    text = theFont.render("Password :",True,(0,0,0))
    mainScreen.blit(text,(pos[0],pos[1]-25))

    hover = pygame.Surface((200,30), pygame.SRCALPHA)
    hover.fill((100,100,100,90))
    mainScreen.blit(hover,pos)
    mainScreen.blit(password.get_surface(), (pos[0]+10,pos[1]+5))

def login_Box(events) :
    mouse = pygame.mouse.get_pos()
    pos = (200,220)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                sendCred(userName.get_text(),password.get_text())

    pygame.draw.rect(mainScreen,(20,20,20),pygame.Rect(pos,(140,25)))

    text = theOtherFont.render("LogIN",True,(200,200,200))
    mainScreen.blit(text,(pos[0]+44,pos[1]+1))


while True:
    mainScreen.fill((225, 225, 225))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()


    userName_Box(events)
    password_Box(events)
    login_Box(events)

    pygame.display.update()
    clock.tick(30)
