"""Modify animals_by_color such that it takes any number of colors.
Animals having any of the listed colors should be returned.
The method should raise an exception if no colors are passed."""

# O sea, voy a partir de 45 zoo pero simplemente voy a modificar el método para obtener los
# animales del zoo, ahora pudiendo elegir varios colores para seleccionar a los animales,
# en vez de uno solo como antes...

from ex_43_ext_02_legs_como_atributo_clase import Sheep, Snake, Wolf, Parrot
from ex_44_cages import Cage


class NoColorsPassedError(Exception):
    pass


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages: Cage):
        for cage in cages:
            self.cages.append(cage)

    def __repr__(self):
        return '\n'.join(repr(caja) for caja in self.cages)

    def animals_by_color(self, *colores):
        if not colores:
            raise NoColorsPassedError('No ha pasado ningún color para seleccionar')
        return [animal
                for caja in self.cages
                for animal in caja.animals
                if animal.color in colores]

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

print(zoo.animals_by_color('orange', 'red', 'black'))
# print(zoo.animals_by_legs(2))
# print(zoo.number_of_legs())





