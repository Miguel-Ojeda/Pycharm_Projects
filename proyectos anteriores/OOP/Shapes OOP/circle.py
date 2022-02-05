# Clase Circle
import pygame
import pygame.locals
import random
import math
from auxiliar import distancia
from shape import Shape


class Circle(Shape):
    def __init__(self, window: pygame.Surface):
        super().__init__(window, 'Círculo')
        self.radio = random.randrange(10, 50)
        self.center_x = self.x + self.radio
        self.center_y = self.y + self.radio
        self.rect = pygame.Rect(self.x, self.y, 2 * self.radio, 2 * self.radio)

    def clicked_inside(self, position):
        if distancia((self.center_x, self.center_y), position) <= self.radio:
            return True
        else:
            return False

    def get_area(self):
        return math.pi * self.radio ** 2

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.center_x, self.center_y), self.radio, 0)


