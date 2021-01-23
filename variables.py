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

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (196,140,232)
#text
introfont = pygame.font.Font('resources/fonts/GOTHICB.ttf', 25)
introtext = introfont.render('<=> Micro Space <=>', False, BLACK)

getusernametext = introfont.render('Please enter your name:', False, PURPLE)


buttonfont = pygame.font.Font('resources/fonts/GOTHICB.ttf', 14)
