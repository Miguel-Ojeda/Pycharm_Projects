"""
Define a Person class, and a population class attribute that increases each time
you create a new instance of Person.

Double-check that after you’ve created five instances, named p1 through p5,
Person.population and p1.population are both equal to 5.
"""

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
        print(f'Creando a la persona nº {Person.population}: {name}')


if __name__ == '__main__':

    p1 = Person('Juan')
    p2 = Person('Pepe')
    p3 = Person('Luis')
    p4 = Person('Carla')
    p5 = Person('Eustaquio')


