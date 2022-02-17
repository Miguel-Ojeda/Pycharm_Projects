"""
Given an existing text file, create two new text files. The new files will each contain the same number of lines as the input file. In one output file, you’ll write
all of the vowels (a, e, i, o, and u) from the input file. In the other, you’ll write
all of the consonants. (You can ignore punctuation and whitespace.)
"""

from pathlib import Path
import string

def get_vowels_and_consonants(text_file):
    text_file = Path(text_file)
    dir_base = text_file.parent
    vowels_file = dir_base / f'{text_file.stem}_vowels{text_file.suffix}'
    consonants_file = dir_base / f'{text_file.stem}_consonants{text_file.suffix}'

    with open(text_file) as file, open(vowels_file, 'w') as vowels, open(consonants_file, 'w') as consonants:
        for linea in file:
            for caracter in linea:
                if caracter in 'aAeEiIoOuU':
                    vowels.write(caracter)
                elif caracter in string.ascii_letters:
                    # es consonante
                    consonants.write(caracter)
            # Añadimos el final de línea
            consonants.write('\n')
            vowels.write('\n')


text_file = 'files/texto sencillo.txt'
get_vowels_and_consonants(text_file)
text_file = 'files/wcfile.txt'
get_vowels_and_consonants(text_file)



