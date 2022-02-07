"""
“Encrypt” a text file by turning all of its characters into
their numeric equivalents (with the built-in ord function) and writing that file to disk.

Now “decrypt” the file (using the built-in chr function),
turning the numbers back into their original characters.
"""

from pathlib import Path

def encrypt_text_file(text_file):
    text_file = Path(text_file)
    dir_base = text_file.parent
    result_file = dir_base / f'{text_file.stem}_encrypted{text_file.suffix}'
    with open(text_file) as file, open(result_file, 'w') as encrypted:
        for linea in file:
            # Le quitamos el \n y los espacios que pudiera haber por la derecha
            linea = linea.rstrip()
            for caracter in linea:
                encrypted.write(f'-{ord(caracter)}-')
            encrypted.write('\n')



text_file = 'files/texto sencillo.txt'
encrypt_text_file(text_file)
