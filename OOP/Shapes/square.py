# Clase Square
import pygame
import pygame.locals
import random
from colores import *


class Square:
    def __init__(self, window: pygame.Surface):
        self.window = window
        window_width = window.get_width()
        window_height = window.get_height()
        self.side = random.randrange(10, 100)
        self.color = random.choice(COLORES)
        self.x = random.randrange(10, window_width - self.side - 10)
        self.y = random.randrange(40, window_height - self.side - 10)
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.forma = 'Cuadrado'

    def clicked_inside(self, position):
        return self.rect.collidepoint(position)

    def get_type(self):
        return self.forma

    def get_area(self):
        return self.side ** 2

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    # ejemplo de sobrecarga de operadores... (magic methods)
    def __eq__(self, other_square):
        # primero comprobamos que ambos objetos son cuadrados... (bueno, el segundo realmente)
        if not isinstance(other_square, Square):
            raise TypeError('Second object not a square!!')

        if self.side == other_square.side:
            return True
        else:
            return False
