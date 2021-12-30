# Part 1 - The import
import PySimpleGUI

# Part 2 - The layout
layout = [[PySimpleGUI.Text('Un poco de texto')],
          [PySimpleGUI.Input()],
          [PySimpleGUI.Button('Ok')]]

# Parte 3 creación de la ventana
window = PySimpleGUI.Window('Título de la ventana', layout)

# Parte 4  Event loop or Window.read call
event, values = window.read()

print('Hello', values[0], "! Thanks for trying PySimpleGUI")


# Parte 5... destruimos la ventana...
window.close()






