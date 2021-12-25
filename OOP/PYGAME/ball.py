import pygame.image
import random
class Ball:
    def __init__(self, window: pygame.Surface):
        # obtener datos de la ventana de dibujo..., máxima posición para dibujar...
        self.window = window
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.SIZE = 100
        self.max_width = self.window_width - self.SIZE
        self.max_height = self.window_height - self.SIZE

        # cargamos la imagen...
        self.image = pygame.image.load('images/ball.png')

        # Casi sería mejor crear un rectángulo de la imagen y obtenerlo de ahí...
        # Aquí lo haré....

        # Iniciamos posición aleatoria...
        # Y hallamos el rectángulo actual que define la posición de la bola
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.max_width)
        self.rect.y = random.randrange(self.max_height)

        # Velocidad y dirección inicial del movimiento...
        speeds_list = [-4, -3, -5, 3, 4, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]
        self.speed_x = random.choice(speeds_list)
        self.speed_y = random.choice(speeds_list)

    def move(self):
        if (self.rect.x < 0) or (self.rect.x >= self.max_width):
            self.speed_x *= -1  # reverse X direction
        if (self.rect.y < 0) or (self.rect.y >= self.max_height):
            self.speed_y *= -1  # reverse Y direction

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self):
        self.window.blit(self.image, self.rect)
