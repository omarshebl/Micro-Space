import pygame
import time
import variables # game variables file "variables.py"

# exit variable
exiting = False
startup = True

# initiation
pygame.init()
pygame.font.init()

# window creation
gamescreen = pygame.display.set_mode(variables.screensize)

# icon & title set
pygame.display.set_caption("Micro Space")
pygame.display.set_icon(variables.titlelogo)

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
        screenupdate()
        startup = False

def screenupdate():
    pygame.display.flip()



def mainmenu():
    global exiting
    while not exiting:
        checkexiting()


# main loop
while not exiting:
    checkexiting()
    screenstartup()
    mainmenu()

