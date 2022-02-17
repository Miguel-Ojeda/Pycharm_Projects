"""
Reimplement the all_lines function from exercise 48 using my_chain.
"""
def my_chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

from pathlib import Path



def all_lines_all_files(directorio):
    path = Path(directorio)
    return my_chain(*(open(fichero, encoding='utf-8')
                     for fichero in path.glob('*')))


directorio = 'files'
for item in all_lines_all_files(directorio):
    print(item)