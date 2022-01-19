import zipfile
import os
from pathlib import Path
'''
Para usar el módulo zipfile lo primero es crear un ZipFile Object con...zipfile.ZipFile()
Luego podremos usar métodos para hacer cosas como extraer...
zip_file = zipfile.ZipFile(fichero --> puede ser str, path
                            modo --> puede ser r (lectura), w (escritura), a (append), x (exclusive create)
                            y más parámetros....)
                            
                            IMPORTANTE: como con los ficheros, hay tb. que hacer al final un close!!!
'''
# Veamos el uso con un zip de ejemplo. ... example.zip
# Creamos el Zip Object
path = 'example.zip'
zip_file = zipfile.ZipFile(path)
# o tb. path = Path.home() / .....

# AHora podemos extraer info con los métodos namelist(), getinfo(),
print(f'Los contenidos del ZIP son:')
for file in zip_file.namelist():
    print(file, type(file))  # son cadenas lo que retorna!!!
# Los contenidos del ZIP son:
# spam.txt <class 'str'>
# cats/ <class 'str'>
# cats/catnames.txt <class 'str'>
# cats/zophie.jpg <class 'str'>

# Vamos ahora a extraer info sobre el primer elemento devuelto....
primer_fichero = zip_file.namelist()[0]
print(f'Extrayendo información del primer elemento del ZIP --> {primer_fichero}')
zip_file_info = zip_file.getinfo(primer_fichero)
# Lo que devuelve es un objeto ZipInfo, que tiene algunos atributos que podemos consultar...
print(f'El tamaño original del fichero es {zip_file_info.file_size},'
      f'el tamaño comprimido {zip_file_info.compress_size}',
      f'y el ratio es de {round(100 * zip_file_info.compress_size/zip_file_info.file_size)} %')

# También podemos obtener una lista con todos los zip_file de todos los ficheros que contiene
for zip_file_info in zip_file.infolist():
    print('Fichero ->', zip_file_info.filename,
          'Tamaño original ->', zip_file_info.file_size,
          'Tamaño comprimido ->', zip_file_info.compress_size)

zip_file.close()

# ------------------------- U S A R   M E J O R     E L     W I T H ------------------------

# Mejor, como siempre, usar el with... así evitamos dejar cosas abiertas si olvidamos o ocurre alguna excepción
# Veamos como hacer la extracción, ahora, USANDO WITH!!!!
path = 'example.zip'
with zipfile.ZipFile(path) as zip_object:
    zip_object.extractall()
# Podemos dar un montón de parámetros... cosas que queremos descomprimir, directorio para descomprimir... etc

# También hay métodos para extraer algunos ficheros....
# zip_object.extract(....)

# También podemos crear nuevos objetos zip para añadirle luego cosas...
# Para ello, al crear el objeto zip hacerlo, como con ficheros, en modo 'w'
# Creemos el ZIP para meter dentro todo_ el directorio ejemplo_os.walk
path = Path.cwd() / 'ejemplo_os.walk'

# Creamos un nuevo objeto zip, que va a llamarse ejemplo....zip ... en modo w
zip_object = zipfile.ZipFile('ejemplo_os.walk.MAL.zip', 'w')
for folder, folders_list, files_list in os.walk(path):
    for file in files_list:
        # File es tan solo la cadena con el nombre (sin la ruta) del fichero..
        # Habrá que obtener el path para poder agregarlo al zip
        path_file = Path(folder) / file
        zip_object.write(path_file, compress_type=zipfile.ZIP_DEFLATED)
        print(f'Añadiendo el fichero {str(path_file)}')

zip_object.close()   # Cuidado, no olvidar!! mejor con with....!!!

# Cuidado, lo anterior no funciona bien... porque, aunque mete los ficheros correctos...
# pero crea toda la estructura desde C: !!!!
# El fallo está en que estamos metiendo en el ZIP toda la ruta!!!
# Habría que meter los objetos con un path RELATIVO!!!
# Por eso lo modifico ahora otra vez...
zip_object = zipfile.ZipFile('ejemplo_os.walk.BIEN.zip', 'w')
for folder, folders_list, files_list in os.walk(path):
    for file in files_list:
        # File es tan solo la cadena con el nombre (sin la ruta) del fichero..
        # Habrá que obtener el path para poder agregarlo al zip
        path_file = Path(folder) / file
        path_file_relative = path_file.relative_to(Path.cwd())
        zip_object.write(path_file_relative, compress_type=zipfile.ZIP_DEFLATED)
        print(f'Añadiendo el fichero {str(path_file_relative)}')

zip_object.close()   # Cuidado, no olvidar!! mejor con with....!!!

# ESTO YA ES OTRA COSA!!!!


# Si queremos añadir ficheros a un ZIP ya existente... lo haríamos
# abriendo un objeto ZIP en modo 'a' (si lo abriéramos en modo 'w' nos lo cargaríamos!!!)