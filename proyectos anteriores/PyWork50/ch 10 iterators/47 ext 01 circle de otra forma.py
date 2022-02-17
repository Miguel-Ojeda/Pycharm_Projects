"""Rather than write a helper, you could also define iteration capabilities
in a class and then inherit from it.

Reimplement Circle as a class that inherits from CircleIterator,
which implements __init__ and __next__.

Of course, the parent class will have to know what to return in each iteration;
add a new attribute in Circle, self.returns, a list of attribute names that should be returned
"""

# O sea, ahora partimos del iterador, y el objeto Circle es derivado de él...
# Cojo el iterador del ej. 47


class CircleIterator:
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


class Circle(CircleIterator):
    def __init