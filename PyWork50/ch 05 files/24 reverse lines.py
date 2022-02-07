"""
In many cases, we want to take a file in one format and save it to another format.
In this function, we do a basic version of this idea.
The function takes two arguments: the names of the input file (to be read from)
and the output file (which will be created).

For example, if a file looks like
abc def
ghi jkl

then the output file will be
fed cba
lkj ihg
Notice that the newline remains at the end of the string, while the rest of the characters are all reversed
"""

from pathlib import Path


def reverse_lines_v1(text_file):
    text_file = Path(text_file)
    dir_base = text_file.parent
    result_file = dir_base / f'{text_file.stem}_reversed_v1{text_file.suffix}'
    with open(text_file) as file, open(result_file, 'w') as reversed_file:
        for line in file:
            if line[-1] == '\n':
                reversed_line = line[-2::-1] + '\n'
            else:
                # es la última línea y parece que no existe \n al final!!
                reversed_line = line[::-1]
            reversed_file.write(reversed_line)

# Después de ver solución de Reuven.... Muchísimo mejor!!!
def reverse_lines_v2(text_file):
    text_file = Path(text_file)
    dir_base = text_file.parent
    result_file = dir_base / f'{text_file.stem}_reversed_v2{text_file.suffix}'

    with open(text_file) as file, open(result_file, 'w') as reversed_file:
        for line in file:
            reversed_file.write(f'{line.rstrip()[::-1]}\n')


text_file = 'files/linux-etc-passwd.txt'
reverse_lines_v1(text_file)
reverse_lines_v2(text_file)

text_file = 'files/wcfile.txt'
reverse_lines_v1(text_file)
reverse_lines_v2(text_file)

