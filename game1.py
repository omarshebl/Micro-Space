import pygame
import time
import os
import random
import variables # game variables file "variables.py"
from variables import collide
from classes import Player
from classes import Enemy
from highscores import writescore
from questions import askquestion

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


pwrups = ["armor", "health", "smrtmissile", "nuke", "revive", "auto", "multiplier"]

lost = False
pausegame = False
exiting = False
FPS = variables.FPS
level = variables.level
lives = variables.lives
playervelocity = variables.playervel
enemyvelocity = variables.enemyvel
trajectoryvelocity = variables.trajectoryvel
wavelength = variables.wavelength
multiplier = variables.multiplierval
multipliertime = variables.multipliertime


simplea = 0
simplef = 0
harda = 0
hardf = 0
score = 0
alienkilled = 0
alienkilled1 = 0
alienkilled2 = 0
armorpwrup = False
healthpwrup = False
smrtmissilepwrup = False
nukepwrup = False
revivepwrup = False
autopwrup = False
useauto = False
usemultiplier = False
multitimer = 0
multiply = False
question = False
questionType = 0
keys = []


player = Player(400, 600)
enemies = []

def setpwrup(state, which):
    global armorpwrup, healthpwrup, smrtmissilepwrup, nukepwrup, revivepwrup, autopwrup, usemultiplier
    if state:
        if which == "nuke":
            nukepwrup = True
        if which == "revive":
            revivepwrup = True
        if which == "armor":
            armorpwrup = True
        if which == "health":
            healthpwrup = True
        if which == "auto":
            autopwrup = True
        if which == "smrtmissile":
            smrtmissilepwrup = True
        if which == "multiplier":
            usemultiplier = True

def checkexiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

def checkmultipwrup():
    global multitimer, usemultiplier, multiply
    if usemultiplier:
        multitimer = pygame.time.get_ticks()
        usemultiplier = False
    seconds = (pygame.time.get_ticks()-multitimer)/1000
    if seconds > multipliertime:
        multiply = False
        multitimer = 0
    else:
        multiply = True

def questionanswer(WIN):
    global question, questionType, useauto, simplea, simplef, harda, hardf
    rando = 6
    if questionType != 1:
        rando = random.randint(0,5)
    randompwrup = pwrups[rando]
    question = askquestion(WIN, questionType, multiplier, useauto, randompwrup)
    setpwrup(question, randompwrup)
    if questionType == 1:
        if question:
            simplea +=1
        else:
            simplef +=1
    else:
        if question:
            harda +=1
        else:
            hardf +=1
    question = False
    questionType = 0
    useauto = False

def checkquestion(WIN):
    if question:
        questionanswer(WIN)

def togglepause():
    global pausegame
    if pausegame is True:
        pausegame = False
    else:
        pausegame = True

def checkpause():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                togglepause()
                return

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    togglepause()
                    return

def checkmovement():
    global player, playervelocity, armorpwrup, healthpwrup, smrtmissilepwrup, nukepwrup, revivepwrup, autopwrup, enemies, lives, useauto
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
            useauto = True
        autopwrup = False

def generalmovement():
    global alienkilled, alienkilled1, alienkilled2, question, questionType, score
    for enemym in enemies[:]:
        enemym.move(enemyvelocity)
        enemym.move_projectiles(trajectoryvelocity, player)
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

    [var, questionType] = player.move_projectiles(-trajectoryvelocity, enemies)

    if (var is not None) and (questionType is not None):
        if multiply:
            score += 10*multiplier
        else:
            score += 10

    if questionType is None:
        questionType = 0
    if questionType != 0:
        question = True
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
            randomX = random.randrange(50, variables.Xgame1 - 300)
            randomY = random.randrange(0, 250)
            randomType = random.randint(0, 2)
            randomQues = 0
            if random.randrange(0, 4) == 1:
                randomQues = 1
            elif random.randrange(0, 20) == 1:
                randomQues = 2
            enemy = Enemy(randomX, randomY, randomType, randomQues)
            enemies.append(enemy)

