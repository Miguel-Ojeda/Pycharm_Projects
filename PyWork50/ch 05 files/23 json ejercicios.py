"""
Observar que el contenido de los json es como una lista de diccioanrios
[{"math" : 90, "literature" : 98, "science" : 97},
 {"math" : 65, "literature" : 79, "science" : 85},
 {"math" : 78, "literature" : 83, "science" : 75},
 {"math" : 92, "literature" : 78, "science" : 85},
 {"math" : 100, "literature" : 80, "science" : 90}
]
"""
'''
Utilizaremos the json.load method reads a JSON-encoded string from a
file and returns a combination of Python objects

Existe tb el método loads que lee los datos directamente desde una string..

Deserialize fp (a .read()-supporting text file or binary file containing
a JSON document) to a Python object using this conversion table.

O sea, traduciendo... pasa el contenido de ficheros (o de strings en el caso del método loads)
a estructuras de datos, a objetos...

Por tanto, json.load y json.loads sirve para recuperar datos almacenados en este formato
y ponerlos en un objeto....

En el caso de este fichero, producirá una lista de diccionarios....
'''

import pprint
import json
from pathlib import Path


# Esta es la versión inicial... no está mal pero la versión 2 ocupa menos de la mitad...
def extract_scores_1(json_file):
    with open(json_file) as file:
        notas_clase = json.load(file)
    notas_mates = []
    notas_literatura = []
    notas_ciencias = []
    for notas_estudiante in notas_clase:
        notas_mates.append(notas_estudiante['math'])
        notas_literatura.append(notas_estudiante['literature'])
        notas_ciencias.append(notas_estudiante['science'])
    max_mates = max(notas_mates)
    min_mates = min(notas_mates)
    media_mates = sum(notas_mates) / len(notas_mates)

    max_literatura = max(notas_literatura)
    min_literatura = min(notas_literatura)
    media_literatura = sum(notas_literatura) / len(notas_literatura)

    max_ciencias = max(notas_ciencias)
    min_ciencias = min(notas_ciencias)
    media_ciencias = sum(notas_ciencias) / len(notas_ciencias)

    print(f'{json_file}:')
    print(f'\tCiencias: min {min_ciencias}, máx {max_ciencias}, media {media_ciencias}')
    print(f'\tLiteratura: min {min_literatura}, máx {max_literatura}, media {media_literatura}')
    print(f'\tMatemáticas: min {min_mates}, máx {max_mates}, media {media_mates}')


def extract_scores_2(json_file):
    """
    La solución de Reuven es mucho mejor, guarda las notas de cada materia
    no en tres listas separadas, sino en un diccionario...
    El código es mucho mejor!! Esta es una adaptación mía a lo de Reuven...
    Pasamos de 23 filas de las versión anterior, a 11 filas!!
    Además es mejor, pq guardamos todas las notas en un solo objeto (antes eran 3 listas)
    """
    with open(json_file) as file:
        notas_clase = json.load(file)
    notas = {'math': [], 'literature': [], 'science': []}

    for notas_estudiante in notas_clase:
        for subject, score in notas_estudiante.items():
            notas[subject].append(score)

    # pprint.pprint(notas)
    # Mostramos los resultados
    print(json_file)  # --> simplemente para identificar el fichero (clase)
    for subject in notas:
        print(f'\t{subject.capitalize()}: mín {min(notas[subject])},',
              f'max {max(notas[subject])}, media: {sum(notas[subject]) / len(notas[subject])}')


'''
    El resultado de lo anterior sería, con el fichero de ejemplo...
    json-files\9a.json
        Math: mín 65, max 100, media: 85.0
        Literature: mín 78, max 98, media: 83.6
        Science: mín 75, max 97, media: 86.4
'''


def extract_scores_folder(directorio):
    directorio = Path(directorio)
    for file_name in directorio.glob('*.json'):
        # extract_scores(file_name)
        extract_scores_2(file_name)


json_file = 'json-files/9a.json'
json_directorio = 'json-files'
# extract_scores_1(json_file)
# extract_scores_2(json_file)

extract_scores_folder(json_directorio)
