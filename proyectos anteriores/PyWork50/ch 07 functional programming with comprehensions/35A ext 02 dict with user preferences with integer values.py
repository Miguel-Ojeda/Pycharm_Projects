"""
Create a dict based on the config file, as in the previous exercise, but this time,
all of the values should be integers.

This means that you’ll need to filter out (and ignore) those values that can’t be turned into integers
"""
# Para hacerlo partimos del ejercicio antesrior, 35A ext 01
'''
def dict_from_config_file_v1(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.split('=')[0]: linea.split('=', maxsplit=1)[1].strip()
                for linea in config
                if not linea.startswith('#')
                if not linea.isspace()}
'''

import pprint


# Vamos a coger el fichero fácil, supondremos inicialmente que no hay
# que hacer comprobaciones para detectar comentarios, ni líneas vacías, etc..
def dict_from_config_file_with_integer_values(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.split('=')[0]: int(linea.split('=')[1].strip())
                for linea in config
                if linea.split('=')[1].strip().isdigit()
                # if not linea.startswith('#')
                # if not linea.isspace()}
                }


# Es lo mismo, pero admite comentarios y que haya listas vacías, o con varios igual, etc...
def dict_from_config_file_with_integer_values_v2(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.split('=')[0]: int(linea.split('=', maxsplit=1)[1].strip())
                for linea in config
                if not linea.startswith('#')
                if not linea.isspace()
                if linea.split('=', maxsplit=1)[1].strip().isdigit()
                }


config_file = 'files/para 32 ext 03.txt'
resultado = dict_from_config_file_with_integer_values_v2(config_file)
pprint.pprint(resultado)



from io import StringIO

frase = StringIO('''# Esto se puede ignorar, todo_ lo que empiece con #
# Si está vacío pues también...

color='red'
resolution=1024
so=windows
ip=10.24.12.12
Ahora otra vacía pero con varios espacios...

DNS=9.9.9.9
user=mojeaco''')