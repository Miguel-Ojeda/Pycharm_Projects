"""
One of my favorite objects in itertools is called chain.
It takes any number of iterables as arguments and then returns each of their elements,
one at a time, as if they were all part of a single iterable;
for example:

from itertools import chain
for one_item in chain('abc', [1,2,3], {'a':1, 'b':2}):
    print(one_item)

This code would print:
a b c 1 2 3 a b

While itertools.chain is convenient and clever, it’s not that hard to implement.
For this exercise, that’s precisely what you should do:

implement a generator function called mychain that takes any number of arguments,
each of which is an iterable.
With each iteration, it should return the next element from the current iterable,
or the first element from the subsequent iterable—unless you’re at the end, in which case it
should exit.
"""

def my_chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


# Prueba
for one_item in my_chain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
    print(one_item)
'''
a
b
c
1
2
3
a
b
'''


