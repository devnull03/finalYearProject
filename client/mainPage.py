import pygame, time, os
#from modules.pygame_textinput import TextInput
'''
with open("client/temp/nothingToSeeHere.txt") as tempFile :
    userName = tempFile.read()
os.remove("client/temp/nothingToSeeHere.txt")
'''


screenSize = (460,800)
mainScreen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

timerBool = False

Font = pygame.font.SysFont('Times New Roman',30)

#--------------Timer Function---------------#
t=time.time()
Time = 15*60
secs = 60
mins = Time//60 -1    
def timer(location) :
    global secs
    global mins
    minus = time.time()-t
    sec = int(secs-minus)
    secc = f"0{sec}" if sec<10 else sec
    Timer = f"{mins}:{secc}"
    if sec < 0 : 
        secs+=60
        mins-=1
    #pygame.draw.rect()
    text = Font.render(str(Timer),True,(0,0,0))
    mainScreen.blit(text,location)
#--------------------------------------------#
#-----------------A button-------------------#
def button(events):
    global timerBool
    global t

    pos = (200,24)
    size = (60,25)
    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(mainScreen,(20,20,20),pygame.Rect(pos,size))

    for event in events :
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pos[0] <= mouse[0] <= pos[0]+size[0] and pos[1] <= mouse[1] <= pos[1]+size[1] :
                if timerBool is False : t = time.time()
                timerBool = True
#--------------------------------------------#

def startMainPage() :
    pygame.init()
    pygame.display.set_caption("Clash of Code")
    back = pygame.image.load(r'client\assets\mainPageBack.png')

    while 1 :
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
                exit()
        #mainScreen.fill((170, 170, 170))
        mainScreen.blit(back,(0,0))

        button(events)
        if timerBool :
            timer((33,20))
        else :
            text = Font.render(f"{mins+1}:00",True,(0,0,0))
            mainScreen.blit(text,(33,20))


        pygame.display.update()
        clock.tick(30)

