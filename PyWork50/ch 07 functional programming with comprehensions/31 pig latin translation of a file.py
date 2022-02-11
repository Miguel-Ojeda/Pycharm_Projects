"""
In this exercise, I want you to write a function that takes a filename as an argument.
It returns a string with the file’s contents, but with each word translated into Pig
Latin, as per our plword function in chapter 2 on “strings.”

The returned translation can ignore newlines and isn’t required to handle capitalization
and punctuation in any specific way

Recordamos del capítulo 2...
The rules for translating words from English into Pig Latin are quite simple:
 If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the
word. So “air” becomes “airway” and “eat” becomes “eatway.”
 If the word begins with any other letter, then we take the first letter, put it on
the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay”
and “computer” becomes “omputercay.”
"""


# Como no me acuerdo, voy a hacer la función para pasar una palabra a piglatin
def piglatin_word(word):
    if word[0].lower() in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


from io import StringIO

fake_file = StringIO('''Esto es una prueba
para luego poder pasar
al fichero y hacer la prueba, si me apetece,
con un fichero.''')


def piglatin_file(text_file):
    with open(text_file, encoding='utf-8') as file:
        return ' '.join([piglatin_word(palabra)
                         for linea in file
                         for palabra in linea.strip().split()
                         ])


# Mejor como generator expression!! para ahorrar memoria  (además me ahorro los paréntesis interiores
def piglatin_file_v2(text_file):
    with open(text_file, encoding='utf-8') as file:
        return ' '.join(piglatin_word(palabra)
                         for linea in file
                         for palabra in linea.strip().split())

text_file = 'files/43-0.txt'
resultado = piglatin_file_v2(text_file)
print(resultado)

