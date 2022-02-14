"""For the purposes of these exercises, you are the director of IT at a zoo.
The zoo contains several different kinds of animals, and for budget reasons,
some of those animals have to be housed alongside other animals.

We will represent the animals as Python objects, with each species defined as a distinct class.

All objects of a particular class will have the same species and number of legs,
but the color will vary from one instance to another.

We can thus create a white sheep s = Sheep('white')
I can similarly get information about the animal back from the object by retrieving its attributes:
print(s.species)
print(s.color)
print(s.number_of_legs)
If I convert the animal to a string (using str or print), I’ll get back a string combining all of these details:
print(s) --> Prints “White sheep, 4 legs”
We’re going to assume that our zoo contains four different types of animals:
sheep, wolves, snakes, and parrots.
(The zoo is going through some budgetary difficulties, so our animal collection is both small and unusual.)
Create classes for each of these types, such that we can print each of them and get
a report on their color, species, and number of legs.
"""


# MUY INTERESANTE LA SOLUCIÖN DE REUVEN...
# La mía la borré, era bastante peor...
# Esta minimiza el código en las clases derivadas!!
'''
Abstract base classes
The Animal class here is what other languages might call an abstract base class,
namely one that we won’t actually instantiate, but from which other classes will inherit.
In Python, you don’t have to declare such a class to be abstract, but you also won’t get
the enforcement that other languages provide.
If you really want, you can import ABC-Meta from the abc (abstract base class) module.
Following its instructions, you’ll be able to declare particular methods as abstract,
meaning that they must be overridden in the child.

I’m not a big fan of abstract base classes; I think that it’s enough to document a class
as being abstract, without the overhead or language enforcement.
Whether that’s a smart approach depends on several factors, including the nature and size
of the project you’re working on and whether you come from a background in dynamic languages.
A large project, with many developers, would probably benefit from the additional safeguards
that an abstract base class would provide.
If you want to learn more about abstract base classes in Python, you can read about
ABCMeta here: http://mng.bz/yyJB.
'''
class Animal:
    # No usar, es sólo como base!!
    # Reuven prefiere no usar clases abstractas ABCMeta, leer anterior
    def __init__(self, color, number_of_legs):
        self.number_of_legs = number_of_legs
        self.species = self.__class__.__name__.lower()
        # o sea, saca la especie de la clase derivada que la llama!!!
        self.color = color

    def __repr__(self):
        return f'{self.color.title()} {self.species}, {self.number_of_legs} legs'


class Sheep(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):

    def __init__(self, color):
        super().__init__(color, 2)
        # También podríamos...
        # Animal.__init__(self, color, 2)
        # O sea, super me devuelve la función y el objeto apropiado ya!!


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
