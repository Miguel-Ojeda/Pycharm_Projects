"""
Many programs’ functionality is modified via configuration files, which are often set using name-value pairs.
That is, each line of the file contains text in the form of name=value,
where the = sign separates the name from the value.

I’ve prepared one such sample config file at http://mng.bz/rryD.

Download this file, and then use a dict comprehension to read its contents from disk, turning it into
a dict describing a user’s preferences. Note that all of the values will be strings.
"""

# OBSERVAR, ya lo había hecho, en el ejercicio 32 ext 03 config to dict.... se equivocó y lo duplicó!!!


import pprint


def dict_from_config_file_v0(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.strip().split('=', maxsplit=1)[0]: linea.strip().split('=', maxsplit=1)[1]
                for linea in config
                if not linea.startswith('#')
                if not linea.isspace()}


# Mejoro un poco después de ver cómo lo hace Reuven
def dict_from_config_file_v1(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.split('=')[0]: linea.split('=', maxsplit=1)[1].strip()
                for linea in config
                if not linea.startswith('#')
                if not linea.isspace()}


config_file = 'files/para 32 ext 03.txt'
resultado = dict_from_config_file_v0(config_file)
pprint.pprint(resultado)

resultado = dict_from_config_file_v1(config_file)
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