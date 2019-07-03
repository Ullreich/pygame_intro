import sys
import pygame
from pygame.locals import *
import os
import time

os.chdir('/Users/nol975/python_projects/pygames/fontfuckaround')
print(os.listdir())

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('shitty font stuff')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (240, 233, 24)

# print(pygame.font.get_fonts())

# sysfont would use the relative path but it doesn't work
# this seems to be a bug in macos high sierra
fontObj = pygame.font.Font('starjedi.ttf', 32)
textSurfaceObj = fontObj.render('SANS UNDERTALE', True, yellow)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

soundObj = pygame.mixer.Sound('test.wav')

# main loop
playvar = 1
while True:
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    if playvar == 1:
        soundObj.play()
        playvar = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
