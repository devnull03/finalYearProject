import pygame
import time

from pygame import mouse
# from modules.pygame_textinput import TextInput
from modules.text_wrapper import drawText


class MainPage:

    mousePos = (0, 0)
    
    def __init__(self, **kwargs):
        pygame.init()
        pygame.display.set_caption("Clash of Code")
        pygame.display.set_icon(pygame.image.load('assets/logo.png'))
        pygame.display.set_caption("Clash of Code")
        self.screenSize = (460, 800)
        self.back = pygame.image.load(r'assets\mainPageBack.png')
        self.mainScreen = pygame.display.set_mode(self.screenSize)
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('Times New Roman', 30)
        self.small_font = pygame.font.SysFont('Times New Roman', 20)
        self.black = (0, 0, 0)

        self.mode = kwargs["mode"]
        self.task = kwargs["task"]
        self.examples = kwargs["examples"]

        self.timerBool = False
        self.t = time.time()
        self.Time = kwargs["time"] * 60
        self.secs = 60
        self.mins = self.Time // 60 - 1

        words = self.task.split()
        print(words)


    def timer(self):
        location = (33, 20)
        if self.timerBool:
            minus = time.time() - self.t
            sec = int(self.secs - minus)
            secc = f"0{sec}" if sec < 10 else sec
            Timer = f"{self.mins}:{secc}"
            if sec < 0:
                self.secs += 60
                self.mins -= 1
                if self.mins < 0:
                    self.timerBool = False
        else:
            Timer = f"{self.mins + 1}:00"

        text = self.Font.render(str(Timer), True, (0, 0, 0))
        self.mainScreen.blit(text, location)

    def dev_button(self, events):

        pos = (20, 240)
        size = (60, 25)
        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(self.mainScreen, (20, 20, 20), pygame.Rect(pos, size))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + size[0] and pos[1] <= mouse[1] <= pos[1] + size[1]:
                    if self.timerBool is False:
                        self.t = time.time()
                    self.timerBool = True

    def finish_button(self, events):

        pos = (200, 640)
        size = (60, 25)
        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(self.mainScreen, (20, 20, 20), pygame.Rect(pos, size))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + size[0] and pos[1] <= mouse[1] <= pos[1] + size[1]:
                    return True

    def display_info(self):
        black = self.black

        mode_location = (200, 19)
        mode_text = self.Font.render(f"Mode - {self.mode}", True, black)
        self.mainScreen.blit(mode_text, mode_location)

        drawText(
            self.mainScreen, self.task, self.black, ((25, 115), (427, 227)), self.small_font
            )

        

    def test_start(self):

        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            # pos = pygame.mouse.get_pos()
            # if pos != self.mousePos:
            #     print(pos)
            #     self.mousePos = pos
            # mainScreen.fill((170, 170, 170))

            self.mainScreen.blit(self.back, (0, 0))
            self.display_info()
            self.dev_button(events)
            self.timer()

            '''
            if self.timerBool:
                self.timer()
            else:
                text = self.Font.render(f"{self.mins + 1}:00", True, (0, 0, 0))
                self.mainScreen.blit(text, (33, 20))
            '''

            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":

    d = {
        "mode": "Shortest",
        "time": 1,
        "task": "Test task ........... .............. .........."
    }

    MainPage(**d).test_start()