def enemykilled(enemy, add=False):
    global alienkilled, alienkilled1, alienkilled2, questionType, question
    if not add:
        enemies.remove(enemy)
    else:
        var = enemy.get_var()
        questionType = enemy.get_ques()
        if questionType != 0:
            question = True
        if var == 0:
            alienkilled += 1
        elif var == 1:
            alienkilled1 += 1
        elif var == 2:
            alienkilled2 += 1
        enemies.remove(enemy)

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
    username_label = variables.mainfont.render(username, 1, variables.WHITE)
    levelandlives_label = variables.smallfont.render(f"Level: {level} Lives: {lives}", 1, variables.WHITE)
    enemiesleft_label = variables.smallfont.render(f"Enemies left: {len(enemies)}", 1, variables.RED)
    score_label = variables.smallfont.render(f"Score: {score}", 1, variables.PURPLE)
    WIN.blit(username_label, (900 - username_label.get_width() / 2, 20))
    WIN.blit(levelandlives_label, (900 - levelandlives_label.get_width()/2, 60))
    WIN.blit(enemiesleft_label, (900 - enemiesleft_label.get_width()/2, 100))
    WIN.blit(score_label, (900 - score_label.get_width()/2, 140))

def redrawanswerinfstats(WIN):
    simplea_label = variables.smallfont.render(f"{simplea}", 1, variables.GREEN)
    simplef_label = variables.smallfont.render(f"{simplef}", 1, variables.RED)
    harda_label = variables.smallfont.render(f"{harda}", 1, variables.GREEN)
    hardf_label = variables.smallfont.render(f"{hardf}", 1, variables.RED)
    pygame.draw.circle(WIN, variables.RED, ((800 + 200 / 3), variables.Y - 500), 10)
    WIN.blit(simplea_label, (800 + 200 / 3 - simplea_label.get_width() / 2, variables.Y - 490))
    WIN.blit(simplef_label, (800 + 200 / 3 - simplef_label.get_width() / 2, variables.Y - 470))
    pygame.draw.circle(WIN, variables.OCEANBLUE, ((800 + 400 / 3), variables.Y - 500), 10)
    WIN.blit(harda_label, (800 + 400 / 3 - harda_label.get_width() / 2, variables.Y - 490))
    WIN.blit(hardf_label, (800 + 400 / 3 - hardf_label.get_width() / 2, variables.Y - 470))

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
    if multitimer != 0:
        variables.multiplier.set_alpha(255)
    else:
        variables.multiplier.set_alpha(80)
    WIN.blit(variables.armor, ((800 + 200 / 3) - variables.armor.get_width() / 2 - 66.7 / 2, variables.Y - 150))
    WIN.blit(variables.health, ((800 + 400 / 3) - variables.health.get_width() / 2 - 66.7 / 2, variables.Y - 150))
    WIN.blit(variables.smrtmissile, ((800 + 600 / 3) - variables.smrtmissile.get_width() / 2 - 70 / 2, variables.Y - 150))
    WIN.blit(variables.nuke, ((800 + 200 / 3) - variables.nuke.get_width() / 2 - 66.7 / 2, variables.Y - 200))
    WIN.blit(variables.revive, ((800 + 400 / 3) - variables.revive.get_width() / 2 - 66.7 / 2, variables.Y - 200))
    WIN.blit(variables.auto,((800 + 600 / 3) - variables.auto.get_width() / 2 - 70 / 2, variables.Y - 200))
    WIN.blit(variables.multiplier, ((800 + 400 / 3) - variables.multiplier.get_width() / 2 - 66.7 / 2, variables.Y - 250))

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
    redrawanswerinfstats(WIN)
    redrawpwrups(WIN)
    redrawkilled(WIN)

def redrawgame(WIN, username):
    global player, lost, enemies, pausegame
    WIN.fill(variables.BLACK)
    WIN.blit(variables.background, (0, 0))

    redrawsidebar(WIN, username)
    player.draw(WIN)
    for enemyd in enemies:
        enemyd.draw(WIN)
    if lost is True:
        lost_label = variables.mainfont.render("You Lost!!", 1, (255, 255, 255))
        WIN.blit(lost_label, (variables.Xgame1 / 2 - lost_label.get_width() / 2, 400))
    if pausegame is True:
        pause_label = variables.mainfont.render("Game Paused!", 1, (255, 255, 255))
        WIN.blit(pause_label, (variables.Xgame1 / 2 - pause_label.get_width() / 2, 400))


    pygame.display.update()

def game1(WIN, username):
    global pausegame
    while not exiting:
        clock.tick(FPS)
        checkpause()
        checkexiting()
        if pausegame:
            redrawgame(WIN, username)
            wait()
        else:
            checkloss()
            redrawgame(WIN, username)
            lostgame(username)
            newenemywave()
            checkmovement()
            generalmovement()
            checkquestion(WIN)
            checkmultipwrup()








