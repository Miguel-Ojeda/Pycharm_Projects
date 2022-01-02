import pygame
import pygwidgets

# Clase Card

class Card:

    # Variables GLobales para la clase Card...
    BACK_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        """ Crea una carta dado:
         window (superficie para dibujar)
         rank: rango de la carta (ace, 2, 3, ... 10, jack, queen, king
         suite: el palo...
         value: el valor numérico, desde 1 hasta 13!!
         Las imágenes las buscaremos en 'images/rank of suit.png"""

        self.window = window
        # Posibles estados = 'back', 'front',
        self.cara_a_mostrar = 'back'
        self.rank = rank
        self.suit = suit
        self.value = value
        self.card_name = rank + ' of ' + suit
        file_name = 'images/' + self.card_name + '.png'
        # Colección de imágenes asociada a la carga...
        self.images = pygwidgets.ImageCollection(window,   # Ventana
                                                 (0, 0),   # Posición de la carta en la ventana al dibujarla!!
                                                 {'front': file_name, 'back': Card.BACK_IMAGE},  # diccionario imágenes
                                                 'back')  # imagen inicial seleccionada
        # En el diccionario de imágenes, cada imagen puede ser o un file_name o una imagen pygame
        # No entiendo la necesidad, podría prescindir del diccionario imagino, y coger la trasera y la delantera

    def conceal(self):
        self.cara_a_mostrar = 'back'
        self.images.replace('back')  # ¡hacemos que de la galería se selecciona la imagen trasera!!

    def reveal(self):
        self.cara_a_mostrar = 'front'
        self.images.replace('front')

    def flip(self):
        if self.cara_a_mostrar == 'back':
            self.reveal()
        else:
            self.conceal()

    def clicked(self, point):
        return self.images.rect.collidepoint(point)

    def get_name(self):
        return self.card_name

    def __str__(self):
        return self.card_name
    
    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def set_loc(self, loc):  # call the setLoc method of the pygwidgets.ImageCollection
        self.images.setLoc(loc)

    def get_loc(self):  # get the location from the ImageCollection
        loc = self.images.getLoc()
        return loc

    def draw(self):
        self.images.draw() # Invoca el método draw() de una pygwidgets.ImageCollection
