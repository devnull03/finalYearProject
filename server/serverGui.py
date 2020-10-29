import pygame
import os
import time

class serverGui:

    def __init__(self, **kwargs):
        pygame.init()
        pygame.display.set_caption("Clash of Code | Admin")
        pygame.display.set_icon(pygame.image.load('assets/logo.png'))
        self.display_size = (600, 350)
        self.mainScreen = pygame.display.set_mode(self.display_size)
        self.clock = pygame.time.Clock()

        self.background_color = (170, 170, 170)
        self.white = (255, 255, 255)
        self.Font = pygame.font.SysFont('Times New Roman', 20)
        self.smallFont = pygame.font.SysFont('Times New Roman', 17)
        
        self.participants = kwargs["participants"]
        
        self.timerBool = False
        self.t = time.time()
        self.Time = kwargs["time"] * 60
        self.secs = 60
        self.mins = self.Time // 60 - 1

    def timer(self):
        location = (30, 20)
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

    def start_button(self, events):
        pos = (499, 297)
        size = (60, 25)
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(self.mainScreen, (100, 100, 100), pygame.Rect(pos, size))
        pygame.draw.rect(self.mainScreen, self.white, pygame.Rect(pos, size), 2)

        text = self.smallFont.render("Start", True, (0, 0, 0))
        self.mainScreen.blit(text, (pos[0]+13, pos[1]+2))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + size[0] and pos[1] <= mouse[1] <= pos[1] + size[1]:
                    if self.timerBool is False:
                        self.t = time.time()
                    self.timerBool = True

    def testRun(self):
        while 1:
            self.mainScreen.fill(self.background_color)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            self.timer()
            self.start_button(events)

            pygame.display.update()


if __name__ == "__main__":
    cwd = os.getcwd()
    if '\\server' not in cwd:
        os.chdir(f"{cwd}\\server")

    serverGui(time=1).testRun()

