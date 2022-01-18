# Módulos....

import tabula  # Hace la extracción de datos
from pathlib import Path  # Objetos Path
import PySimpleGUI as sg  # Salida gráfica
import time
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
# Deshabilitado!!
logging.disable(logging.CRITICAL)

# Creamos una ventana para elegir la carpeta donde están los PDFs...
sg.theme('Dark Blue 3')
layout = [[sg.Text("Elija la carpeta donde está los PDFs")],
          # FILA 2: el cuadro de entrada para el directorio, y el botón de explorar...
          [sg.Input(key='DIRECTORIO', default_text=''),
           sg.FolderBrowse('Explorar', initial_folder='')],
          # FILA 3: Utilizaremos esto para mostrar errores...
          [sg.Text(text_color='red', key='OUTPUT_ERROR', border_width=2)],
          # FILA 4: Los botones
          [sg.Button('Aceptar'), sg.Button('Salir')]]

window = sg.Window('PDF a CSV', layout)

# Elegimos el directorio desde donde queremos buscar los PDF
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Salir'):
        window.close()
        sys.exit()
    # Si llegamos aquí es que apretó el botón  de Aceptar
    # Leemos el valor elegido...
    directorio_base = values['DIRECTORIO']
    # Creamos el objeto path con la elección del usuario
    # path_base = Path(directorio_base).resolve() si necesitáramos además que fuera absoluto
    path_base = Path(directorio_base)
    if path_base.exists():
        # Ya está hecha la elección..
        # El método glob nos dará todos los objetos Path que cumplen la condición que le pasamos....
        numero_de_pdfs = len(list(path_base.glob('*.[pP][dD][fF]')))
        if not numero_de_pdfs:
            window['OUTPUT_ERROR'].update('No existe ningún PDF en el directorio')
            continue
        else:
            # Todo_ está bien ahora, tenemos ya nuestro directorio con nuestros PDFS....
            break
    else:
        # El directorio NO EXISTE
        window['OUTPUT_ERROR'].update('El directorio indicado no existe')

window.close()
logging.debug(f'El directorio elegido ha sido {str(path_base)}')
logging.debug(f'Tenemos {numero_de_pdfs} PDFs. para analizar')
# sys.exit()

# Creamos el subdirectorio para los ficheros CSV
# Le añadimos el tiempo actual, para no sobreescribir lo que ya hubiera...
local_time = time.localtime()
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv = path_base / str_time
path_csv.mkdir(exist_ok=True)  # Si existiera, (que es casi imposible pq va por tiempo) pues que no pase nada...

for _, pdf_file in enumerate(path_base.glob('*.[pP][dD][fF]')):
    # Averiguamos el nombre (sin la extensión) del pdf
    nombre_del_fichero = pdf_file.stem
    # Creamos el objeto path apropiado para el correspondiente CSV
    csv_file = path_csv / f'{nombre_del_fichero}.csv'
    # print(f'Transformando el fichero {nombre_del_fichero} a CSV')
    # Mostramos el progreso....
    sg.one_line_progress_meter(f'Procesando {numero_de_pdfs} PDFs...', _ + 1, numero_de_pdfs,
                               f'Procesando fichero {_ + 1} de {numero_de_pdfs} --> {nombre_del_fichero}',
                               key='HLC_METER', orientation='h', no_button=True)
    tabula.convert_into(input_path=pdf_file, output_path=str(csv_file), output_format='csv', pages='all')

window.close()
sg.popup('Proceso terminado')

