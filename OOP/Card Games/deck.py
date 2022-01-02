# Deck class... es un objeto manejador de objetos (object manager object)
# En este caso administra cartas, su labor es crear y administrar el mazo!!!
import random
from card import Card


class Deck():
    # Variables globales a la clase... compartidas por todas las instancias
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    # This dict maps each card rank to a value for a standard deck
    STANDARD_VALUES = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                     '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self, window, rank_values=STANDARD_VALUES):
        """ La función inicar el mazo admite como parámetro opcional el diccionario de rangos y valores"""
        self.sorted_deck = []  # va a ser la lista con la baraja ordenada
        self.shuffled_deck = []  # va a ser la lista con la baraja mezclada ya...
        # creamos todas las cartas!!
        # depende de los palos y los valores... en principio, como está, es la americana
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rank_values.items():
                carta = Card(window, rank, suit, value)
                self.sorted_deck.append(carta)

        # Y para terminar... barajamos... para crear otra copia de la baraja, pero mezclada ya!!!
        self.shuffle()

    def shuffle(self):
        # Creamos una copia de la baraja original, que luego desordenaremos
        self.shuffled_deck = self.sorted_deck.copy()
        # no podemos hacer self.playing_list = self.cards_list pq entonces sería un objeto, con 2 referencias!!!
        for carta in self.shuffled_deck:
            carta.conceal()  # creo que no es necesario, pero por si acaso...
        random.shuffle(self.shuffled_deck)

    def get_card(self):
        if len(self.shuffled_deck) == 0:
            raise IndexError('No more cards')
        carta = self.shuffled_deck.pop()
        return carta

