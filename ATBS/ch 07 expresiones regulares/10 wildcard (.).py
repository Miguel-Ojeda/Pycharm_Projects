# El punto hace de comodín....
# representa a cualquier cosa, menos a newline...

import re

at_pattern = re.compile(r'.at')
# Esto es un pattern con 3 caracteres!!! el primer da igual el que sea, el segundo y tercero deben ser 'at'

lista_coincidencias = at_pattern.findall('The cat in the hat sat on the flat mat or at')
print(lista_coincidencias)
#  --> ['cat', 'hat', 'sat', 'lat', 'mat', ' at']
# Observar que también encuenta ' at' porque el primer carácter es espacio, y sería válido...
# no es válido flat porque serían 4 caracteres... así que encuentra 'lat'


# Matching Newlines with the Dot Character
# By passing re.DOTALL as the second argument to re.compile(), you can make
# the dot character match all characters, including the newline character





# Matching cualquier cosa:   .*   (recordar que . es cualquier cosa, y * significa 0 o más repeticiones!!)
# Si queremos buscar una expresión del tipo... First name: <cualquier cosa>Last name: <cualquier cosa>
# Haríamos....

pattern = re.compile(r'First name:(.*)Last name:(.*)')
mo = pattern.search('First name: Al Last name: Sweigart')
if mo:
    print(mo.groups())
# Encuentra la expresión, y los grupos serían --> (' Al ', ' Sweigart')

# Importante, esto actúa en greedy mode... Si queremos el lazy mode, como hemos visto, usar ? ---> (.*?)


