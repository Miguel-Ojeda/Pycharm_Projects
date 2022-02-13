"""
Python provides a __del__ method that’s executed when an object is garbage collected.

(In my experience, deleting a variable or assigning it to another object
triggers the calling of __del__ pretty quickly.)

Modify your Person class such that when a Person instance is deleted,
the population count decrements by 1.

If you aren’t sure what garbage collection is, or how it works in Python,
take a look at this article: http://mng.bz/nP2a.
"""

# Parto de 40 ext 01

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1
        print(f'Creando a la persona nº {Person.population}: {name}')


    def __del__(self):
        Person.population -= 1
        print(f'Se destruye la persona {self.name}\nPoblación actual: {Person.population}.')


if __name__ == '__main__':

    juan = Person('Juan')
    pepe = Person('Pepe')
    luis = Person('Luis')
    carla = Person('Carla')
    eustaquio = Person('Eustaquio')

    print(0)
    del(luis)
    print(1)
    del(eustaquio)
    print(2)
    # Ahora tb se destruye el objeto Person asociado a juan anteriormente
    # ya que su reference count se hace 0!!!
    juan = 'Hola'

    print('FIN')
    # Aquí se deberían de destruir los objetos que quedan, pepe y carla
    # pq al terminar el programa lógicamente sus reference count van a 0
    # y se invocar el método __del__ para ellos...

    '''
    La salida que muestra la destrucción de los objetos.,,
    empezando en donde hacemos print(0) es la siguiente...
    0
    Se destruye la persona Luis
    Población actual: 4.
    1
    Se destruye la persona Eustaquio
    Población actual: 3.
    2
    Se destruye la persona Juan
    Población actual: 2.
    FIN
    Se destruye la persona Pepe
    Población actual: 1.
    Se destruye la persona Carla
    Población actual: 0.
    '''