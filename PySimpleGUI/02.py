# Part 1 - The import
import PySimpleGUI as sg

# Part 2 - The layout
layout = [[sg.Text("What's your name")],
          [sg.Input(key='INPUT')],
          [sg.Text(key='OUTPUT', size=(40, 1))],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Parte 3 creación de la ventana
window = sg.Window('Título de la ventana', layout)

# Parte 4  Event loop or Window.read call
while True:
    event, values = window.read()
    # el usuario quiere salir???
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    window['OUTPUT'].update('Hello ' + values['INPUT'] + "! Thanks for trying PySimpleGUI", text_color='yellow')

print(event)

# Parte 5... destruimos la ventana...
window.close()






