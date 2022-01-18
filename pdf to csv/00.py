# Import the required Module
import tabula
from pathlib import Path
import time
import sys

# Elegimos el directorio desde que queremos buscar los PDF
directorio_base = 'C:/Users/Miguel/Downloads/HLC noviembre'

# creamos un objeto Path
path_base = Path(directorio_base)
if not path_base.exists():
    input('EL directorio no existe')
    sys.exit()

# Creamos el subdirectorio para los ficheros CSV
local_time = time.localtime()
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv = path_base / str_time
path_csv.mkdir(exist_ok=True)

for pdf_file in path_base.glob('*.[pP][dD][fF]'):
    # Averiguamos el nombre (sin la extensión) del pdf
    nombre_del_fichero = pdf_file.stem
    # Creamos el objeto path apropiado para el correspondiente CSV
    csv_file = path_csv / f'{nombre_del_fichero}.csv'
    print(f'Transformando el fichero {nombre_del_fichero} a CSV')
    tabula.convert_into(input_path=pdf_file, output_path=str(csv_file), output_format='csv', pages='all')

input('Proceso terminado')