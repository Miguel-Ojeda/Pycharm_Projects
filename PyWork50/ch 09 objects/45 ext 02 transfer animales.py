"""As things currently stand, we’re treating our Zoo class almost as if it’s a singleton
object—that is, a class that has only one instance.

Let’s assume, then, that we have two instances of Zoo, representing two different zoos,
and that we would like to transfer an animal from one to the other.

Implement a Zoo.transfer_animal method that takes a target_zoo and a subclass of Animal as arguments.

The first animal of the specified type is removed from the zoo on which we’ve called the method and
inserted into the first cage in the target zoo."""

# Parto de l anterior, 45 ext 01

from ex_43_ext_02_legs_como_atributo_clase import Sheep, Snake, Wolf, Parrot, Animal
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

    def transfer_animal(self, target_zoo, species):
        # Cuidado, no transferimos un animal concreto, sino cualquiera de la especie especificada
        # La especie puede ser cualquier subclase de Animal, o sea, Snake, Sheep, Wolf, o Parrot
        # vamos a borrar el animal de su jaula en el zoo original
        for jaula in self.cages:
            for animal in jaula.list_of_animals:
                # Creo que tb valdría con type(animal) == species
                if isinstance(animal, species):
                    jaula.remove(animal)
                    # No lo he probado... pero existe jaula.remove???
                    target_zoo.cages[0].add_animals(animal)

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

