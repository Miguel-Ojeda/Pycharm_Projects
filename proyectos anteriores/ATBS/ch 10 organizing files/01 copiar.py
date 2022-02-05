import shutil
from pathlib import Path
# El módulo shutil (shell utilities) proporciona funciones para copiar
# cambiar el nombre, mover, ficheros carpetas...
# Con shutil podemos usar Paths o tb. strings simplemente!!!

# El módulo shutil tiene, además de las que veremos, muchísimas funciones más!!
# por ejemplo make_archive para crear zips, etc...


# 1 shutil.copy(origen, destino)   -> sirve para copiar ficheros
# El origen y destino pueden ser strings o objetos Path...
# La función devuelve el path al fichero creado...
'''
obs que hay una función copy2 que copia los datos y tb. los metadatos...
Tenemos dos posibildiades...
a) si el destino es una carpeta (existe ya), se copiará el fichero a esa carpeta, manteniendo el nombre
b) si el destino no es una carpeta (o sea, no existe), pues será el nuevo nombre para el fichero
'''
# Ejemplo 1... supongamos que existe un fichero spam.txt en home....
# y tb. existe una subcarpeta en home que se llama something
'''
path = Path.home()
shutil.copy(path / 'spam.txt', path / 'something')
Pues lo que hace es copiar spam.txt a la carpeta 'something'
'''

# Ejemplo 2.... ahora resulta que no existe la carpeta 'something'
# entonces interpretará que el destino es el nombre que queremos para la copia....
'''
path = Path.home()
shutil.copy(path / 'spam.txt', path / 'something')
Pues lo que hace es copiar spam.txt  y crearlo como nuevo fichero 'some folder'
'''

# 2 shutil.copytree(path_source, path_destination)
# COpia la carpeta (con todo_ su contenido, subcarpetas....) al destino propuesto...
# O sea, sirve para hacer backups, por ejemplo...
# La función devuelve el Path a la carpeta destino
'''
p = Path.home()
shutil.copytree(p / 'spam', p / 'spam_backup')
'''
