"""
Find a configuration file in which the lines look like “name=value.”
Use a dict comprehension to read from the file, turning each line into a key-value pair.
"""
import pprint


def dict_from_config_file_v0(config_file):
    with open(config_file, encoding='utf-8') as config:
        return {linea.strip().split('=', maxsplit=1)[0]: linea.strip().split('=', maxsplit=1)[1]
                for linea in config
                if not linea.startswith('#')
                if not linea.isspace()}



config_file = 'files/para 32 ext 03.txt'
resultado = dict_from_config_file_v0(config_file)
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


