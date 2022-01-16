import os
from pathlib import Path

# tenemos un método en pathlib para saber si un path es absoluto o relativo...
# Método is_absolute()
path_relativo = Path('spam/bacon/eggs')
print(path_relativo.is_absolute())  # False

path_home = Path.home()
print(path_home.is_absolute())  # True

path_cwd = Path.cwd()
print(path_cwd.is_absolute())  # True

# Si tenemos un path relativo... cómo podemos obtener el absoluto..
# Sencillo, anteponíendole el path de su directorio padre...
# Por ejemplo, si el path relativo tiene como padre el home, para obtener el path absoluto haríamos
path_absoluto_1 = Path.home() / path_relativo
print(path_absoluto_1)

# Si el path abs lo fuera respecto al cwd, la fórma de obtener el absoluto sería
path_absoluto_2 = Path.cwd() / path_relativo
print(path_absoluto_2)

# También podríamos haberlo hecho directamente, claro...
path_abs = Path.cwd() / Path('spam/bacon/eggs')
print(path_abs)


# Podemos hacer tb cosas con el módulo os.path !!!
# os.path.abspath(relative_path) will return a string of the absolute path
# This is an easy way to convert a relative path into an absolute one.

# os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

# os.path.relpath(path, start) will return a string of a relative path # from the start path to path.
# If start is not provided, the current working directory is used as the start path.

# Ejemplos
# Muestra el path absoluto del cwd
print(os.path.abspath('.'))
# C:\Users\Angel Ojeda\Documents\Miguel\Repos\Pycharm_Projects\ATBS\ch 09 reading and writing files
# Es el directorio donde está este script....

print(os.path.abspath('./spam/eggs/bacon/Extra_de_queso'))
# C:\Users\Angel Ojeda\Documents\Miguel\Repos\Pycharm_Projects\ATBS\
# ch 09 reading and writing files\spam\eggs\bacon\Extra_de_queso

# Hallemos el path relativo de /hola/como/estas/hoy/domingo/Miguel/Angel/Ojeda
# respecto a /hola/como/estas
full_path = '/hola/como/estas/hoy/domingo/Miguel/Angel/Ojeda'
relative_path = os.path.relpath(full_path, start='/hola/como/estas')
print(relative_path)
# ---> hoy\domingo\Miguel\Angel\Ojeda





