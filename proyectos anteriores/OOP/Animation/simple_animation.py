# Animation class
import pygame
import time

class Simple_Animation:

    def __init__(self, window: pygame.Surface, position, path_list, frame_duration):
        self.lista_imagenes = []
        for path in path_list:
            # creo que esto estaría mejor con un with o un try...
            imagen = pygame.image.load(path)
            imagen = pygame.Surface.convert_alpha(imagen)  # optimiza la imagen dotando de canal alfa
            self.lista_imagenes.append(imagen)
        self.position = position
        self.window = window
        self.playing = False
        self.frame_duration = frame_duration
        self.num_frames = len(self.lista_imagenes)
        self.index = 0  # ahora la animación apunta al principio

    def play(self):
        # Si ya está en marcha la animación no hay que hacer nada...
        if self.playing:
            return True
        # Si queremos empezar la animación, pues ponemos en marcha el cronómtro e iniciamos por el primer frame...
        self.playing = True
        self.start_time = time.time()
        self.index = 0

    def update(self):
        # Si no está en marcha la animación no hay que actualizar nada
        if not self.playing:
            return
        # Si ha pasado el tiempo indicado, habrá que avanzar el frame...
        if time.time() - self.start_time >= self.frame_duration:
            # Avanzar el índice de la imagen a mostrar
            self.index += 1
            if self.index >= self.num_frames:
                self.index = 0
            # poner otra vez el tiempo actual
            self.start_time = time.time()

    def draw(self):
        self.window.blit(self.lista_imagenes[self.index], self.position)

