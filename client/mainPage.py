import pygame
import time
# from modules.pygame_textinput import TextInput


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
        self.black = (0, 0, 0)

        self.mode = kwargs["mode"]
        self.task = kwargs["task"]

        self.timerBool = False
        self.t = time.time()
        self.Time = kwargs["time"] * 60
        self.secs = 60
        self.mins = self.Time // 60 - 1

        words = self.task.split()
        print(words)


    def timer(self):
        location = (33, 20)
        minus = time.time() - self.t
        sec = int(self.secs - minus)
        secc = f"0{sec}" if sec < 10 else sec
        Timer = f"{self.mins}:{secc}"
        if sec < 0:
            self.secs += 60
            self.mins -= 1

        text = self.Font.render(str(Timer), True, (0, 0, 0))
        self.mainScreen.blit(text, location)

    def button(self, events):

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

    def display_info(self):
        black = self.black

        mode_location = (200, 19)
        mode_text = self.Font.render(f"Mode - {self.mode}", True, black)
        self.mainScreen.blit(mode_text, mode_location)

        task_location = (25, 115)
        task_text = self.small_font.render(self.task, True, black)
        self.mainScreen.blit(task_text, task_location)

    def test_start(self):

        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            # mainScreen.fill((170, 170, 170))
            self.mainScreen.blit(self.back, (0, 0))
            self.display_info()

            self.button(events)
            if self.timerBool:
                self.timer()
            else:
                text = self.Font.render(f"{self.mins + 1}:00", True, (0, 0, 0))
                self.mainScreen.blit(text, (33, 20))

            pygame.display.update()
            self.clock.tick(30)


if __name__ == "__main__":

    d = {
        "mode": "Shortest",
        "time": 15,
        "task": "wwwwwwwwwwwwwwwwwwwwwwwwwwwww 123456789012345678901234567890"
    }
    print(len(d["task"]), len("123456789012345678901234567890"))
    MainPage(**d).test_start()
