"""
From the examples we’ve seen so far, it might appear as though an iterable simply
goes through the elements of whatever data it’s storing and then exits.

But an iterator can do anything it wants, and can return whatever data it wants,
until the point when it raises StopIteration. In this exercise, we see just how that works.

Define a class, Circle, that takes two arguments when defined: a sequence and a number.
The idea is that the object will then return elements the defined number of times.

If the number is greater than the number of elements, then the sequence
repeats as necessary.

You should define the class such that it uses a helper (which I call CircleIterator).

Here’s an example:
c = Circle('abc', 5)
print(list(c))  --> Prints a, b, c, a, b
"""

# O sea, la clase Circle, al ser invocada, devuelve un objeto iterador!!!


class CircleIterator_v0:
    def __init__(self, secuencia, longitud):
        self.secuencia = secuencia
        self.longitud = longitud
        self.totales = 0
        self.indice_actual = 0

    def __next__(self):
        if self.totales == self.longitud:
            raise StopIteration
        valor_retorno = self.secuencia[self.indice_actual]
        if self.indice_actual == len(self.secuencia) - 1:
            self.indice_actual = 0
        else:
            self.indice_actual += 1

        self.totales += 1
        return valor_retorno


class CircleIterator_v1:
    # Después de ver solución de Reuven... muchísimo mejor
    # para saber el índice simplemente utiliza el módulo, ya está!!!
    def __init__(self, secuencia, longitud):
        self.secuencia = secuencia
        self.longitud = longitud
        self.indice = 0

    def __next__(self):
        if self.indice >= self.longitud:
            raise StopIteration
        valor_retorno = self.secuencia[self.indice % len(self.secuencia)]
        self.indice += 1
        return valor_retorno



class Circle:
    def __init__(self, secuencia, longitud):
        self.secuencia = secuencia
        self.longitud = longitud

    def __iter__(self):
        return CircleIterator_v1(self.secuencia, self.longitud)


c = Circle('abcd', 14)
for i in c:
    print(i)

print(list(c))