import sys
from pygame.locals import *
import pygame


a = pygame.init()  # this initializes all the shit from pygame. don't ask me why it has to be initalized manually

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('shitty shapes')

# set color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# draw some nice shapes
DISPLAYSURF.fill(white)
pygame.draw.polygon(DISPLAYSURF, green, ((10, 10), (100, 10), (10, 100)))
pygame.draw.line(DISPLAYSURF, blue, (100, 10), (100, 100), 10)
pygame.draw.circle(DISPLAYSURF, red, (100, 150), 20)
pygame.draw.rect(DISPLAYSURF, black, (100, 100, 30, 20), 1)
ellipse = pygame.draw.ellipse(DISPLAYSURF, green, (150, 150, 30, 20), 1)

# set indidividual pixels and lock the screen i.e. no new images can be drawn
pixobj = pygame.PixelArray(DISPLAYSURF)
pixobj[120][120] = green,
pixobj[121][121] = green,
pixobj[122][122] = green,
del pixobj  # now we can draw again

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
