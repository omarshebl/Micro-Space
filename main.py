import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from classes import button
from game1 import game1

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

#set main menu buttons
menuB1 = button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB1, variables.wh, variables.textB1)
menuB2 = button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB2, variables.wh, variables.textB2)
menuB3 = button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB3, variables.wh, variables.textB3)

def checkexiting():
    global exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exiting = True
            return True
    return False

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
                screenupdate(variables.BLACK)
                gamescreen.blit(variables.getusernametext, variables.screenstartuppoint)
                usernametext = variables.introfont.render(username, True, variables.PURPLE)
                gamescreen.blit(usernametext, variables.usernamepoint)
                screenupdate()

screenupdate(variables.BLACK)

def drawbuttons():
    menuB1.draw(gamescreen, variables.WHITE)
    menuB2.draw(gamescreen, variables.WHITE)
    menuB3.draw(gamescreen, variables.WHITE)
    screenupdate()

def mainmenu():
    global exiting
    while not exiting:
        checkexiting()
        drawbuttons()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            menuB1.isOver(pos)
            menuB2.isOver(pos)
            menuB3.isOver(pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuB1.isOver(pos):
                    pass #TODO play games
                if menuB2.isOver(pos):
                    pass #TODO show high scores
                if menuB3.isOver(pos):
                    exiting = True
                    pygame.quit()

# ---------------------- main loop -----------------------
while not exiting:
    checkexiting()
    #screenstartup()
    #getusername()
    #mainmenu()
    game1(gamescreen,username)