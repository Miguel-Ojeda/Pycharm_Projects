"""
File objects, as we’ve seen, are iterators;
when we put them in a for loop, each iteration returns the next line from the file.

But what if we want to read through a number of files?
It would be nice to have an iterator that goes through each of them.

In this exercise, I’d like you to create just such an iterator, using a generator function.
That is, this generator function will take a directory name as an argument.
With each iteration, the generator should return a single string, representing one line from
one file in that directory.
Thus, if the directory contains five files, and each file contains 10 lines,
the generator will return a total of 50 strings—each of the lines from file
0, then each of the lines from file 1, then each of the lines from file 2,
until it gets through all of the lines from file 4.

If you encounter a file that can’t be opened—because it’s a directory, because
you don’t have permission to read from it, and so on—you should just ignore the
problem altogether."""

from pathlib import Path

def all_lines_all_files(directorio):
    path = Path(directorio)
    lista_ficheros = path.glob('*')
    for fichero in lista_ficheros:
        try:
            with open(fichero, encoding='utf-8') as file_text:
                for linea in file_text:
                    yield linea
        except:
            pass


directorio = 'files'

for linea in all_lines_all_files(directorio):
    if linea.endswith('\n'):
        print(linea, end='')
    else:
        print(linea)




