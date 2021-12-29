import pygame
from pygame.locals import *

class SimpleText:
    def __init__(self, window, location, texto, color):
        # Iniciamos el sistema de fuentes de pygame; observar que aunque creemos muchos objetos,
        # realmente la llamada sólo inicializa la primera vez, las demás pues no hace nada
        # porque ya el sistema está en marcha...
        # quizás se podría mejorar poniéndolo fuera???
        # Pero como es una clase tiene que asegurarse... el código tiene que estar OK en sí mismo
        self.text_surface = None
        pygame.font.init()
        self.window = window
        self.location = location
        self.font = pygame.font.SysFont(None, 30)  # utilizamos la fuente estándar del sistema!!!
        self.color = color
        self.text = "Prueba"   # lo crearemos luego en setvalue...
        self.set_text(texto)

    def set_text(self, texto):
        # No sólo asigna el valor, sino que crea el objeto tipo superficie...!!!
        # nada que hacer.... ya que el texto, y la superficie, ya están creados!!!
        if self.text == texto:
            return

        self.text = texto
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.window.blit(self.text_surface, self.location)
