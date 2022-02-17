"""It’s not very realistic to say that we would limit the number of animals in a cage.
Rather, it makes more sense to describe how much space each animal needs and to ensure
that the total amount of space needed per animal isn’t greater than the space in each cage.

You should thus modify each of the Animal subclasses to include a space_required attribute.
Then modify the Cage and BigCage classes to reflect how much space each one has.
Adding more animals than the cage can contain should raise an exception"""

class Animal:
    # No usar, es sólo como base!!
    def __init__(self, color):
        self.species = self.__class__.__name__.lower()
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class Sheep(Animal):
    number_of_legs = 4
    space_required = 5


class Wolf(Animal):
    number_of_legs = 4
    space_required = 10


class Snake(Animal):
    number_of_legs = 0
    space_required = 2


class Parrot(Animal):
    number_of_legs = 2
    space_required = 1


class NotEnoughSpaceError(Exception):
    pass


class Cage:
    total_space = 35

    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        self.espacio_ocupado = 0

    def add_animals(self, *animals):
        for animal in animals:
            if self.espacio_ocupado + animal.space_required > self.total_space:
                raise NotEnoughSpaceError(f'Cuidado, no hay espacio en la jaula para {animal}')
            self.animals.append(animal)
            self.espacio_ocupado += animal.space_required

    def __repr__(self):
        contenido_str = '\n'.join('\t' + repr(animal) for animal in self.animals)
        return f'\nJaula: {self.id_number}\n' \
               f'Espacio ocupado: {self.espacio_ocupado}/{self.total_space}' \
               f'\nContenido:\n{contenido_str}'


class BigCage(Cage):
    max_space = 50


caja_1 = Cage(1)
caja_1.add_animals(Sheep('brown'), Wolf('black'), Wolf('gray'), Sheep('white'))
# caja_1.add_animals(Parrot('orange'), Snake('blue'))
print(caja_1)
caja_2 = BigCage(2)
caja_2.add_animals(Wolf('brown'), Snake('black'), Parrot('gray'), Sheep('white'))
caja_2.add_animals(Parrot('orange'), Snake('blue'))
print(caja_2)