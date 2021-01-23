import pygame

# initialization
pygame.font.init()

# image resources
titlelogo = pygame.image.load("resources/images/titlelogo.png")
startscreen = pygame.image.load("resources/images/startscreen.png")

# screen variables
X = 800  # Screen width
Y = 600  # Screen height
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


# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (196,140,232)
#text
introfont = pygame.font.Font('resources/fonts/GOTHICB.ttf', 25)
introtext = introfont.render('<=> Micro Space <=>', False, BLACK)

getusernametext = introfont.render('Please enter your name:', False, PURPLE)


