# find  the word with the greatest number of repeated vowels.
# Basado en word with most repeated letters...

from collections import Counter
# https://docs.python.org/3/library/collections.html#collections.Counter


def cuenta_maximas_vocales_repetidas(word: str):

    lista_tupla_valores_repetidos = Counter(word).most_common()
    # Tendremos ahora una lista con las tuplas valor (letra) y repeticiones...
    repeticiones = 0
    for tupla in lista_tupla_valores_repetidos:
        # estamos en una lista, donde los primeros elementos son los más repetidos...
        # el primer elemento que aparezca que sea vocal ya estaría
        if tupla[0].lower() in 'aeiou':
            repeticiones = tupla[1]
            return repeticiones

# Versión más sencilla, similar a lo del ejercicio anterior....
# Simplificamos primero la palabra!!!!!
# Es más sencillo porque no tenemos que recurrir a estructuras tan complicadas...
def cuenta_maximas_vocales_repetidas_v2(word: str):
    palabra_solo_con_vocales = ''
    for letra in word:
        if letra in 'aeiou':
            palabra_solo_con_vocales += letra

    return Counter(palabra_solo_con_vocales).most_common(1)[0][1]


# Segunda versión!!! Mucho más sencillo....
def cuenta_maximas_letras_repeticiones(word: str):
    return Counter(word).most_common(1)[0][1]

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
words2 = ['this', 'is', 'annnnnnnn', 'elementary', 'test', 'example']

print('La palabra con más repetidas de la lista es: ', max(words, key=cuenta_maximas_vocales_repetidas))
print('La palabra con más repetidas de la lista es: ', max(words, key=cuenta_maximas_vocales_repetidas_v2))

print('La palabra con más repetidas de la lista 2 es: ', max(words2, key=cuenta_maximas_vocales_repetidas))
print('La palabra con más repetidas de la lista 2 es: ', max(words2, key=cuenta_maximas_vocales_repetidas_v2))


