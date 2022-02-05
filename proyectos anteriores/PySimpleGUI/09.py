import PySimpleGUI as sg
print = sg.Print   # si quisiéramos que los print los dibujara SimpleGUI

sg.theme('Dark Blue 3')  # personalizamos con un tema

# 2
layout = [[sg.Text('File name')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]


# 3
window = sg.Window('Title', layout, alpha_channel=0.8)
# 4
event, values = window.read()

print(event)
print("El fichero es: ", values[0])

# 5
window.close()

# Otro ejemplo
event, values = sg.Window('Title', [[sg.ColorChooserButton('Elige un color')], [sg.OK(), sg.Cancel()]]).read()

print(event, values)
