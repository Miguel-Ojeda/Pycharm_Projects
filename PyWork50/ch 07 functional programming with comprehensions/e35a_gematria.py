"""
This exercise, the result of which you’ll use in the next one, asks that you create a
dict whose keys are the (lowercase) letters of the English alphabet, and whose values
are the numbers ranging from 1 to 26.

And yes, you could simply type {'a':1, 'b':2, 'c':3} and so forth,
but I’d like you to do this with a dict comprehension.
"""

import string


def gematria_dict_v0():
    return {letra: valor + 1
            for valor, letra in enumerate(string.ascii_lowercase)}


# Mejora después de leer Reuven!!!!!
def gematria_dict():
    return {letra: valor
            for valor, letra in enumerate(string.ascii_lowercase, 1)}


def dict_letters_values_v2():
    # Esta opción parece más enrevesada, es más natural la anterior
    inicio = ord('a')
    return {chr(numero): numero - inicio + 1
            for numero in range(inicio, inicio + 26)}


if __name__ == '__main__':

    resultado = gematria_dict()
    print(resultado)

    resultado_2 = dict_letters_values_v2()
    print(resultado_2)
