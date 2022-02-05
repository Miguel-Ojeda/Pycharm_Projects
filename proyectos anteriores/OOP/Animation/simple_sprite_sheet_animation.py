# Aquí pasamos una sola imagen, formada por multitud de imágenes pequeñitas, todas en el mismo fichero
# Veamos como animar con una clase un fichero de este tipo...
# La clase es igual, lo único que al iniciar tenemos que subdividir la imagen grande en muchas pequeñitas!!!

import pygame
import time

class Simple_Sprite_Sheet_Animation:

    def __init__(self, window: pygame.Surface, position, simple_sheet_sprite_path,
                 n_images, width_subimage, height_subimage, frame_duration):
        self.position = position
        self.window = window
        self.playing = False
        self.frame_duration = frame_duration
        self.num_frames = n_images
        self.index = 0  # ahora la animación apunta al principio
        self.lista_imagenes = []

        imagen_compuesta = pygame.image.load(simple_sheet_sprite_path)
        # Convierte para optimizarlo a dibujo a pantalla!!!
        imagen_compuesta = pygame.Surface.convert_alpha(imagen_compuesta)
        # imagen = imagen.convert_alpha(imagen)
        imagen_compuesta_height = imagen_compuesta.get_height()
        imagen_compuesta_width = imagen_compuesta.get_width()
        n_rows = imagen_compuesta_height // height_subimage
        n_cols = imagen_compuesta_width // width_subimage
        for row in range(n_rows):
            for col in range(n_cols):
                rectangle = pygame.Rect(col * width_subimage, row * height_subimage, width_subimage, height_subimage)
                imagen = imagen_compuesta.subsurface(rectangle)
                self.lista_imagenes.append(imagen)

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
