from deck import Deck
import pygame


# 3 iniciamos el entorno de pygame
pygame.init()
window = pygame.display.set_mode((600, 600))

mazo = Deck(window)

for carta1 in mazo.cards_list:
    print(carta1)
for carta2 in mazo.playing_list:
    print(carta2)

pygame.quit()
