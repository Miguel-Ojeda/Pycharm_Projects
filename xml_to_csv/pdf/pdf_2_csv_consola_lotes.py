# Import the required Module
import tabula
from pathlib import Path
import time
import sys

# Esta es una versión de prueba, ya le digo yo donde están los pdf...
directorio_base = 'C:/Users/Miguel/Downloads/HLC noviembre'
path_base = Path(directorio_base)

# Esta versión es como la anterior pero más corta pq utilizamos
# una función de tabula que busca los pdfs de todo el directorio
# Los CSV se crean en el mismo directorio, mezclados!!!

print(f'Procesando el directorio {str(path_base)}')
tabula.convert_into_by_batch(input_dir=str(path_base), output_format='csv',
                             pages='all', java_options='-Dfile.encoding=UTF8')
# Tuve que añadir la opción java_options pq, aunque en el ordenador de casa no había problemas
# en el trabajo decía que había error no se qué de UTF-8, creo que puede que fuera la configuración JAVA

input('Proceso terminado')
