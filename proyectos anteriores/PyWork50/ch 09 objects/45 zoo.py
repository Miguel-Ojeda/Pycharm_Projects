"""Finally, the time has come to create our Zoo object. It will contain cage objects, and
they in turn will contain animals.

Our Zoo class will need to support the following operations:
 Given a zoo z, we should be able to print all of the cages (with their ID numbers)
and the animals inside simply by invoking print(z).

 We should be able to get the animals with a particular color by invoking the method z.animals_by_color.
For example, we can get all of the black animals by invoking z.animals_by_color('black').
The result should be a list of Animal objects.
 We should be able to get the animals with a particular number of legs by invoking the method z.animals_by_legs.
For example, we can get all of the fourlegged animals by invoking z.animals_by_legs(4).
The result should be a list of Animal objects.

 Finally, we have a potential donor to our zoo who wants to provide socks for all of the animals.
Thus, we need to be able to invoke z.number_of_legs() and get a count of the
total number of legs for all animals in our zoo.

The exercise is thus to create a Zoo class on which we can invoke the following:
z = Zoo()
z.add_cages(c1, c2)
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs()"""

from ex_43_ext_02_legs_como_atributo_clase import Sheep, Snake, Wolf, Parrot
from ex_44_cages import Cage


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages: Cage):
        for cage in cages:
            self.cages.append(cage)

    def __repr__(self):
        return '\n'.join(repr(caja) for caja in self.cages)

    def animals_by_color(self, color):
        return [animal
                for caja in self.cages
                for animal in caja.animals
                if animal.color == color]

    def animals_by_legs(self, legs):
        return [animal
                for caja in self.cages
                for animal in caja.animals
                if animal.number_of_legs == legs]

    def number_of_legs(self):
        return sum(animal.number_of_legs
                   for caja in self.cages
                   for animal in caja.animals)


zoo = Zoo()

caja_1 = Cage(1)
caja_2 = Cage(2)
caja_3 = Cage(3)
caja_4 = Cage(4)

caja_1.add_animals(Wolf('gray'), Snake('red'), Sheep('brown'), Parrot('green'))
caja_1.add_animals(Snake('orange'), Parrot('blue'), Wolf('black'))

caja_2.add_animals(Wolf('white'), Snake('blue'), Sheep('white'), Parrot('red'))
caja_2.add_animals(Snake('orange'), Snake('blue'), Snake('black'))

caja_3.add_animals(Wolf('gray'), Snake('red'), Sheep('brown'), Parrot('green'))
caja_3.add_animals(Parrot('orange'), Parrot('blue'), Parrot('black'))

caja_4.add_animals(Wolf('gray'), Snake('red'), Sheep('brown'), Parrot('green'))
caja_4.add_animals(Wolf('black'), Wolf('brown'), Wolf('white'))

zoo.add_cages(caja_1, caja_2, caja_3)
zoo.add_cages(caja_4)

print(zoo)

print(zoo.animals_by_color('red'))
print(zoo.animals_by_legs(2))
print(zoo.number_of_legs())





