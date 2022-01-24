# Módulos....
import tabula  # Hace la extracción de datos utilizando tabula Java
from pathlib import Path  # Objetos Path
import PySimpleGUI as sg  # Salida gráfica
import time
import sys
import logging
import pandas as pd         # Pandas para manejar dataframes
# Para pasar a excel hace falta tener instalado también el módulo openpyxl
# import openpyxl

# Auxiliares...
from get_clean_hlc_df import get_clean_hlc_df

# Opciones para ver mejor los dataframes al imprimir en pantalla para ver los datos...
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)  # hay 14 columnas en HLC!!

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
    # Si llegamos aquí es que apretó el botón de Aceptar
    # Leemos el valor elegido...
    directorio_base = values['DIRECTORIO']
    # Creamos el objeto path con la elección del usuario
    # path_base = Path(directorio_base).resolve() si necesitáramos además que fuera absoluto
    path_base = Path(directorio_base)
    if path_base.exists():
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

# Creamos el subdirectorio para los ficheros CSV, basándonos en la fecha y hora actual
# local_time = time.localtime()
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv = path_base / str_time
path_csv.mkdir(exist_ok=True)

# Vamos a almacenar los datos de cada centro en una lista de data_frames, para luego poder combinarlos
lista_datos_centros = []

for _, pdf_file in enumerate(path_base.glob('*.[pP][dD][fF]')):
    # Averiguamos el nombre (sin la extensión) del pdf
    nombre_del_fichero = pdf_file.stem
    csv_file = path_csv / f'{nombre_del_fichero}.csv'
    # Mostramos el progreso....
    sg.one_line_progress_meter(f'Procesando {numero_de_pdfs} PDFs...', _ + 1, numero_de_pdfs,
                               f'Procesando fichero {_ + 1} de {numero_de_pdfs} --> {nombre_del_fichero}',
                               key='HLC_METER', orientation='h', no_button=True)

    # Obtenemos el listado de dataframes con los datos de cada tabla encontrada
    # en nuestro caso, habrá una tabla por página con datos de HLC
    lista_df = tabula.read_pdf(input_path=pdf_file, pages='all')
    # Igual hace falta añadir java_options='-Dfile.encoding=UTF8' a la llamada ...
    # a mí me sirve sin ponerlo, debería ser el defecto...
    # lista_df = tabula.read_pdf(input_path=pdf_file, pages='all', java_options='-Dfile.encoding=UTF8')

    # Habría que pasar a la función get_clean.-... el centro y las observaciones detectadas...
    # datos_centro va a ser el data frame con los datos ya arreglados...
    # de momento le pasamos como centro el nombre del fichero, y nada en observations
    datos_centro = get_clean_hlc_df(lista_df, centro=nombre_del_fichero, observaciones=None)
    datos_centro.to_csv(csv_file, header=False, index=False)

    # Añadimos los datos de cada centro al listado
    lista_datos_centros.append(datos_centro)

# Ahora nos queda combinar los datos de todos los centros y crear el csv...
datos_todos_centros = pd.concat(lista_datos_centros)
datos_todos_centros.to_csv(path_csv / 'todos_los_centros.csv', header=False, index=False)
# Para pasar a excel hace falta tener instalado también el módulo openpyxl
datos_todos_centros.to_excel(path_csv / 'todos_los_centros.xlsx', sheet_name='HLC', header=False, index=False)

# with pd.ExcelWriter(path_csv / 'todos_los_centros.xlsx') as writer:
#     datos_todos_centros.to_excel(writer, sheet_name='HLC', header=False, index=False)

'''
La llamada original que hacíamos... ahora cogemos los dataframes y analizamos los datos
tabula.convert_into(input_path=pdf_file, output_path=str(csv_file),
                    output_format='csv', pages='all', java_options='-Dfile.encoding=UTF8')
'''

window.close()
sg.popup('Proceso terminado')
