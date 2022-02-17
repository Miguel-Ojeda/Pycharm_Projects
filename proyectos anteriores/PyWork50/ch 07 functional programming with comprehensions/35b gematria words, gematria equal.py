"""
In this exercise, you’ll write two functions:

 gematria_for, which takes a single word (string) as an argument and returns
the gematria score for that word (sumando el valor numérico de cada una de sus letras)

 gematria_equal_words, which takes a single word and returns
a list of those dict words whose gematria scores match the current word’s score.

For example, if the function is called with the word cat with a gematria value of 24 (3 + 1 + 20),
then the function will return a list of strings, all of whose gematria values are also 24.

(This will be a long list!)

Any non lowercase characters in the user’s input should count 0 toward our final score for the word.

Your source for the dict words will be the Unix file you used earlier in this chapter,
which you can load into a list comprehension  (el fichero words.txt)
"""
import pprint
import string
from e35a_gematria import gematria_dict

GEMATRIA = gematria_dict()


# Utilizamos generator expressions, en lugar de list comprehnsions... nos ahorramos memoria y los corchetes...
def gematria_for(word):
    return sum(GEMATRIA[letra.lower()]
                for letra in word
                if letra in string.ascii_letters)


# Versión Reuven es mejor... se ahorra la condición... obteniendo el valor con get!!!
def gematria_for_v2(word):
    return sum(GEMATRIA.get(letra.lower(), 0)
                for letra in word)


def gematria_equal_words(nuestra_palabra):
    score = gematria_for_v2(nuestra_palabra)
    # lo calculamos ya para no tener que ir calculando de nuevo para cada vez que comparemos...
    with open('files/words.txt', encoding='utf-8') as words:
        return [word.strip()  # le quitamos el '\n' final y espacios si hubiera
                for word in words
                if gematria_for_v2(word) == score]




resultado = gematria_for('Cat')
print(resultado)
# >>> 24

resultado = gematria_for_v2('C.+-#~€ at')
print(resultado)
# >>> 24

listado_palabras = gematria_equal_words('perro')
pprint.pprint(listado_palabras)

