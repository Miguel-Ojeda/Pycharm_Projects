# Write a function, most_repeating_word, that takes a sequence of strings as input. The
# function should return the string that contains the greatest number of repeated letters. In other words
#  For each word, find the letter that appears the most times.
#  Find the word whose most-repeated letter appears more than any other.
# That is, if words is set to words = ['this', 'is', 'an', 'elementary', 'test', 'example']
# then your function should return elementary

from collections import Counter
# https://docs.python.org/3/library/collections.html#collections.Counter


# Primeras versión....  (la segunda versión es más elegante, más sencilla y rápida de implementar!!!!)
def most_repeating_word(words):
    palabra = ''
    max_letters = 0
    letra = ''
    for word in words:
        # Obtenemos el counter de cada palabra
        # y miramos la ocurrencia más común...
        # Nos da una lista con una tupla, cuyo primer elemento es el item (en este caso letra)
        # que más se repite y el segundo elemento, el número de veces que se repite
        tupla = Counter(word).most_common(1)[0]
        if tupla[1] > max_letters:
            letra = tupla[0]
            max_letters = tupla[1]
            palabra = word

    return (palabra, letra, max_letters)
    # return palabra

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
words2 = ['this', 'is', 'annnnnnnn', 'elementary', 'test', 'example']

palabra, letra, max_letters = most_repeating_word(words)

print('Primera versión: función most_repeating_wors')
print(f'La palabra con más letras repetidas es: "{palabra}". La letra "{letra}" se repite {max_letters} veces')


# Segunda versión!!! Mucho más sencillo
def cuenta_maximas_letras_repeticiones(word: str):
    return Counter(word).most_common(1)[0][1]

print('Segunda versión... utilizando la función máx con una key que funciona por palabras y es más sencilla')
print('La palabra con más repetidas de la lista es: ', max(words, key=cuenta_maximas_letras_repeticiones))
print('La palabra con más repetidas de la lista 2 es: ', max(words2, key=cuenta_maximas_letras_repeticiones))







