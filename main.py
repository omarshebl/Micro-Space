import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from classes import Button
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
menuB1 = Button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB1, variables.wh, variables.textB1)
menuB2 = Button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB2, variables.wh, variables.textB2)
menuB3 = Button(variables.buttonC,variables.buttonH, variables.buttonTC, variables.startposB3, variables.wh, variables.textB3)

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
        gamescreen.blit(variables.introtext, (variables.X/2 - variables.introtext.get_width()/2,variables.Y/2 + 200))
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
    gamescreen.blit(variables.getusernametext,((variables.X / 2 - variables.getusernametext.get_width() / 2), (variables.Y / 2 - 50)))
    screenupdate()
    while not exitinguser:
        checkexiting()
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
                elif (not len(username) > 15) and event.unicode:
                    username += event.unicode
                gamescreen.fill(variables.BLACK)
                gamescreen.blit(variables.getusernametext, ((variables.X / 2 - variables.getusernametext.get_width() / 2), (variables.Y / 2 - 50)))
                usernametext = variables.introfont.render(username, True, variables.PURPLE)
                gamescreen.blit(usernametext, ((variables.X / 2 - usernametext.get_width() / 2), (variables.Y / 2)))
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
                    game1(gamescreen, username)
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
    game1(gamescreen, username)
