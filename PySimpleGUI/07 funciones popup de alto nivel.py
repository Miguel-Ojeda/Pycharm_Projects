# Part 1 - The import
import PySimpleGUI as sg

date = sg.popup_get_date()
sg.popup('La fecha elegida es:', date)
print(date)

file_name = sg.popup_get_file('Cuál es el fichero', default_path='c:/windows')
sg.popup('El fichero elegido es:', file_name)

texto = sg.popup_get_text('Escribe algo...')
sg.popup('El texto elegido es', texto)
folder = sg.popup_get_folder('Elige una carpeta...', no_titlebar=True)
sg.popup('La carpeta elegida es:', folder)
