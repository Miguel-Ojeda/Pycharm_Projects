"""
In this exercise, I want you to write a get_sv function that returns a set of all “supervocalic” words in the dict.
If you’ve never heard the term supervocalic before, you’re not alone:
I only learned about such words several years ago. Simply put, such words contain all five vowels in English
each of them appearing once and in alphabetical order.
For the purposes of this exercise, I’ll loosen the definition, accepting any word that has all five vowels,
in any order and any number of times.

Your function should find all of the words that match this definition and return a set containing them.

Your function should take a single argument: the name of a text file containing one word per line,
as in a Unix/Linux dict. If you don’t have such a “words” file, you can download one from here: http://mng.bz/D2Rw.
"""

# Suponemos pues el fichero que nos da con una palabra por línea
import pprint


def get_super_vocalic(unix_dict):
    with open(unix_dict, encoding='utf-8') as texto_file:
        return {linea.strip()
                for linea in texto_file
                if sum([letra in linea.lower()
                        for letra in 'aeiou']) == 5
                }


def get_super_vocalic_v2(unix_dict):
    with open(unix_dict, encoding='utf-8') as texto_file:
        return {linea.strip()
                for linea in texto_file
                if set('aeiou') <= set(linea.strip().lower())
                }

def get_super_vocalic_v3(unix_dict):
    # Mejor, respecto a v2, Reuven define ya de entrada el set que vamos a usar...
    # no como en la v2
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(unix_dict, encoding='utf-8') as texto_file:
        return {linea.strip()
                for linea in texto_file
                if vowels <= set(linea.lower())
                }

file = 'files/words.txt'

resultado = get_super_vocalic(file)
pprint.pprint(resultado)

resultado_2 = get_super_vocalic_v2(file)
pprint.pprint(resultado_2)

resultado_3 = get_super_vocalic_v3(file)
pprint.pprint(resultado_3)
print(resultado == resultado_3)