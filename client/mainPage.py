import pygame
import time
import os
from modules.pygame_textinput import TextInput
from modules.text_wrapper import drawText


class MainPage:
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
        self.smaller_font = pygame.font.SysFont('Times New Roman', 17)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.mousePos = (0, 0)

        self.mode = kwargs["mode"]
        self.task = kwargs["task"]
        self.examples = kwargs["examples"]
        self.default_path = kwargs["default_path"]
        self.file_path = TextInput(font_size=20, max_string_length=60, initial_string=self.default_path)
        self.path_box_bool = False

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

    def finish_gui(self, events):
        pos = (325, 580)
        size = (95, 29)
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(self.mainScreen, (20, 20, 20), pygame.Rect(pos, size))
        pygame.draw.rect(self.mainScreen, self.black, pygame.Rect(box_pos:=(20, 581), box_size:=(281, 28)), 1)

        self.mainScreen.blit(self.file_path.get_surface(), (25, 587))

        location = (pos[0]+10, pos[1]+3)
        text = self.small_font.render("Send file", True, self.white)
        self.mainScreen.blit(text, location)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + size[0] and pos[1] <= mouse[1] <= pos[1] + size[1]:
                    self.path_box_bool = False
                    return self.file_path.get_text()
                if box_pos[0] <= mouse[0] <= box_pos[0] + box_size[0] and box_pos[1] <= mouse[1] <= box_pos[1] + box_size[1]:
                    self.path_box_bool = True
                else:
                    self.path_box_bool = False
        if self.path_box_bool:
            self.file_path.update(events)

    def display_info(self):
        black = self.black
        mode_location = (200, 19)
        mode_text = self.Font.render(f"Mode - {self.mode}", True, black)
        self.mainScreen.blit(mode_text, mode_location)
        drawText(self.mainScreen, self.task, self.black, ((25, 115), (427, 227)), self.small_font)
        # (19, 359), (447, 499)
        example_location = (25, 396)
        example_text = self.small_font.render("Examples :", True, black)
        self.mainScreen.blit(example_text, (25,366))
        n = 0
        for i in self.examples:
            example = self.smaller_font.render(f"solution({i})-> {self.examples[i]}", True, black)
            self.mainScreen.blit(example, (example_location[0], example_location[1]+n))
            n += 30

    def test_start(self):
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            if 0:
                pos = pygame.mouse.get_pos()
                if pos != self.mousePos:
                    print(pos)
                    self.mousePos = pos
                self.mainScreen.fill((170, 170, 170))

            self.mainScreen.blit(self.back, (0, 0))
            self.display_info()
            self.dev_button(events)
            self.timer()
            if a:=self.finish_gui(events):
                print(a)

            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":
    cwd = os.getcwd()
    if '\\client' not in cwd:
        os.chdir(f"{cwd}\\client")

    d = {
        "mode": "Shortest",
        "time": 1,
        "task": "Test task " * 10,
        "examples": {
            1: 1,
            2: 4,
            3: 9
        },
        "default_path": "C:\\Users\\Dell\\OneDrive\\Desktop"
    }

    MainPage(**d).test_start()
