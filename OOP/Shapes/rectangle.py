# Clase Rectangle
import pygame
import pygame.locals
import random
from colores import *

# Se trata de una clase simplificada, para probar sobrecarga de operadores
# por eso tenemos pocas opciones para las dimensiones, etc
class Rectangle:
    def __init__(self, window: pygame.Surface):
        self.window = window
        window_width = window.get_width()
        window_height = window.get_height()

        self.width = random.choice((20, 30, 40))
        self.height = random.choice((20, 30, 40))
        self.color = random.choice(COLORES)
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.forma = 'Rectángulo'
        self.area = self.width * self.height

    def clicked_inside(self, position):
        return self.rect.collidepoint(position)

    def get_type(self):
        return self.forma

    def get_area(self):
        return self.area

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    # ejemplo de sobrecarga de operadores... (magic methods)
    # Igualdad: definiremos que dos rect. son iguales, si lo son sus áreas...
    def __eq__(self, rectangle_2):
        # Primero comprobaremos que el segundo objeto es también un rectángulo
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError('Second object not a rectangle!!')

        if self.area == rectangle_2.area:
            return True
        else:
            return False

    # Comparación < (less than)
    def __lt__(self, rectangle_2):
        # Primero comprobaremos que el segundo objeto es también un rectángulo
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError('Second object not a rectangle!!')

        if self.area < rectangle_2.area:
            return True
        else:
            return False

    # Comparación > (greater than)
    def __gt__(self, rectangle_2):
        # Primero comprobaremos que el segundo objeto es también un rectángulo
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError('Second object not a rectangle!!')

        if self.area > rectangle_2.area:
            return True
        else:
            return False
