# Import the required Module
import tabula
from pathlib import Path
import time
import PySimpleGUI as sg
import sys

# Elegimos el directorio desde que queremos buscar los PDF
# directorio_base = 'C:/Users/Angel Ojeda/Documents/Miguel/ejemplos de HLC'

layout = [[sg.Text("Elija la carpeta donde está los PDFs")],     # Part 2 - The Layout
          [sg.Input(key='-INPUT-'), sg.FolderBrowse('Explorar')],
          [sg.Button('Aceptar'), sg.Button('Salir')]]

# Create the window
window = sg.Window('PDF a CSV', layout)

# Display and interact with the Window using an Event Loop
while True:
    print('Leyendo')
    event, values = window.read()
    print('Termino de leer...')
    print('Evento', event)
    print('Values', values)
    # # See if user wants to quit or window was closed
    # if event == sg.WINDOW_CLOSED or event == 'Quit':
    #     break
    # # Output a message to the window
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
sys.exit()

while True:
    directorio_base = sg.popup_get_folder(message='Elige la carpeta donde están los PDFs...',
                                          title='Tablas PDF -> CSV',
                                          default_path='',  # lo que se muestra relleno en el campo de texto
                                          no_titlebar=False,
                                          grab_anywhere=True,
                                          keep_on_top=True,
                                          initial_folder='',  # lo que aparece al darle al browse
                                          )
    # si el usuario ha cancelado y no ha eligido nada, pues que repita...
    if not directorio_base:
        sg.popup('Cancelando la ejecución del programa')
        sys.exit()
    else:
        # creamos el objeto path con la elección del usuario
        path_base = Path(directorio_base)
        if path_base.exists():
            break
        else:
            # El directorio NO EXISTE!!
            sg.popup_error('El directorio NO EXISTE... ELija un directorio válido')



#
# # creamos un objeto Path
# # path_base = Path(directorio_base)
# # if not path_base.exists():
# #     input('EL directorio no existe')
# #     sys.exit()
#
# # Creamos el subdirectorio para los ficheros CSV
# local_time = time.localtime()
# str_time = time.strftime('%y%m%d-%H%M%S')
# path_csv = path_base / str_time
# path_csv.mkdir(exist_ok=True)
#
# for pdf_file in path_base.glob('*.[pP][dD][fD]'):
#     # Averiguamos el nombre (sin la extensión) del pdf
#     nombre_del_fichero = pdf_file.stem
#     # Creamos el objeto path aproopiado para el correspondiente CSV
#     csv_file = path_csv / f'{nombre_del_fichero}.csv'
#     print(f'Transformando el fichero {nombre_del_fichero} a CSV')
#     tabula.convert_into(input_path=pdf_file, output_path=str(csv_file), output_format='csv', pages='all')
#
#
