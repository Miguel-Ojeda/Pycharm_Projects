"""Assume that you have a list of dicts, in which each dict contains two name-value
pairs: name and hobbies, where name is the person’s name and hobbies is a set of strings
representing the person’s hobbies.

What are the three most popular hobbies among the people listed in the dicts?
"""
import pprint

people_hobbies = [dict(name='Gregorio', hobbies={'ciclismo', 'fútbol', 'petanca'}),
                  dict(name='Paola', hobbies={'fútbol', 'cine', 'ajedrez', 'patinaje'}),
                  dict(name='Ana', hobbies={'baloncesto', 'ciclismo', 'lectura', 'ajedrez', 'programación'}),
                  dict(name='Eva', hobbies={'voley', 'cine', 'fútbol', 'baloncesto'}),
                  dict(name='Adán', hobbies={'balonmano', 'parapente', 'baile'}),
                  dict(name='Gina', hobbies={'badminton', 'fútbol', 'música'}),
                  dict(name='Mist', hobbies={'fútbol', 'lectura', 'balonmano', 'voley'}),
                  dict(name='John', hobbies={'bolos', 'baloncesto', 'baile'}),
                  dict(name='Carlos', hobbies={'balonmano', 'fútbol', 'fotografía'}),
                  dict(name='Yera', hobbies={'badminton', 'cine', 'pesca', 'baloncesto'}),
                  dict(name='Buffy', hobbies={'parapente', 'balonmano', 'lectura', 'ajedrez'}),
                  dict(name='Aarón', hobbies={'baloncesto', 'cine', 'voley', 'fútbol', 'programación'}),
                  ]

# pprint.pprint(people_hobbies)


def three_most_repaeted_hobbies_v0(people_hobbies):
    """Me retorna todos los hobbies, en un set, sin repetir!!"""
    todos_los_hobbies = set()
    for person in people_hobbies:
        todos_los_hobbies.update(person['hobbies'])

    return todos_los_hobbies


def three_most_repaeted_hobbies_v1(people_hobbies):
    # Me retorna una lista con todos los hobbies, repetidos las veces que se repiten!!
    lista_todos_hobbies = [hobbie
                           for persona in people_hobbies
                           for hobbie in persona['hobbies']]

    return lista_todos_hobbies


from collections import Counter
def three_most_repaeted_hobbies_v2(people_hobbies):
    # Ahora ya debería servir, nos basamos en v1 para obtener una lista con todos los hobbies repetidos
    # y, a raíz de esa lista pues simplemente creamos un objeto counter!!!

    contador_hobbies = Counter([hobbie
                                for persona in people_hobbies
                                for hobbie in persona['hobbies']]
                               )

    return contador_hobbies


def three_most_repaeted_hobbies_v3(people_hobbies):
    # Con esto ya conseguimos lo que buscábamos, averiguar los 3 hobbies más comunes
    # utilizamos simplemente el counter (es lo de antes, pero ahora retornamos no todo_
    # el counter, sino los 3 elementos más repetidos
    contador_hobbies = Counter([hobbie
                                for persona in people_hobbies
                                for hobbie in persona['hobbies']]
                               )

    return contador_hobbies.most_common(3)


def three_most_repaeted_hobbies_v4(people_hobbies):
    # Es lo mismo, pero supercompacto, y sigue siendo claro!!
    return Counter([hobbie
                    for persona in people_hobbies
                    for hobbie in persona['hobbies']]).most_common(3)



set_hobbies = three_most_repaeted_hobbies_v0(people_hobbies)
print(set_hobbies)
'''
NOS DEVUELVE TODOS LOS HOBBIES SIN REPETIR; PQ HEMOS CREADO UN SET!!
{'ciclismo', 'parapente', 'cine', 'petanca', 'fotografía', 'música', 'voley', 'balonmano', 'baloncesto', 'ajedrez',
'badminton', 'patinaje', 'pesca', 'baile', 'programación', 'lectura', 'bolos', 'fútbol'}
'''

lista_hobbies = three_most_repaeted_hobbies_v1(people_hobbies)
print(lista_hobbies)
'''
Devuelve una lista con todos los hobbies, apareciendo repetidos incluso!!
['fútbol', 'petanca', 'ciclismo', 'patinaje', 'fútbol', 'ajedrez', 'cine', 'baloncesto', 'ciclismo', 'programación',
'ajedrez', 'lectura, 'voley', 'fútbol', 'cine', 'baloncesto', 'balonmano', 'baile', 'parapente',
'fútbol', 'música', 'badminton', 'voley', 'fútbol', 'balonmano', 'lectura', 
'bolos', 'baile', 'baloncesto', 'fútbol', 'balonmano', 'fotografía', 'pesca', 'badminton', 'baloncesto',
'cine', 'balonmano', 'ajedrez', 'parapente', 'lectura', 'voley', 'fútbol', 'baloncesto', 'programación', 'cine']
'''


contador_hobbies = three_most_repaeted_hobbies_v2(people_hobbies)
print(contador_hobbies)
'''
Counter({'fútbol': 7, 'baloncesto': 5, 'cine': 4, 'balonmano': 4, 'ajedrez': 3, 'lectura': 3, 'voley': 3,
'ciclismo': 2, 'programación': 2, 'baile': 2, 'parapente': 2, 'badminton': 2, 'petanca': 1, 'patinaje': 1,
'música': 1, 'bolos': 1, 'fotografía': 1, 'pesca': 1})'''


three_most_repeated = three_most_repaeted_hobbies_v3(people_hobbies)
print(three_most_repeated)
# >>> [('fútbol', 7), ('baloncesto', 5), ('cine', 4)]

three_most_repeated = three_most_repaeted_hobbies_v4(people_hobbies)
print(three_most_repeated)
# >>> [('fútbol', 7), ('baloncesto', 5), ('cine', 4)]
