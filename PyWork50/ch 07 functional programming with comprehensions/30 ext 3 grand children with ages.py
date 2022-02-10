"""Redo this exercise, but replace each grandchild’s name (currently a string) with
a dict. Each dict will contain two name-value pairs, name and age. Produce a list
of the grandchildren’s names, sorted by age, from eldest to youngest
"""
import operator
import pprint

"""Recordemos...
la familia es un diccionario... las keys, en este caso Hijo_1, Hijo_2, Hijo_3, representan los 3 hijos
de una familia...
Los values representan los nietos (o sea, la value asociada a cada hijo, son sus hijos"""


familia = {'Hijo_1': [{'name': 'Juan', 'age': 14},
                      {'name': 'Miguel', 'age': 25},
                      {'name': 'Fran', 'age': 13},
                      {'name': 'Luisa', 'age': 20}],
           'Hijo_2': [{'name': 'Carla', 'age': 12},
                      {'name': 'Benito', 'age': 18}],
           'Hijo_3': [{'name': 'Ana', 'age': 16},
                      {'name': 'Lucía', 'age': 20},
                      {'name': 'Iris', 'age': 15},
                      {'name': 'Penélope', 'age': 7},
                      {'name': 'Virginia', 'age': 10}],
           }


def get_grandchildren_names(familia):
    """Aquí no he conseguido que salga ordenada"""
    return[nieto['name']
           for nietos in familia.values()
           for nieto in nietos]


nietos = get_grandchildren_names(familia)
pprint.pprint(nietos)
'''
No están ordenadas, aparecen en el orden tal cuál aparecen en el diccionario!!
['Juan',
 'Miguel',
 'Fran',
 'Luisa',
 'Carla',
 'Benito',
 'Ana',
 'Lucía',
 'Iris',
 'Penélope',
 'Virginia']'''



def get_grandchildren_names_v2(familia):
    """Aquí ya consigo ordenarlo, pero me aparecen diccionarios!!"""
    return sorted([nieto
                   for nietos in familia.values()
                   for nieto in nietos], key=operator.itemgetter('age'))


nietos = get_grandchildren_names_v2(familia)
pprint.pprint(nietos)
'''
Casi, me aparece el diccionario entero... sólo debería tener el nombre
[{'age': 7, 'name': 'Penélope'},
 {'age': 10, 'name': 'Virginia'},
 {'age': 12, 'name': 'Carla'},
 {'age': 13, 'name': 'Fran'},
 {'age': 14, 'name': 'Juan'},
 {'age': 15, 'name': 'Iris'},
 {'age': 16, 'name': 'Ana'},
 {'age': 18, 'name': 'Benito'},
 {'age': 20, 'name': 'Luisa'},
 {'age': 20, 'name': 'Lucía'},
 {'age': 25, 'name': 'Miguel'}]
 '''

def get_grandchildren_names_v3(familia):
    """Aquí ya consigo ordenarlo, aunque de dos pasos...!!"""
    nietos = sorted([nieto
                     for nietos in familia.values()
                     for nieto in nietos], key=operator.itemgetter('age'))
    return [nieto['name']
            for nieto in nietos]


def get_grandchildren_names_v3bis(familia):
    """¡Aquí ya consigo ordenarlo, aunque de dos pasos
    Esta versión es igual que la 3, aunque quizás más clara
    pq primero genero los nietos y luego, al devolver, es cuando los ordeno...!!"""
    nietos = [nieto
              for nietos in familia.values()
              for nieto in nietos]
    return [nieto['name']
            for nieto in sorted(nietos, key=operator.itemgetter('age'))]

nietos = get_grandchildren_names_v3(familia)
pprint.pprint(nietos)
nietos = get_grandchildren_names_v3bis(familia)
pprint.pprint(nietos)


def get_grandchildren_names_v4(familia):
    lista_nietos = []
    for nietos in familia.values():
        lista_nietos.extend(nietos)
    return [nieto['name']
            for nieto in sorted(lista_nietos, key=operator.itemgetter('age'))]


nietos = get_grandchildren_names_v4(familia)
pprint.pprint(nietos)







