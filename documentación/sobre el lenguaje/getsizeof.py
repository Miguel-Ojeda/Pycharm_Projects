# Esta función nos da lo que ocupa un objeto... (no suma lo que ocupa los objetos que tienen dentro!!!)

# Veamos lo que ocupan las listas según su tamaño
# Python Workouts 50 .... pg. 36

import sys

lista = []

for i in range(25):
    print(f'Lista de longitud {len(lista)} ocupa {sys.getsizeof(lista)} bytes')
    lista.append(i)

