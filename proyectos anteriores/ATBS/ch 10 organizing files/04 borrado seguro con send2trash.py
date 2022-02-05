# send2trash es mucho más seguro (y rápido) que el borrado con los otros métodos...
# Realmente lo que hace es mandar los ficheros a la papelera de reciclaje!!!
# desde donde podremos, si lo necesitamos, volver a recuperar!!

from pathlib import Path
import send2trash

# creamos un nuevo fichero en el home
path_file = Path.home() / 'bacon.txt'
with open(path_file, 'w') as file:
    file.write('Primera línea\n')
    file.write('Segunda línea, ')
    file.write('que continúa aquí')

# Ahora vamos a comprobar que existe... y leer todo_ su contenido...
with open(path_file) as file:
    contenido = file.read()     # Leemos todo_ a lo bestia...
print(f'El contenido de {str(path_file)} es:')
print(contenido)

# Ahora lo borramos, enviandolo a la papelera...
send2trash.send2trash(path_file)

# Ahora intentamos otra vez leerlo...
try:
    with open(path_file) as file:
        contenido = file.read()     # Leemos todo_ a lo bestia...
    print(f'El contenido de {str(path_file)} es:')
    print(contenido)
except:
    print('El fichero no se ha podido leer...')