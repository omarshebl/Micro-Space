import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from classes import Player

pygame.init()
pygame.font.init()




def checkexiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

def game1(WIN, username):
    exiting = False
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 5
    playervelocity = 5

    player = Player(300,300)

    def redrawwindow():
        WIN.blit(variables.background, (0,0))
        username_label = variables.mainfont.render(username, 1, variables.WHITE) #TODO change coloring here and below
        levels_label = variables.mainfont.render(f"Level: {level}", 1, variables.WHITE)
        lives_label = variables.mainfont.render(f"Lives: {lives}", 1, variables.WHITE)
        player.draw(WIN)
        WIN.blit(username_label, (810,20))
        WIN.blit(lives_label, (810,60))
        WIN.blit(levels_label, (810, 100))
        pygame.display.update()

    while not exiting:
        clock.tick(FPS)
        redrawwindow()
        exiting = checkexiting()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - playervelocity > 0:  # left
            player.x -= playervelocity
        if keys[pygame.K_RIGHT] and player.x + playervelocity + player.get_width() < variables.Xgame1:  # right
            player.x += playervelocity
        if keys[pygame.K_UP] and player.y - playervelocity > 0:  # up
            player.y -= playervelocity
        if keys[pygame.K_DOWN] and player.y + playervelocity + player.get_height() + 15 < variables.Ygame1:  # down
            player.y += playervelocity