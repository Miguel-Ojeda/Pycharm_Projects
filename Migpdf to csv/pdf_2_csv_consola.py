# Módulos a importar
import tabula
from pathlib import Path
import time
import sys

# Esta es una versión de prueba, ya le digo yo donde están los pdf...
directorio_base = 'C:/Users/Miguel/Downloads/HLC noviembre'
path_base = Path(directorio_base)
if not path_base.exists():
    input('EL directorio no existe')
    sys.exit()

# Creamos el subdirectorio para los ficheros CSV
# en una subcarpeta según fecha y hora del sistema
local_time = time.localtime()
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv = path_base / str_time
path_csv.mkdir(exist_ok=True)
# exist_ok es para si ya existiera el subdirectorio pues que no dé error


for pdf_file in path_base.glob('*.[pP][dD][fF]'):
    # Averiguamos el nombre (sin la extensión) del pdf
    nombre_del_fichero = pdf_file.stem
    # Creamos el objeto path apropiado para el correspondiente CSV
    csv_file = path_csv / f'{nombre_del_fichero}.csv'
    print(f'Transformando el fichero {nombre_del_fichero} a CSV')
    tabula.convert_into(input_path=pdf_file, output_path=str(csv_file),
                        output_format='csv', pages='all', java_options='-Dfile.encoding=UTF8'
                        )
    # Tuve que añadir la opción java_options pq, aunque en el ordenador de casa no había problemas
    # en el trabajo decía que había error no se qué de UTF-8, creo que puede que fuera la configuración JAVA
input('Proceso terminado')
