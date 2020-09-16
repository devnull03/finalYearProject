import pygame
#from modules.pygame_textinput import TextInput

pygame.init()

size = (460,800)
mainScreen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

Font = pygame.font.SysFont('Times New Roman',17)

while 1 :
    
    mainScreen.fill((170, 170, 170))
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    text = Font.render("",True,(0,0,0))
    mainScreen.blit(text,(10,10))

    pygame.display.update()
    clock.tick(30)

