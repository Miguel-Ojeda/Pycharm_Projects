# Clase Square
import pygame
import pygame.locals
import random
from shape import Shape


class Square(Shape):
    def __init__(self, window: pygame.Surface):
        super().__init__(window, 'Cuadrado')
        self.side = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    def clicked_inside(self, position):
        return self.rect.collidepoint(position)

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
