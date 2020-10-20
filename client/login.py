import pygame
from modules.pygame_textinput import TextInput


class Login:

    def __init__(self):
        pygame.display.set_caption("Login")
        pygame.display.set_icon(pygame.image.load('assets/logo.png'))
        self.mainScreen = pygame.display.set_mode((550, 300))
        self.clock = pygame.time.Clock()

        self.userName, self.userBool = TextInput(font_size=25, max_string_length=16), True
        self.password, self.passBool = TextInput(font_size=25, max_string_length=16), False
        self.red, self.green = (170, 0, 0), (0, 170, 0)

        self.theFont = pygame.font.SysFont('Times New Roman', 20)
        self.theOtherFont = pygame.font.SysFont('Times New Roman', 17)

        self.cmd = ''
        self.userColor, self.passColor = (100, 100, 100), (100, 100, 100)
        self.done = False

    def userName_Box(self, events):
        mouse = pygame.mouse.get_pos()
        pos = (190, 110)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + 200 and pos[1] <= mouse[1] <= pos[1] + 30:
                    self.userBool = True
                else:
                    self.userBool = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.passBool = True
                    self.userBool = False
                if event.key == pygame.K_ESCAPE:
                    self.userBool = False
        if self.userBool:
            a = self.userName.update(events)
            if a:
                self.check()
                return True

        text = self.theFont.render("Username :", True, (0, 0, 0))
        self.mainScreen.blit(text, (pos[0], pos[1] - 25))

        pygame.draw.rect(self.mainScreen, self.userColor, pygame.Rect((pos[0] - 50, pos[1]), (30, 30)))

        hover = pygame.Surface((200, 30), pygame.SRCALPHA)
        hover.fill((100, 100, 100, 90))
        self.mainScreen.blit(hover, pos)
        self.mainScreen.blit(self.userName.get_surface(), (pos[0] + 10, pos[1] + 6))

    def password_Box(self, events):
        mouse = pygame.mouse.get_pos()
        pos = (190, 180)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + 200 and pos[1] <= mouse[1] <= pos[1] + 30:
                    self.passBool = True
                else:
                    self.passBool = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.userBool = True
                    self.passBool = False
                if event.key == pygame.K_ESCAPE:
                    self.passBool = False
        if self.passBool:
            a = self.password.update(events)
            if a:
                self.check()
                return True

        text = self.theFont.render("Password :", True, (0, 0, 0))
        self.mainScreen.blit(text, (pos[0], pos[1] - 25))

        pygame.draw.rect(self.mainScreen, self.passColor, pygame.Rect((pos[0] - 50, pos[1]), (30, 30)))

        hover = pygame.Surface((200, 30), pygame.SRCALPHA)
        hover.fill((100, 100, 100, 90))
        self.mainScreen.blit(hover, pos)
        self.mainScreen.blit(self.password.get_surface(), (pos[0] + 10, pos[1] + 6))

    def login_Box(self, events):
        mouse = pygame.mouse.get_pos()
        pos = (220, 220)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] <= mouse[0] <= pos[0] + 200 and pos[1] <= mouse[1] <= pos[1] + 30:
                    self.check()
                    return True

        pygame.draw.rect(self.mainScreen, (20, 20, 20), pygame.Rect(pos, (140, 25)))

        text = self.theOtherFont.render("LogIN", True, (200, 200, 200))
        self.mainScreen.blit(text, (pos[0] + 44, pos[1] + 1))

    def check(self):
        self.entered = True

    def testing_start(self):
        while True:
            self.mainScreen.fill((170, 170, 170))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    # time.sleep(1)
                    # send("!DISCONNECT")
                    self.done = (True, False)
                    pygame.quit()
                    return False

                if self.eeee:
                    # send("!DISCONNECT")
                    # return userName.get_text()
                    self.done = (True, True)
                    pygame.quit()
                    return True

            self.password_Box(events)
            self.userName_Box(events)
            self.login_Box(events)

            text = self.theOtherFont.render(self.cmd, True, (170, 0, 0))
            self.mainScreen.blit(text, (2, 280))

            pygame.display.update()
            self.clock.tick(30)

"""
def check():
    global eeee
    global userColor
    global passColor
    global cmd
    global entered
    entered = True

    toSend = f'{userName.get_text()}<SEP>{password.get_text()}'

    try:

        b = send(toSend)  # sendCred((user:=userName.get_text()),password.get_text()).split("<SEP>")
        cmd = ""
        if b[0] == "True":
            userColor = green
            if b[1] == "True":
                passColor = green
                eeee = True
                if "temp" not in os.listdir("client"):
                    os.mkdir('client/temp')
                with open("client/temp/nothingToSeeHere.txt", "w") as tempFile:
                    tempFile.write(userName.get_text())
            else:
                passColor = red
        else:
            userColor = red
            passColor = red
    except:
        print(c := "Server not found, try again")
        cmd = c
"""
'''
class Login:
    def __init__(self):
        # self.entered = entered
        # self.run += 1
        pass

    @staticmethod
    def run():
        startLogin()

    @property
    def running(self):
        global done
        return not any(done)

    @property
    def get_input(self):
        toSend = f'{userName.get_text()}<SEP>{password.get_text()}'
        return toSend

    def send_result(self, result_tuple, _cmd=""):
        global userColor
        global passColor
        global cmd
        global eeee
        if type(result_tuple) is list or type(result_tuple) is tuple:
            if result_tuple[0] == "True":
                userColor = green
                if result_tuple[1] == "True":
                    passColor = green
                    eeee = True
                else:
                    passColor = red
            else:
                userColor = red
                passColor = red

    @property
    def got_input(self):
        global entered
        if entered is True:
            entered = False
            return True

    @property
    def successful(self):
        return done[1]

'''

if __name__ == "__main__":
    pygame.init()
    test = Login().testing_start()

    print(
        test,
        "-----------test-------------",
        sep='\n'
    )
