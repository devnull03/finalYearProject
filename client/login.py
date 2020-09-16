import pygame
import sys, os
curPath = os.getcwd()
sys.path.append(curPath)
from modules.pygame_textinput import TextInput
from client.mainClient import sendCred

pygame.init()
mainScreen = pygame.display.set_mode((550,300))
clock = pygame.time.Clock()

userName,userBool = TextInput(font_size=25,max_string_length=16),True
password,passBool = TextInput(font_size=25,max_string_length=16),False
red,green = (255,0,0),(0,255,0)

theFont = pygame.font.SysFont('Times New Roman',20)
theOtherFont = pygame.font.SysFont('Times New Roman',17)

eeee = False
userColor,passColor = (100,100,100),(100,100,100)

def userName_Box(events) :
    mouse = pygame.mouse.get_pos()
    global passBool
    global userBool
    pos = (170,110)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                userBool = True
            else : userBool = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_TAB :
                passBool = True
                userBool = False
            if event.key == pygame.K_ESCAPE :
                userBool = False
    if userBool :
        a = userName.update(events)
        if a:
            check()

    text = theFont.render("Username :",True,(0,0,0))
    mainScreen.blit(text,(pos[0],pos[1]-25))

    pygame.draw.rect(mainScreen,userColor,pygame.Rect((pos[0]-50,pos[1]),(30,30)))

    hover = pygame.Surface((200,30), pygame.SRCALPHA)
    hover.fill((100,100,100,90))
    mainScreen.blit(hover,pos)
    mainScreen.blit(userName.get_surface(), (pos[0]+10,pos[1]+6))

def password_Box(events) :
    mouse = pygame.mouse.get_pos()
    global passBool
    global userBool
    pos = (170,180)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                passBool = True
            else : passBool = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_TAB :
                userBool = True
                passBool = False
            if event.key == pygame.K_ESCAPE :
                passBool = False
    if passBool :
        a = password.update(events)
        if a :
            check()

    text = theFont.render("Password :",True,(0,0,0))
    mainScreen.blit(text,(pos[0],pos[1]-25))

    pygame.draw.rect(mainScreen,passColor,pygame.Rect((pos[0]-50,pos[1]),(30,30)))

    hover = pygame.Surface((200,30), pygame.SRCALPHA)
    hover.fill((100,100,100,90))
    mainScreen.blit(hover,pos)
    mainScreen.blit(password.get_surface(), (pos[0]+10,pos[1]+6))

def login_Box(events) :
    mouse = pygame.mouse.get_pos()
    pos = (200,220)

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+200 and pos[1] <= mouse[1] <= pos[1]+30 :
                check()

    pygame.draw.rect(mainScreen,(20,20,20),pygame.Rect(pos,(140,25)))

    text = theOtherFont.render("LogIN",True,(200,200,200))
    mainScreen.blit(text,(pos[0]+44,pos[1]+1))

def check():
    global eeee
    global userColor
    global passColor

    b = sendCred(userName.get_text(),password.get_text()).split("<SEP>")
    if b[0]=="True" :
        userColor = green
        if b[1]=="True" :
            passColor = green
            eeee = True
        else : passColor = red
    else : 
        userColor = red
        passColor = red


while True:
    mainScreen.fill((225, 225, 225))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            raise TypeError("False")
            exit()
        if eeee : 
            raise BaseException("True")
            exit()

    password_Box(events)
    userName_Box(events)
    login_Box(events)

    pygame.display.update()
    clock.tick(30)
