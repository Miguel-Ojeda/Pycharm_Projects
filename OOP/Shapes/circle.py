# Clase Circle
import pygame
import pygame.locals
import random
import math
from colores import *
from auxiliar import distancia


class Circle:
    def __init__(self, window: pygame.Surface):
        self.window = window
        window_width = window.get_width()
        window_height = window.get_height()
        self.color = random.choice(COLORES)
        self.radio = random.randrange(10, 50)
        self.x = random.randrange(10, window_width - 2 * self.radio - 10)
        self.y = random.randrange(40, window_height - 2 * self.radio - 10)
        self.center_x = self.x + self.radio
        self.center_y = self.y + self.radio
        self.rect = pygame.Rect(self.x, self.y, 2 * self.radio, 2 * self.radio)
        self.forma = 'Círculo'

    def clicked_inside(self, position):
        if distancia((self.center_x, self.center_y), position) <= self.radio:
            return True
        else:
            return False

    def get_type(self):
        return self.forma

    def get_area(self):
        return math.pi * self.radio ** 2

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radio, 0)


