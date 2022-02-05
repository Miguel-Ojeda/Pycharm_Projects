# Rectangle class
import pygame
from shape import Shape
import random


class Rectangle(Shape):
    def __init__(self, window):
        super().__init__(window, 'Rectangle')
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clicked_inside(self, position):
        return self.rect.collidepoint(position)

    def get_area(self):
        return self.width * self.height

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, 0)
