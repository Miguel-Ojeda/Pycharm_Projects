import pathlib
from pathlib import Path
# Veamos atributos de un objeto Path que me sirven para obtener las partes de un path...
r'''
Las partes de un path son

EN WINDOWS Ejemplo con C:\\Users\Al\spam.txt

1) Anchor (es el root) --> C:\
a) Drive es una parte de Anchor, que nos da la unidad.
En este caso sería C:, o sea, lo mismo pero sin el \ final !!!

2) Parent: es el la ruta completa del directorio que contiene al fichero
Parent sería C:\Users\Al\

3) Name --> spam.txt
a) Stem --> spam
b) Suffix... es la extensión, incluye dot --> .txt  (INCLUYE EL PUNTO!!!)


EN UNIX, ejemplo con /home/al/spam.txt
Es igual, pero no hay drive y además el Anchor es más sencillo, simplemente
'''

# Podemos acceder directamente a estos atributos de nuestors objetos path...
# Observar que todos estos atributos van a ser cadenas, excepto el atributo parent
# Ejemplo
path = Path('C:/Users/Al/spam.txt')
print('Anchor:', path.anchor)  # C:\
# Esto lo hago pq estoy en Windows... si no no sé si daría error!!
print('Drive:', path.drive)  # C:
print('Parent .. es un objeto Path, no una cadena:', repr(path.parent))  # WindowsPath('C:/Users/Al')
print('Name:', path.name)   # spam.txt
print('Stem: ', path.stem)  # spam
print('Sufjio o extensión:', path.suffix)   # .txt   CUIDADO, incluye el punto!!!


# path.parent hemos visto que es un objeto pathlib.Path con el path del padre
# En cambio path.parents, nos da un objeto iterable con todos los ancestros (padres)
# desde el actual, hasta el raíz...
print('Imprimiendo los items del objeto "path.parents":')
for parte in path.parents:
    print(parte)
# C:\Users\Al
# C:\Users
# C:\

# También se puede hacer algo similar con el campo parts ... nos devuelve una tupla!!!
# con todos los elementos separados que forman el path completo del fichero
partes = path.parts
print('Imprimiendo el la tupla "path.parts"')
for parte in partes:
    print(parte)
# C:\
# Users
# Al
# spam.txt


# ------------------------------------------------
# También se puede hacer con el módulo os, aunque está nmás limitado...
# Trabaja y devuelve cadenas... como hemos visto
import os

calc_path = 'C:/Windows/System32/calc.exe'
# Obtengamos el nombre del fichero y el directorio
print('Utilizando os.path para obtener datos de una cadena con el path de un fichero...')
print('Fichero', calc_path)
name = os.path.basename(calc_path)
print('Name con os.path:', name)
directorio = os.path.dirname(calc_path)
print('EL directorio, con os.path, es:', directorio)
# Si queremos tener una tupla con ambos elementos de forma rápida utilziamos os.path.split()
tupla_parent_name = os.path.split(calc_path)
print(tupla_parent_name)
# ('C:/Windows/System32', 'calc.exe')
# Si queremos obtener todo_ separadito es muy fácil....
# Usar el método split de cadenas, utilziando como separador os.sep
partes_separadas = calc_path.split('/')
print(partes_separadas)
# aunque esto nos quitaría el símbolo /, claro, por eso es mucho mejor utilizar pathlib...
# ['C:', 'Windows', 'System32', 'calc.exe']

# Para hacer lo mismo con el método moderno sería...
print('Ahora hacemos lo mismo con pathlib')
path = Path('C:/Windows/System32/calc.exe')
print('Directorio:', path.parent)
print('Nombre de fichero', path.name)
# La tupla, por supuesto, es inmediato aquí...
# Para impimir las partes separadas, es facilísimo... como hemos visto
for parte in path.parts:
    print(parte)


