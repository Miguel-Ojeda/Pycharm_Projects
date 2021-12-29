# Clase vector
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x + vec.x, self.y + vec.y)
        else:
            raise TypeError('El segundo objeto debe ser también un vector')

    def __sub__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x - vec.x, self.y - vec.y)
        else:
            raise TypeError('El segundo objeto debe ser también un vector')

    def __mul__(self, vec_o_num):
        if isinstance(vec_o_num, Vector):
            # Tenemos dos vectores: devolveremos, por ejemplo, el vector producto de las componenetes
            return Vector(self.x * vec_o_num.x, self.y * vec_o_num.y)
        elif isinstance(vec_o_num, int):
            # Tenemos un vector por un número... multiplicaremos el número por ambas componentes...
            return Vector(vec_o_num * self.x, vec_o_num * self.y)
        else:
            raise TypeError('El segundo objecto debe ser otro vector o un escalar')

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, vec):
        if isinstance(vec, Vector):
            return self.x == vec.x and self.y == vec.y
        else:
            raise TypeError('El segundo objeto debe ser también un vector')

    def __ne__(self, vec):  # called for != operator
        return not (self == vec)  # calls __eq__ method

    def __lt__(self, vec):  # called for < operator
        if not isinstance(vec, Vector):
            raise TypeError('El segundo objeto debe ser tb. un vector')
        return abs(self) < abs(vec)

    def __gt__(self, vec):
        return vec.__lt__(self)

    def __str__(self):
        return 'Este vector vale (' + str(self.x) + ', ' + str(self.y) + ')'

vec1 = Vector(2, 3)
vec2 = Vector(3, 7)
print(vec1)
print(vec2)
print(vec1 + vec2)
print(vec1 - vec2)
print(vec1 * vec2)
print(vec1 * 4)
print(abs(vec1))
print(abs(vec2))
print(vec1 > vec2)
print(vec1 < vec2)
print(vec1 == vec2)
