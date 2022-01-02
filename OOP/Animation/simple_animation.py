# Animation class
import pygame
import time

class Simple_Animation:

    def __init__(self, window, position, path_list, frame_duration):
        self.lista_imagenes = []
        for path in path_list:
            # creo que esto estaría mejor con un with o un try...
            imagen = pygame.image.load(path)
            imagen = pygame.Surface.convert_alpha(imagen)  # optimiza la imagen dotando de canal alfa
            lista_imagenes.append(imagen)

        self.playing = False
        self.frame_duration = frame_duration
        self.n_images = len(self.lista_imagenes

