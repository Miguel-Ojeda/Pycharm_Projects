'''
Ask the user to enter integers, separated by spaces.
From this input, create a dict whose keys are the factors for each number,
and the values are lists containing those of the users’ integers that are multiples of those factors.
'''
import pprint
from collections import defaultdict
import math

def get_dict_facts_and_nums():
    entrada = input('Introduzca una serie de números enteros, separados por espacio\n\n\t----> : ')
    campos = entrada.split()
    '''Reuven aprovecha ya para asignar campos... haciendo el split a la vez que el input... ver versión 2'''
    factores = defaultdict(list)
    for numero in campos:
        if not numero.isdecimal():
            continue
        numero = int(numero)
        for i in range(1, numero + 1):
            # creo que es más pythonic if not numero % i:
            # if numero % i == 0:
            if not numero % i:
                factores[i].append(numero)

    return factores

def get_dict_facts_and_nums_v2():
    campos = input('Introduzca números enteros, separados por espacio\n\\t----> : ').split()
    factores = defaultdict(list)
    for numero in campos:
        if not numero.isdecimal():
            continue
        numero = int(numero)
        for i in range(1, numero + 1):
            # creo que es más pythonic if not numero % i:
            # if numero % i == 0:
            if not numero % i:
                factores[i].append(numero)

    return factores


factores = get_dict_facts_and_nums()
pprint.pprint(factores)



