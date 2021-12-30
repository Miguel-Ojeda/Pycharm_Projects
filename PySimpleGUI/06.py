# Part 1 - The import
import PySimpleGUI as sg

# Part 2 - The layout
# Parte 3 creación de la ventana
# Parte 4  Event loop or Window.read call
# Parte 5... destruimos la ventana...
# EN UNA LÍNEA
event, values = sg.Window('WT', [[sg.Text('Whats your name')], [sg.Input()], [sg.Button('Ok')]]).read(close=True)
print('Tu nombre es', values[0])

# otro ejemplo en una línea con short-hand aliases...
event, values = sg.Window('WT', [[sg.T('Whats your name')], [sg.I()], [sg.B('Ok')]]).read(close=True)
print('Tu nombre es', values[0])

# otro ejemplo en una línea con short-hand aliases...  y utilizamos el valor alpha_channel....
event, values = sg.Window('WT', [[sg.B(f'{val}') for val in range (1, 6)]], alpha_channel=0.7).read(close=True)
print ("Haz picado en el número", event)


# otro ejemplo igual, pero además usamos el parámetros no_titlebar y el alpha_channel
layout = [[sg.B(f'{i+5*j}') for i in range(1, 6)] for j in range (0, 6)]
window = sg.Window('', layout, no_titlebar=True, alpha_channel=.9)
event, values = window.read(close=True)

print('Haz clicado en', event)