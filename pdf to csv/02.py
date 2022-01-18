# Import the required Module
import tabula
from pathlib import Path
import time
import PySimpleGUI as sg
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Elegimos el directorio desde que queremos buscar los PDF
# directorio_base = 'C:/Users/Angel Ojeda/Documents/Miguel/ejemplos de HLC'

# Creamos una ventana para elegir la carpeta donde están los PDFs...

# Pendiente recuperar para poner en Input y en folder el último directorio elegido si existe..
# Si no ponerle ....

layout = [[sg.Text("Elija la carpeta donde está los PDFs")],
          [sg.Input(key='DIRECTORIO', default_text=str(Path.cwd())), sg.FolderBrowse('Explorar')],
          [sg.Text(text_color='red', key='OUTPUT', border_width=2)],
          # Utilizaremos esto para mostrar errores...
          [sg.Button('Aceptar'), sg.Button('Salir')]]

window = sg.Window('PDF a CSV', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Salir'):
        window.close()
        sys.exit()
    # Si llegamos aquí es que apretó el botón  de Aceptar....
    # Leemos el valor elegido...
    directorio_base = values['DIRECTORIO']
    # creamos el objeto path con la elección del usuario
    path_base = Path(directorio_base)
    # path_base = Path(directorio_base).resolve()
    # Si quisiéramos asegurarnos de obtener un path absoluto simplemente añadir el método resolve()
    if path_base.exists():
        # Ya está hecha la elección....
        break
    else:
        # El directorio NO EXISTE!!
        window['OUTPUT'].update('El directorio indicado no existe')

window.close()
logging.debug(f'El directorio elegido ha sido {str(path_base)}')
sys.exit()

# creamos un objeto Path
# path_base = Path(directorio_base)
# if not path_base.exists():
#     input('EL directorio no existe')
#     sys.exit()

# Creamos el subdirectorio para los ficheros CSV
local_time = time.localtime()
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv = path_base / str_time
path_csv.mkdir(exist_ok=True)

# Creamos una nueva ventana para ver el proceso... (no para interactuar)
layout = [[sg.Text("Elija la carpeta donde está los PDFs")],
          [sg.Input(key='DIRECTORIO', default_text=str(Path.cwd())), sg.FolderBrowse('Explorar')],
          [sg.Text(text_color='red', key='OUTPUT', border_width=2)],
          # Utilizaremos esto para mostrar errores...
          [sg.Button('Aceptar'), sg.Button('Salir')]]


for pdf_file in path_base.glob('*.[pP][dD][fD]'):
    # Averiguamos el nombre (sin la extensión) del pdf
    nombre_del_fichero = pdf_file.stem
    # Creamos el objeto path aproopiado para el correspondiente CSV
    csv_file = path_csv / f'{nombre_del_fichero}.csv'
    print(f'Transformando el fichero {nombre_del_fichero} a CSV')
    tabula.convert_into(input_path=pdf_file, output_path=str(csv_file), output_format='csv', pages='all')


