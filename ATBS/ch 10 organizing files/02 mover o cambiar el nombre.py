import shutil

# shutil.move(fichero_origen, destino)

# Si destino es una carpeta existente... puede nos mueve el fichero a esa carpeta, conservando su nombre...
# Cuidado, pq si ya hubiera un fichero con ese nombre en la carpeta destino, pues lo sobreescribiría!!!
# Si el destino es un nombre de fichero, pues realmente lo que hace sería cambiar el nombre, claro...
# La función devuelve un string a la ubicación final del fichero...

# Ejemplos...
'''
shutil.move('C:/bacon.txt', 'C:/eggs')
a) Si existe la carpeta C:/eggs, pues nos mueve bacon.txt a esa carpeta
b) Si no existe la carpeta C:/eggs, pues interpreta que eggs va a ser el nuevo nombre del fichero!!!
---------------------------------------
Cuidado, si ponemos algo como
shutil.move('C:/bacon.txt', 'C:/eggs2/bacon.txt')
Si el directorio eggs2 no existiera, pues se crearía una excepción FileNotFoundError !!
'''
