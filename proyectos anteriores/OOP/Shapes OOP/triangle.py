# Clase Triangle
import pygame
import pygame.locals
import random
from shape import Shape


class Triangle(Shape):
    def __init__(self, window: pygame.Surface):
        super().__init__(window, 'Triángulo')
        self.dx = random.randrange(10, 100)
        self.dy = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.dx, self.dy)
        self.pendiente = self.dy / self.dx

    def clicked_inside(self, position):
        # si no está en el rectángulo, pues nada...
        if not self.rect.collidepoint(position):
            return False
        # calculo la pendiente...
        dx = self.x + self.dx - position[0]
        dy = position[1] - self.y
        pendiente = dy / dx

        if pendiente <= self.pendiente:
            return True
        else:
            return False

    def get_area(self):
        return self.dx * self.dy / 2

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y), (self.x + self.dx, self.y), (self.x, self.y + self.dy)))




