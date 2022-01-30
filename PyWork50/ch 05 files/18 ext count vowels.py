'''
Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
'''
from io import StringIO


def count_vowels_fake():
    # vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    # Equivalente, y más sencillo
    vocales = dict.fromkeys('aeiou', 0)

    for linea in fake_file:
        vocales['a'] += linea.count('a')
        vocales['e'] += linea.count('e')
        vocales['i'] += linea.count('i')
        vocales['o'] += linea.count('o')
        vocales['u'] += linea.count('u')

    return vocales

def count_vowels_fake_2():
    vocales = dict.fromkeys('aeiou', 0)
    for linea in fake_file:
        for letra in linea.lower():
            if letra in 'aeiou':
                vocales[letra] += 1

    return vocales

fake_file = StringIO('''
aee vcdou adfdf
ei oih ueae
''')

vocales = count_vowels_fake()
print(vocales)
