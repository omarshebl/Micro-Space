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



#game1 settings
mainfont = pygame.font.Font('resources/fonts/GOTHIC.ttf', 25)
Xgame1 = 800
Ygame1 = 800
screensizegame1 = (Xgame1,Ygame1)
RED_SPACE_SHIP = pygame.image.load("resources/images/game1/pixel_ship_red_small.png")
GREEN_SPACE_SHIP = pygame.image.load("resources/images/game1/pixel_ship_green_small.png")
BLUE_SPACE_SHIP = pygame.image.load("resources/images/game1/pixel_ship_blue_small.png")
YELLOW_SPACE_SHIP = pygame.image.load("resources/images/game1/pixel_ship_yellow.png")
RED_LASER = pygame.image.load("resources/images/game1/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("resources/images/game1/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("resources/images/game1/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("resources/images/game1/pixel_laser_yellow.png")
BG = pygame.transform.scale(pygame.image.load("resources/images/game1/background-black.png"), screensizegame1)


# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (196,140,232)
#text
introfont = pygame.font.Font('resources/fonts/GOTHICB.ttf', 25)
introtext = introfont.render('<=> Micro Space <=>', True, BLACK)

getusernametext = introfont.render('Please enter your name:', True, PURPLE)


