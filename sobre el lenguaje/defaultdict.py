# Es como un diccionario pero mejorado en el sentido de que, al crearlo,
# le decimos que va a tener dentro, y así, de paso, por defecto
# el valor inicial queda fijado...

from collections import defaultdict

# Crea un diccionario donde, por defecto, el valor de cada clave va a ser [] si no hubiera otro...
diccionario1 = defaultdict(list)

diccionario1['profesiones'] = ['cocinero', 'arquitecto']

print(diccionario1['profesiones'])

# Si no existe previamente la clave, a diferencia de los diccioanrios, NO DA ERROR
# Simplemente tendrá el valor por defecto según el tipo de datos...
# en este caso será una lista...
# NO da error, devuelve []
print(diccionario1['comidas'])
# Además, por el hecho de invocar diccioanario1[´comida'] automáticamente se va a
# crear esa entrada con el valor []
print(diccionario1)
# defaultdict(<class 'list'>, {'profesiones': ['cocinero', 'arquitecto'], 'comidas': []})

# Tampoco da error!!
diccionario1['deportes'].append('badminton')
print(diccionario1)
# defaultdict(<class 'list'>, {'profesiones': ['cocinero', 'arquitecto'], 'comidas': [], 'deportes': ['badminton']})


# es muy cómodo... si no fuera por esto, para añadir badminton con un diccionario normal tendríamos que hacer...
dict = {}
if 'deportes' in dict:
    dict['deportes'].append('badminton')
else:
    dict['deportes'] = ['badminton']

# o...
if dict.get('deportes'):
    dict['deportes'].append('badminton')
else:
    dict['deportes'] = ['badminton']

# o...
valor_anterior = dict.get('deportes', [])
dict['deportes'] = valor_anterior.append('badminton')










