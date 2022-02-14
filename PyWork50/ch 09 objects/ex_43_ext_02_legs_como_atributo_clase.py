"""Instead of writing an __init__ method in each subclass, we could also have a
class attribute, number_of_legs, in each subclass—similar to what we did earlier
with Bowl and BigBowl. Implement the hierarchy that way. Do you even need an
__init__ method in each subclass, or will Animal.__init__ suffice?"""

'''O sea, modificar las clases de 43 animal class para que las patas 
sean un atributos de las clases Sheep, Wolf, et... y no de los animales...
En este caso, sería necesario tener un init para cada animal???
'''


class Animal:
    # No usar, es sólo como base!!
    def __init__(self, color):
        self.species = self.__class__.__name__.lower()
        # o sea, saca la especie de la clase derivada que la llama!!!
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class Sheep(Animal):
    number_of_legs = 4
    # Observar que no hace falta definir los __init__
    # Cuando se intente buscar el __init__ como no está,
    # se ejecutará el de la clase padre!! y todo_ funcionará bien!!
    # def __init__(self, color):
    #     super().__init__(color)


class Wolf(Animal):
    number_of_legs = 4


class Snake(Animal):
    number_of_legs = 0


class Parrot(Animal):
    number_of_legs = 2


if __name__ == '__main__':

    parrot = Parrot('blue')
    lobo = Wolf('gray')
    serpiente = Snake('green')
    oveja = Sheep('white')

    print(parrot)
    print(lobo)
    print(serpiente)
    print(oveja)
    '''Resultado --->
    Blue parrot, 2 legs
    Gray wolf, 4 legs
    Green snake, 0 legs
    White sheep, 4 legs
    '''
