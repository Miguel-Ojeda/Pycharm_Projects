"""
It’s sometimes useful to transform data from one format into another.

Download a JSON-formatted list of the 1,000 largest cities in the United States from http://mng.bz/Vgd0.

Using a dict comprehension, turn it into a dict in which the keys are the city names,
and the values are the populations of those cities.

Why are there only 925 key-value pairs in this dict?

Now create a new dict, but set each key to be a tuple containing the state and city.
Does that ensure there will be 1,000 key-value pairs?
"""

import json
import pprint


# Esta versión tiene el fallo de que hay ciudades que, siendo distintas
# tienen el mismo nombre... pero están en distinto estado...
# para corregirlo.... ver v2
def create_dict_city_population(json_file):
    with open(json_file) as cities:
        data = json.load(cities)

    return {datos_ciudad['city']: datos_ciudad['population']
            for datos_ciudad in data
            }

# Esta versión incluye en el diccionario, como clave, la tupla ciudad, estado
# así evita que desaparezcan ciudades... (por ejemplo, oregon maine y oregón de Portland...
def create_dict_city_state_population(json_file):
    with open(json_file) as cities:
        data = json.load(cities)

    return {(datos_ciudad['state'], datos_ciudad['city']): datos_ciudad['population']
            for datos_ciudad in data
            }


# Después de ver la solución de Reuven... lo hace mucho más sencillo pq itera directamente
# sobre el objeto json que se crea al abrir el json....
def create_dict_city_population_v2(json_file):
    return {datos_ciudad['city']: datos_ciudad['population']
            for datos_ciudad in json.load(open(json_file))
            }

def create_dict_city_state_population_v2(json_file):
    return {(datos_ciudad['state'], datos_ciudad['city']): datos_ciudad['population']
            for datos_ciudad in json.load(open(json_file))
            }


cities_data = 'files/cities.json'
resultado = create_dict_city_population(cities_data)
print(resultado)
print(len(resultado))
# >>> 925 ciudades (faltan, pq son 1000)
# Faltan pq hay ciudades distintas con el mismo nombre,
# como Oregón en el estado de Portland y Oregón del estado de Maine

resultado_2 = create_dict_city_state_population(cities_data)
print(resultado_2)
print(len(resultado_2))