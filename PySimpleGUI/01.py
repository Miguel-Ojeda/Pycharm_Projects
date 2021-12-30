# Part 1 - The import
import PySimpleGUI as sg

# Part 2 - The layout
layout = [[sg.Text('Un poco de texto')],
          [sg.Input()],
          [sg.Button('Ok')]]

# Parte 3 creación de la ventana
window = sg.Window('Título de la ventana', layout)

# Parte 4  Event loop or Window.read call
event, values = window.read()

print('Hello', values[0], "! Thanks for trying PySimpleGUI")


# Parte 5... destruimos la ventana...
window.close()

# otro ejemplo parte 2
layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.OK(), sg.Cancel()]]   # aquí creamos ya unos botones predefinidos, los botones Ok y Canceñ

# Create the Window parte 3
window = sg.Window('Window Title', layout)
# Parte 4  Event loop or Window.read call
event, values = window.read(close=True)  # Aquí incluso hacemos que al retornar de la lectura se cierre sola la ventana
print(event)  # en este caso el botón OK o el botón Cancel
print(values[0])
# window.close() no necesaria la parte 5 pq autocerramos....







