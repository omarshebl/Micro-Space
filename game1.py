import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from variables import collide
from classes import Player
from classes import Enemy
from highscores import writescore

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

score = 0
alienkilled = 0
alienkilled1 = 0
alienkilled2 = 0
armorpwrup = True
healthpwrup = True
smrtmissilepwrup = True
nukepwrup = True
revivepwrup = True
autopwrup = False

player = Player(400, 600)
enemies = []

def checkexiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

def checkmovement():
    global player, playervelocity, armorpwrup, healthpwrup, smrtmissilepwrup, nukepwrup, revivepwrup, autopwrup, enemies, lives
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
    if keys[pygame.K_x]:
        if armorpwrup:
            player.set_armor(True)
        armorpwrup = False
    if keys[pygame.K_c]:
        if healthpwrup:
            player.health = 100
        healthpwrup = False
    if keys[pygame.K_v]:
        if smrtmissilepwrup:
            pass #TODO smrtmissilecode
        smrtmissilepwrup = False
    if keys[pygame.K_n]:
        if nukepwrup:
            enemies = []
        nukepwrup = False
    if keys[pygame.K_b]:
        if revivepwrup:
            lives = 5
        revivepwrup = False
    if keys[pygame.K_m]:
        if autopwrup:
            pass # TODO autocomplete question
        autopwrup = False

def generalmovement():
    global alienkilled, alienkilled1, alienkilled2
    for enemym in enemies[:]:
        enemym.move(enemyvelocity)
        enemym.move_lasers(trajectoryvelocity, player)
        if random.randrange(0, 10 * FPS) == 1:
            enemym.shoot()
        if collide(enemym, player):
            if player.get_armor():
                player.set_armor(False)
            else:
                player.health -= 10
            enemykilled(enemym, True)
        if enemym.y + enemym.get_height() > variables.Ygame1:
            global lives
            lives -= 1
            enemykilled(enemym)
    var = player.move_lasers(-trajectoryvelocity, enemies)
    if var is not None:
        if var == 0:
            alienkilled += 1
        elif var == 1:
            alienkilled1 += 1
        elif var == 2:
            alienkilled2 += 1

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

def lostgame(username):
    global lost, exiting
    if lost:
        writescore((username, score))
        exiting = True
        pygame.time.delay(3000)

def redrawinfo(WIN, username):
    username_label = variables.mainfont.render(username, 1, variables.WHITE)  # TODO change coloring here and below
    levelandlives_label = variables.smallfont.render(f"Level: {level} Lives: {lives}", 1, variables.WHITE)
    enemiesleft_label = variables.smallfont.render(f"Enemies left: {len(enemies)}", 1, variables.WHITE)
    WIN.blit(username_label, (900 - username_label.get_width() / 2, 20))
    WIN.blit(levelandlives_label, (900 - levelandlives_label.get_width()/2, 60))
    WIN.blit(enemiesleft_label, (900 - enemiesleft_label.get_width()/2, 100))

def redrawpwrups(WIN):
    if armorpwrup:
        variables.armor.set_alpha(255)
    else:
        variables.armor.set_alpha(80)
    if healthpwrup:
        variables.health.set_alpha(255)
    else:
        variables.health.set_alpha(80)
    if smrtmissilepwrup:
        variables.smrtmissile.set_alpha(255)
    else:
        variables.smrtmissile.set_alpha(80)
    if autopwrup:
        variables.auto.set_alpha(255)
    else:
        variables.auto.set_alpha(80)
    if revivepwrup:
        variables.revive.set_alpha(255)
    else:
        variables.revive.set_alpha(80)
    if nukepwrup:
        variables.nuke.set_alpha(255)
    else:
        variables.nuke.set_alpha(80)
    WIN.blit(variables.armor, ((800 + 200 / 3) - variables.armor.get_width() / 2 - 66.7 / 2, variables.Y - 150))
    WIN.blit(variables.health, ((800 + 400 / 3) - variables.health.get_width() / 2 - 66.7 / 2, variables.Y - 150))
    WIN.blit(variables.smrtmissile, ((800 + 600 / 3) - variables.smrtmissile.get_width() / 2 - 70 / 2, variables.Y - 150))
    WIN.blit(variables.nuke, ((800 + 200 / 3) - variables.nuke.get_width() / 2 - 66.7 / 2, variables.Y - 200))
    WIN.blit(variables.revive, ((800 + 400 / 3) - variables.revive.get_width() / 2 - 66.7 / 2, variables.Y - 200))
    WIN.blit(variables.auto,((800 + 600 / 3) - variables.auto.get_width() / 2 - 70 / 2, variables.Y - 200))

def redrawkilled(WIN):
    alienkilled_text = variables.smallfont.render(f"{alienkilled}", 1, variables.WHITE)
    alienkilled_text1 = variables.smallfont.render(f"{alienkilled1}", 1, variables.WHITE)
    alienkilled_text2 = variables.smallfont.render(f"{alienkilled2}", 1, variables.WHITE)
    WIN.blit(variables.alien32, ((800 + 200 / 3) - variables.alien32.get_width() / 2 - 66.7 / 2, variables.Y - 70))
    WIN.blit(variables.alien132, ((800 + 400 / 3) - variables.alien32.get_width() / 2 - 66.7 / 2, variables.Y - 70))
    WIN.blit(variables.alien232, ((800 + 600 / 3) - variables.alien32.get_width() / 2 - 70 / 2, variables.Y - 70))
    WIN.blit(alienkilled_text, ((800 + 200 / 3) - alienkilled_text.get_width() / 2 - 66.7 / 2, variables.Y - 40))
    WIN.blit(alienkilled_text1, ((800 + 400 / 3) - alienkilled_text1.get_width() / 2 - 66.7 / 2, variables.Y - 40))
    WIN.blit(alienkilled_text2, ((800 + 600 / 3) - alienkilled_text2.get_width() / 2 - 70 / 2, variables.Y - 40))

def redrawsidebar(WIN, username):
    redrawinfo(WIN,username)
    redrawpwrups(WIN)
    redrawkilled(WIN)

def enemykilled(enemy, add=False):
    global alienkilled, alienkilled1, alienkilled2
    if not add:
        enemies.remove(enemy)
    else:
        var = enemy.get_var()
        if var == 0:
            alienkilled += 1
        elif var == 1:
            alienkilled1 += 1
        elif var == 2:
            alienkilled2 += 1
        enemies.remove(enemy)

def redrawgame(WIN, username):
    global player
    global enemies
    global lost
    WIN.fill(variables.BLACK)
    WIN.blit(variables.background, (0, 0))
    redrawsidebar(WIN, username)
    player.draw(WIN)
    for enemyd in enemies:
        enemyd.draw(WIN)
    if lost is True:
        lost_label = variables.mainfont.render("You Lost!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (variables.Xgame1 / 2 - lost_label.get_width() / 2, 400))
    pygame.display.update()

def game1(WIN, username):
    while not exiting:
        clock.tick(FPS)
        checkexiting()
        checkloss()
        redrawgame(WIN, username)
        lostgame(username)
        newenemywave()
        checkmovement()
        generalmovement()







