# Partimos de la implementación guay (con el iterator en clase aparte)
# Ahora se trata de poder especificar en otro argumento, cuál es el índice inicial
'''
The built-in enumerate method takes a second, optional argument—an integer,
representing the first index that should be used. (This is particularly handy
when numbering things for nontechnical users, who believe that things should
be numbered starting with 1, rather than 0.)
'''

class MyEnumerateIterator:
    def __init__(self, iterable, inicio):
        self.iterable = iterable
        self.indice = 0
        self.inicio = inicio

    def __next__(self):
        if self.indice >= len(self.iterable):
            raise StopIteration
        tupla = (self.indice + self.inicio, self.iterable[self.indice])
        self.indice += 1
        return tupla


class MyEnumerate:
    def __init__(self, iterable, inicio=0):
        self.iterable = iterable
        self.inicio = inicio

    def __iter__(self):
        return MyEnumerateIterator(self.iterable, self.inicio)


e = MyEnumerate('Hola, ¿como estás?', 5)

for i in e:
    print(i)