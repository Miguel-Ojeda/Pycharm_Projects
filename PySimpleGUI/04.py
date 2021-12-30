# Part 1 - The import
import PySimpleGUI as sg

# Part 2 - The layout
# usando list comprehension....
layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]

# Parte 3 creación de la ventana
window = sg.Window('Título de la ventana', layout)

# Parte 4  Event loop or Window.read call
event, values = window.read(close=True)   # esto hace que nada más leer y retornar un valor, se cierre
# Parte 5... destruimos la ventana...
# window.close()

print(event, values)

event, values = sg.Window('WT', [[sg.Text('Whats your name')], [sg.Input()], [sg.Button('Ok')]]).read(close=True)

print('Tu nombre es', values[0])



