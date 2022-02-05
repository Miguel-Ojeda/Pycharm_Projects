import os
from pathlib import Path

# Para crear un directorio nuevo lo podemos hacer con
# os.makedirs('C:\\delicious\\walnut\\waffles')
# mejor realmente así... -->
# os.makedirs(r'C:\delicious\walnut\waffles')
# es mejor con /, la función se las apaña para hacer lo correcto
# lo mismo sucede con otras funciones, como open etc... que veremos...
os.makedirs(r'C:/delicious/walnut/waffles')



# Tb podemos crear directorio con utilizadedes de pathlib --> método mkdir()
# Aunque sólo puede hacer un directorio cada vez...
# Ejemplo, para hacer el directorio borrar1/borrar2 dentro de home haríamos...
path = Path.home() / 'borrar_1'
print(path)
path.mkdir()
path = path / 'borrar_2'
print(path)
path.mkdir()






