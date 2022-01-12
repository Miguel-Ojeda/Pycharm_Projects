# write a function, alphabetize_names, that assumes the existence of a
# PEOPLE constant defined as shown in the code. The function should return the list of
# dicts, but sorted by last name and then by first name.

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'},
          {'first': 'Miguel', 'last': 'ojeda', 'email': 'mojec....'},
          ]

def alphabetize_names():
    pass


# Función 1 que utilizaremos para ordenar con la opción 1
def tupla_orden(diccionario: dict):
    return tuple((diccionario['last'].lower(), diccionario['first'].lower()))
    # La ventaja que tiene esta función para ordenar
    # frente al itemgetter es que le podemos meter el método lower...


# Callable 2 que utilizaremos para ordenar con la opción 2
import operator
ordenador = operator.itemgetter('last', 'first')



# Probamos aquí como funcionan la función y el callable que utilizaremos para ordenar...
for person in PEOPLE:
    print(tupla_orden(person))
    print(ordenador(person))

people_orden1 = sorted(PEOPLE, key=tupla_orden)
people_orden2 = sorted(PEOPLE, key=ordenador)

print(people_orden1)
print(people_orden2)
