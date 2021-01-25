import pygame

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None

# initialization
pygame.font.init()

# image resources
titlelogo = pygame.image.load("resources/images/titlelogo.png")
startscreen = pygame.image.load("resources/images/startscreen.png")

# screen variables
X = 1000  # Screen width
Y = 800  # Screen height
screensize = (X,Y)
screenstartuppoint = (X/2-128,Y/2-128)
usernamepoint = (X/2-110,Y/2-100)
middlepoint = (X/2,Y/2)
##############################################################################################################



##############################################################################################################

# main menu buttons variables
buttonwidth = 200
buttonheight = 75
startposB1 = (X/2-buttonwidth/2,buttonheight)
startposB2 = (X/2-buttonwidth/2,buttonheight*2+37.5)
startposB3 = (X/2-buttonwidth/2,buttonheight*4)
wh = (buttonwidth,buttonheight)
textB1 = "PLAY"
textB2 = "HIGHSCORES"
textB3 = "EXIT"
buttonC = (235,131,131)
buttonH = (237,166,85)
buttonTC = (255,255,255)
buttonF = pygame.font.Font('resources/fonts/GOTHICB.ttf', 20)

##############################################################################################################

#game1 settings
FPS = 60
level = 0 # for difficulty over time
lives = 5 # how many aliens can get by you
playervel = 5 # speed of player movement
enemyvel = 1 # speed of enemy movement
trajectoryvel = 4 # speed of missiles & bombs movement
wavelength = 5 # how many enemy spawn at every round
multiplierval = 2 # duplicates score achieved
multipliertime = 30 # how many seconds for multiplier
#font
mainfont = pygame.font.Font('resources/fonts/GOTHIC.ttf', 25)
smallfont = pygame.font.Font('resources/fonts/GOTHIC.ttf', 20)
# window size
Xgame1 = 800
Ygame1 = 800
screensizegame1 = (Xgame1,Ygame1)
# images
alien = pygame.image.load("resources/images/game1/alien.png")
alien1 = pygame.image.load("resources/images/game1/alien1.png")
alien2 = pygame.image.load("resources/images/game1/alien2.png")
alien32 = pygame.image.load("resources/images/game1/alien32.png")
alien132 = pygame.image.load("resources/images/game1/alien132.png")
alien232 = pygame.image.load("resources/images/game1/alien232.png")
mainplayerimg = pygame.image.load("resources/images/game1/space-invaders.png")
missile = pygame.image.load("resources/images/game1/missile.png")
bomb = pygame.image.load("resources/images/game1/bomb.png")
armor = pygame.image.load("resources/images/game1/armor.png")
health = pygame.image.load("resources/images/game1/health.png")
nuke = pygame.image.load("resources/images/game1/nuclear-explosion.png")
auto = pygame.image.load("resources/images/game1/automatic-flash.png")
revive = pygame.image.load("resources/images/game1/revive.png")
multiplier = pygame.image.load("resources/images/game1/multiplier.png")
background = pygame.transform.scale(pygame.image.load("resources/images/game1/background-black.png"), screensizegame1)

##############################################################################################################
#questions setup
questionfont = pygame.font.Font('resources/fonts/GOTHIC.ttf', 22)
Xq = 800
Yq = 800
screensizeq = (Xq,Yq)
armor128 = pygame.image.load("resources/images/game1/armor128.png")
health128 = pygame.image.load("resources/images/game1/health128.png")
nuke128 = pygame.image.load("resources/images/game1/nuclear-explosion128.png")
auto128 = pygame.image.load("resources/images/game1/automatic-flash128.png")
revive128 = pygame.image.load("resources/images/game1/revive128.png")
multiplier128 = pygame.image.load("resources/images/game1/multiplier128.png")
blackbackground = pygame.transform.scale(pygame.image.load("resources/images/game1/black.jpg"), screensizeq)
simpleqtime = 15
hardqtime = 30

##############################################################################################################
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (196,140,232)
RED = (255, 0, 80)
GREEN = (0,255,0)
OCEANBLUE = (50,147,168)
#text
introfont = pygame.font.Font('resources/fonts/GOTHICB.ttf', 25)
introtext = introfont.render('<=> Micro Space <=>', True, BLACK)

getusernametext = introfont.render('Please enter your name:', True, PURPLE)
highscorestext = introfont.render("HIGHSCORES", True, PURPLE)


