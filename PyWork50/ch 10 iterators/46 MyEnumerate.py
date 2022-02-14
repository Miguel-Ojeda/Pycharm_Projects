"""
The built-in enumerate function allows us to get not just the elements of a sequence, but also
the index of each element, as in for index, letter in enumerate('abc'):
print(f'{index}: {letter}')

Create your own MyEnumerate class, such that someone can use it instead of enumerate.

It will need to return a tuple with each iteration, with the first element in the
tuple being the index (starting with 0) and the second element being the current
element from the underlying data structure.

Trying to use MyEnumerate with a noniterable argument will result in an error.
"""


# Ayuda: https://docs.python.org/3/library/functions.html?#iter
'''iter(object[, sentinel])
Return an iterator object. The first argument is interpreted very differently depending
on the presence of the second argument.
Without a second argument, object must be a collection object which supports the iterable protocol
(the __iter__() method), or it must support the sequence protocol
(the __getitem__() method with integer arguments starting at 0).
If it does not support either of those protocols, TypeError is raised'''


# Mi versión utiliza el iterable que ya existe....
class MyEnumerate_v0:
    def __init__(self, iterable):
        self.iterable = iterable
        self.indice = 0
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        tupla = (self.indice, next(self.iterator))
        self.indice += 1
        return tupla


class MyEnumerate_v1:
    """Es la versión mejor, Reuven"""
    def __init__(self, iterable):
        self.iterable = iterable
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.iterable):
            raise StopIteration
        tupla = (self.indice, self.iterable[self.indice])
        self.indice += 1
        return tupla


lista = [1, 2, 3]
secuencia = 'abcde fgh ijkl'

for i in MyEnumerate_v0(lista):
    print(i)

for i in MyEnumerate_v0(secuencia):
    print(i)

for i in MyEnumerate_v1(lista):
    print(i)

for i in MyEnumerate_v1(secuencia):
    print(i)


# Pega, sólo podemos usarlo una vez!!
e = MyEnumerate_v1('abc')
print('** Primera vez que usamos el iterador **')
for index, one_item in e:
    print(f'{index}: {one_item}')

print('** Segunda vez que lo usamos **')
for index, one_item in e:
    print(f'{index}: {one_item}')

'''Salida de la prueba final...
Se observa que sólo podemos recorrer una vez el objeto iterable...
** Primera vez que usamos el iterador **
0: a
1: b
2: c
** Segunda vez que lo usamos **
# AQUÍ NO HAY SALIDA NINGUNA; ya se quedó exhausto el iterador!!!
'''