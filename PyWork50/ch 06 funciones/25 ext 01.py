"""
Write a copyfile function that takes one mandatory argument —the name of an input file—
and any number of additional arguments: the names of files to which the input should be copied.

Calling copyfile('myfile.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')
will create three copies of myfile.txt: one each in copy1.txt, copy2.txt, and copy3.txt.

SUPONDREMOS QUE LOS FICHEROS SON DE TEXTO....
"""

from pathlib import Path


'''
def copyfile_v0(original_file, *args):
    """
    Utilizamos Python shutil utilities
    """
    original_file = Path(original_file)
    for dest_file in args:
        shutil.copyfile(original_file, dest_file)
'''


def copyfile_v1(original_file, *args):
    for out_file in args:
        with open(original_file, encoding='utf-8') as original, open(out_file, 'w', encoding='utf-8') as out:
            for linea in original:
                out.write(linea)


# copyfile_v0('files/43-0.txt', 'files/copia1.txt', 'files/copia2.txt', 'files.copia3.txt',
#             'files/copia4.txt', 'files/copia5.txt', 'files/copia6.txt', 'files.copia7.txt')

copyfile_v1('files/43-0.txt', 'files/copia1.txt', 'files/copia2.txt', 'files.copia3.txt',
            'files/copia4.txt', 'files/copia5.txt', 'files/copia6.txt', 'files.copia7.txt')


