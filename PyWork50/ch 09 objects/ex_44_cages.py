"""Now that we’ve created some animals, it’s time to put them into cages.
For this exercise, create a Cage class, into which you can put one or more animals, as follows:
c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

When you create a new Cage, you’ll give it a unique ID number.
(The uniqueness doesn’t need to be enforced, but it’ll help us to distinguish among the cages.)

You’ll then be able to invoke add_animals on the new cage,
passing any number of animals that will be put in the cage.

I also want you to define a __repr__ method so that printing a cage
prints not just the cage ID, but also each of the animals it contains
"""

# Me quedaré con la versión más sencilla, la que pone las patas como atributo en la clase
# de cada tipo de animal
from ex_43_ext_02_legs_como_atributo_clase import Sheep, Snake, Wolf, Parrot


class Cage:
    def __init__(self, id_number):
        # Esta sería una opción, pero mejor indicamos nosotros el número de la caja!!
        # self.id = id(self)
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)
        # podríamos tb poner
        # self.list_of_animals.extend(animales)

    def __repr__(self):
        contenido_str = '\n'.join('\t' + repr(animal) for animal in self.animals)
        return f'Jaula: {self.id_number}\nContenido:\n{contenido_str}'
        # return f'Jaula: {self.id}\nContenido:\n{animal for animal in self.list.of_animals}'


if __name__ == '__main__':
    caja_1 = Cage(1)
    caja_1.add_animals(Sheep('brown'), Wolf('black'), Wolf('gray'))
    caja_1.add_animals(Parrot('orange'), Snake('blue'))
    print(caja_1)
    caja_2 = Cage(2)
    print(caja_2)


