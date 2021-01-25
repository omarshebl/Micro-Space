import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from variables import collide
from classes import Player
from classes import Enemy

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

lost = False
exiting = False
FPS = variables.FPS
level = variables.level
lives = variables.lives
playervelocity = variables.playervel
enemyvelocity = variables.enemyvel
trajectoryvelocity = variables.trajectoryvel
wavelength = variables.wavelength

player = Player(400, 600)
enemies = []

def checkexiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

def checkmovement():
    global player
    global playervelocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - playervelocity > 0:  # left
        player.x -= playervelocity
    if keys[pygame.K_RIGHT] and player.x + playervelocity + player.get_width() < variables.Xgame1:  # right
        player.x += playervelocity
    if keys[pygame.K_UP] and player.y - playervelocity > 0:  # up
        player.y -= playervelocity
    if keys[pygame.K_DOWN] and player.y + playervelocity + player.get_height() + 20 < variables.Ygame1:  # down
        player.y += playervelocity
    if keys[pygame.K_SPACE]:
        player.shoot()

def generalmovement():
    for enemym in enemies[:]:
        enemym.move(enemyvelocity)
        enemym.move_lasers(trajectoryvelocity, player)
        if random.randrange(0, 10 * FPS) == 1:
            enemym.shoot()
        if collide(enemym, player):
            player.health -= 10
            enemies.remove(enemym)
        if enemym.y + enemym.get_height() > variables.Ygame1:
            global lives
            lives -= 1
            enemies.remove(enemym)
    player.move_lasers(-trajectoryvelocity, enemies)

def newenemywave():
    if len(enemies) == 0:
        global level, wavelength
        level += 1
        wavelength += 1
        for i in range(wavelength):
            enemy = Enemy(random.randrange(50, variables.Xgame1 - 300), random.randrange(0, 250), random.randint(0, 2))
            enemies.append(enemy)

def checkloss():
    global lost, exiting
    if lives <= 0 or player.health <= 0:
        lost = True

def lostgame():
    global lost, exiting
    if lost:
        exiting = True
        pygame.time.delay(3000)

def redrawwindow(WIN, username):
    global player
    global enemies
    global lost
    WIN.fill(variables.BLACK)
    WIN.blit(variables.background, (0,0))
    username_label = variables.mainfont.render(username, 1, variables.WHITE) #TODO change coloring here and below
    levels_label = variables.mainfont.render(f"Level: {level}", 1, variables.WHITE)
    lives_label = variables.mainfont.render(f"Lives: {lives}", 1, variables.WHITE)
    WIN.blit(username_label, (810,20))
    WIN.blit(lives_label, (810,60))
    WIN.blit(levels_label, (810, 100))

    for enemyd in enemies:
        enemyd.draw(WIN)

    player.draw(WIN)

    if lost is True:
        lost_label = variables.mainfont.render("You Lost!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (variables.Xgame1 / 2 - lost_label.get_width() / 2, 400))

    pygame.display.update()

def game1(WIN, username):
    while not exiting:
        clock.tick(FPS)
        checkexiting()
        checkloss()
        redrawwindow(WIN, username)
        lostgame()
        newenemywave()
        checkmovement()
        generalmovement()







