"""Rewrite MyEnumerate such that it uses a helper class (MyEnumerateIterator),
as described in the “Discussion” section.

In the end, MyEnumerate will have the __iter__ method that returns a new instance
ESTA ES LA CLAVE, UNA NUEVA INSTANCIA
of MyEnumerateIterator, and the helper class will implement __next__.

It should work the same way, but will also produce results if we iterate over it twice in a row.
"""


# O sea, es mejor descomponer el iterable y ponerlo en una clase aparte...
# esto hace que simplifiquemos la estructura de la clase original...
# y además hace que podamos repetir varias iteraciones ....
class MyEnumerateIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.indice = 0

    def __next__(self):
        if self.indice >= len(self.iterable):
            raise StopIteration
        tupla = (self.indice, self.iterable[self.indice])
        self.indice += 1
        return tupla


class MyEnumerate:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return MyEnumerateIterator(self.iterable)






lista = [1, 2, 3]
secuencia = 'abcde fgh ijkl'

for i in MyEnumerate(lista):
    print(i)

for i in MyEnumerate(secuencia):
    print(i)


# Pega, sólo podemos usarlo una vez!!
e = MyEnumerate('abc')
print('** Primera vez que usamos el iterador **')
for index, one_item in e:
    print(f'{index}: {one_item}')

print('** Segunda vez que lo usamos **')
for index, one_item in e:
    print(f'{index}: {one_item}')

'''Ahora funciona, pq en cada bucle se llama
al método __iter__ que nos devuelve, creando
el objeto iterador nuevo, con índice 0!!!
Cuando hacemos for ...... in e, aquí, estamos haciendo
realmente e.__iter__(), que conlleva, en esta implementación
de un nuevo objeto iterador con índice a 0...'''