"""As you can see, there are no limits on how many animals can potentially be put into a cage.

Just as we put a limit of three scoops in a Bowl and five in a BigBowl,
you should similarly create Cage and BigCage classes that limit the number of
animals that can be placed there."""

from ex_43_ext_02_legs_como_atributo_clase import Sheep, Snake, Wolf, Parrot


class Cage:
    max_animals = 3

    def __init__(self, id_number):

        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            if len(self.animals) < self.max_animals:
                self.animals.append(animal)

    def __repr__(self):
        contenido_str = '\n'.join('\t' + repr(animal) for animal in self.animals)
        return f'Jaula: {self.id_number}\nContenido:\n{contenido_str}'
        # return f'Jaula: {self.id}\nContenido:\n{animal for animal in self.list.of_animals}'

class BigCage(Cage):
    max_animals = 5

caja_1 = Cage(1)
caja_1.add_animals(Sheep('brown'), Wolf('black'), Wolf('gray'), Sheep('white'))
caja_1.add_animals(Parrot('orange'), Snake('blue'))
print(caja_1)
caja_2 = BigCage(2)
caja_2.add_animals(Wolf('brown'), Snake('black'), Parrot('gray'), Sheep('white'))
caja_2.add_animals(Parrot('orange'), Snake('blue'))
print(caja_2)