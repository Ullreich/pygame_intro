import pygame
import sys
from pygame.locals import *
import os

# print(sys.path)
# print(os.listdir())
os.chdir('/Users/nol975/python_projects/pygames/catgame')

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
catImg = pygame.image.load('cat.png')

catx = 10
caty = 10
direction = 'right'

# shit hamster
hamsterx = 370
hamstery = 30
hamster = pygame.draw.circle(DISPLAYSURF, GREEN, (hamsterx, hamstery), 30)
dirham = 'down'

while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    if dirham == 'right':
        hamsterx += 5
        if hamsterx == 370:
            dirham = 'down'
    elif dirham == 'down':
        hamstery += 5
        if hamstery == 270:
            dirham = 'left'
    elif dirham == 'left':
        hamsterx -= 5
        if hamsterx == 30:
            dirham = 'up'
    elif dirham == 'up':
        hamstery -= 5
        if hamstery == 30:
            dirham = 'right'

    pygame.draw.circle(DISPLAYSURF, GREEN, (hamsterx, hamstery), 30)
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)  # this locks the speed at a maximum of 30 fps, without it'll run at 60
