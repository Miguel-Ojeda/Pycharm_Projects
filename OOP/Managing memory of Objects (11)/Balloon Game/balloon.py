from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
import pygwidgets
from constants import *
import random

# Definimos la clase abstracta Balloon
class Balloon(ABC):
    popsound_loaded = False
    popsound = None
    @abstractmethod
    def __init__(self, window, max_width, max_height, ID, image, size, n_points, speed_y):
        # Variables GLOBALES de la clase, compartidas por todos las instancias!!!
        self.window = window
        self.ID = ID
        self.balloon_image = image
        self.size = size
        self.n_points = n_points
        self.speed_y = speed_y

        if not Balloon.popsound_loaded:  # load first time only
            Balloon.popsound_loaded = True
            Balloon.popsound = pygame.mixer.Sound('sounds/balloonPop.wav')

        self.rect = self.balloon_image.getRect()

        # Position so balloon is within the width of the window,
        # but below the bottom
        self.x = random.randrange(max_width - self.rect.width)
        self.y = max_height + random.randrange(75)  # para que quede por debajo, y no se vea todavía....
        # self.balloon_image.setLoc((self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

    def clicked_inside(self, mousePoint):
        if self.rect.collidepoint(mousePoint):
            Balloon.popsound.play()
            # True here means it was hit
            return True, self.n_points
        else:
            return False, 0  # not hit, no points

    def update(self):
        # update y position by speed
        self.y = self.y - self.speed_y
        self.rect.y = self.y

        # self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.rect.height:  # off the top of the window
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING


    def draw(self):
        self.balloon_image.draw()

    def __del__(self):
        print(self.size, 'Balloon', self.ID, 'is going away')

class Balloon_Small(Balloon):
    balloon_image = pygame.image.load('images/redBalloonSmall.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        imagen = pygwidgets.Image(window, (0, 0), Balloon_Small.balloon_image)
        super().__init__(window, maxWidth, maxHeight, ID, imagen, 'Small', 30, 3.1)

class Balloon_Medium(Balloon):
    balloon_image = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        imagen = pygwidgets.Image(window, (0, 0), Balloon_Medium.balloon_image)
        super().__init__(window, maxWidth, maxHeight, ID, imagen, 'Medium', 20, 2.2)

class Balloon_Large(Balloon):
    balloon_image = pygame.image.load('images/redBalloonLarge.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        imagen = pygwidgets.Image(window, (0, 0), Balloon_Large.balloon_image)
        super().__init__(window, maxWidth, maxHeight, ID, imagen, 'Medium', 10, 1.5)