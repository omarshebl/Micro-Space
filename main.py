import pygame
import time
import variables # game variables file "variables.py"


username = "omar"

# exit variable
exiting = False

# startup variable
startup = True

# initiation
pygame.init()
pygame.font.init()

# window creation
gamescreen = pygame.display.set_mode(variables.screensize)

# icon & caption set
pygame.display.set_caption("Micro Space")
pygame.display.set_icon(variables.titlelogo)

class button:
    def __init__(self, color, highcolor, x, y, width, height, text=''):
        self.highcolor = highcolor
        self.ocolor = color
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = variables.buttonfont
            text = font.render(self.text, True, (0, 0, 0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if (pos[0] > self.x) and (pos[0] < (self.x + self.width)) and (pos[1] > self.y) and (pos[1] < (self.y + self.height)):
            self.color = self.highcolor
            return True
        self.color = self.ocolor
        return False

def checkexiting():
    global exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exiting = True

def screenstartup():
    global startup
    if startup:
        gamescreen.fill(variables.WHITE)
        gamescreen.blit(variables.introtext, (270,448))
        for x in range(0,100):
            variables.startscreen.set_alpha(x)
            gamescreen.blit(variables.startscreen, variables.screenstartuppoint)
            screenupdate()
            time.sleep(0.05)
        time.sleep(1)
        gamescreen.fill(variables.WHITE)
        screenupdate(variables.BLACK)
        startup = False

def screenupdate(color=None):
    if color:
        gamescreen.fill(color)
    pygame.display.flip()

def getusername():
    global username
    screenupdate(variables.BLACK)
    exitinguser = False
    startup = True
    while not exitinguser:
        checkexiting()
        if startup:
            screenupdate(variables.BLACK)
            gamescreen.blit(variables.getusernametext, variables.screenstartuppoint)
            screenupdate()
            startup=False
        for event in pygame.event.get():
            screenupdate(variables.BLACK)
            gamescreen.blit(variables.getusernametext, variables.screenstartuppoint)
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    if len(username)>0:
                        username = username[:-1]
                elif event.key==pygame.K_RETURN:
                    exitinguser = True
                elif event.key==pygame.K_ESCAPE:
                    exitinguser = True
                    username=""
                    global exiting
                    exiting = True
                    break
                elif event.key:
                    if (not len(username) > 15) and event.unicode :
                        username += event.unicode
            usernametext = variables.introfont.render(username, False, variables.PURPLE)
            gamescreen.blit(usernametext, variables.usernamepoint)
            screenupdate()

    screenupdate(variables.BLACK)

def mainmenu():
    global exiting
    while not exiting:
        checkexiting()

# ---------------------- main loop -----------------------
while not exiting:
    checkexiting()
    #screenstartup()
    #getusername()
    mainmenu()