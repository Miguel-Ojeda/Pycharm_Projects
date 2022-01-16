import os
from pathlib import Path

# Para crear un directorio nuevo lo podemos hacer con
# os.makedirs('C:\\delicious\\walnut\\waffles')

# Pero es mucho mejor hacer con Path... método mkdir()
# Aunque sólo puede hacer un directorio cada vez...
# Ejemplo, para hacer el directorio borrar1/borrar2 dentro de home haríamos...
path = Path.home() / 'borrar_1'
print(path)
path.mkdir()
path = path / 'borrar_2'
print(path)
path.mkdir()

