"""
The built-in zip function returns an iterator that, given iterable arguments,
returns tuples taken from those arguments’ elements.

The first iteration will return a tuple from the arguments’ index 0,
the second iteration will return a tuple from the arguments’ index 1,
and so on, stopping when the shortest of the arguments ends.

Thus zip('abc', [10, 20, 30]) returns the iterator equivalent of
[('a', 10), ('b', 20), ('c', 30)].

Write a generator function that reimplements zip in this way
"""

def my_zip(*iterables):
    minimo = min(len(iterable) for iterable in iterables)
    '''
    Opción de Reuven es más sencilla para calcular el mínimo
    minimo = min(iterables, key=len)
    '''
    for index in range(minimo):
        yield tuple([iterable[index] for iterable in iterables])


for item in my_zip('abc', [10, 20, 30], [444, 555, 666, 777, 888]):
    print(item)

