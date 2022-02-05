# class Shape

import random
import pygame
from colores import *
from abc import ABC, abstractmethod

# La clase base la definiremos como abstracta...
class Shape(ABC):
    def __init__(self, window, forma):
        self.window = window
        window_width = window.get_width()
        window_height = window.get_height()
        self.color = random.choice(COLORES)
        self.x = random.randrange(10, window_width - 100)
        self.y = random.randrange(25, window_height - 100)
        self.forma = forma

    def get_type(self):
        return self.forma

    # Métodos abstractos que deben implementar las funciones derivadas...
    @abstractmethod
    def clicked_inside(self, position):
        # realmente esto no se ejecutaría nunca, da igual, sólo es descriptivo....
        raise NotImplementedError

    @abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

