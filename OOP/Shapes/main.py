# 1 import
import pygame
import sys
from pygame.locals import *
import pygwidgets

from square import *
from circle import *
from triangle import *
from rectangle import *

# 2 Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 25


# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapesList = []
formas_conocidas = (Square, Circle, Triangle, Rectangle)

for i in range(0, N_SHAPES):
    forma_seleccionada = random.choice(formas_conocidas)
    shape = forma_seleccionada(window)
    shapesList.append(shape)
    status_line = pygwidgets.DisplayText(window, (4, 4), 'Click on shapes', fontSize=28)

# 6 Main loop
while True:
    # 7 eventos...
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:

            # Reverse order to check last drawn shape first
            # for shape in reversed(shapesList):
            clic = False
            for shape in reversed(shapesList):
                if shape.clicked_inside(event.pos):
                    clic = True
                    area = shape.get_area()
                    area = str(area)
                    forma = shape.get_type()
                    # newText = 'Clicked on a ' + forma + ' whose area is ' + area)
                    newText = 'Clicked on a ' + forma + ' whose area is ' + area
                    status_line.setValue(newText)
                    break  # only deal with topmost shape
            if clic == False:
                newText = 'No haz clicado en ninguna forma'
                status_line.setValue(newText)

    # Tell each shape to draw itself
    window.fill(WHITE)
    for oShape in shapesList:
        oShape.draw()
    status_line.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)