"""Our zookeepers have a macabre sense of humor when it comes to placing animals together,
in that they put wolves and sheep in the first cage, and snakes and birds in the other cage.

Define a dict describing which animals can be with others.
The keys in the dict will be classes, and the values will be lists of classes
that can compatibly be housed with the keys.

Then, when adding new animals to the current cage, you’ll check for compatibility.

Trying to add an animal to a cage that already contains an incompatible animal will raise an exception."""

# Parto de todo_ lo anterior en 44 ext 02 pero añado el diccionario de la seguridad,
#  y modifico el método add de Cage para comprobar la seguridad


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

# Supondremos que las únicas incompatibilidades son meter a los lobos con las ovejas
# y a las serpientes con los loros
COMPATIBLE = {Parrot: [Parrot, Sheep, Wolf],
              Sheep: [Sheep, Parrot, Snake],
              Wolf: [Wolf, Parrot, Snake],
              Snake: [Snake, Wolf, Sheep],
              }

class DangerousAssignmentError(Exception):
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
            for animal_ya_enjaulado in self.animals:
                if type(animal) not in COMPATIBLE[type(animal_ya_enjaulado)]:
                    raise DangerousAssignmentError(f'No puedes poner un {type(animal)} '
                                                   f'con un {type(animal_ya_enjaulado)}')
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