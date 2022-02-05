# 1 import
import pygame
import sys
from pygame.locals import *
import pygwidgets
from rectangle import *

# 2 Set up the constants
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Set up the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectangle_list = []
for i in range(0, N_RECTANGLES):
    rectangulo = Rectangle(window)
    rectangle_list.append(rectangulo)

which_rectangle = FIRST_RECTANGLE

# 6 Main loop
while True:
    # 7 eventos...
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for rectangulo in rectangle_list:
                if rectangulo.clicked_inside(event.pos):
                    print('Clicked on', which_rectangle, 'rectangle.')

                    # Acabamos de elegir el primer rectángulo...
                    if which_rectangle == FIRST_RECTANGLE:
                        first_rectangle = rectangulo
                        which_rectangle = SECOND_RECTANGLE

                    # Ya tenemos el segundo rectángulo... a compararlos...
                    elif which_rectangle == SECOND_RECTANGLE:
                        second_rectangle = rectangulo

                        if first_rectangle == second_rectangle:
                            print('Tienen la misma área')
                        elif first_rectangle < second_rectangle:
                            print('El primero tiene menos área')
                        else:
                            print('El primero tiene mayor área')
                        which_rectangle = FIRST_RECTANGLE


    # Tell each shape to draw itself
    window.fill(WHITE)
    for rectangulo in rectangle_list:
        rectangulo.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)