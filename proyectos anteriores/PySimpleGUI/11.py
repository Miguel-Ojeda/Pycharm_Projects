import PySimpleGUI as sg

# opción disable_close!! y button_color....
choice, val = sg.Window('Continue?', [[sg.T('______ Do you want to continue?_____')], [sg.Yes(s=10), sg.No(s=10)]],
                        disable_close=True,
                        button_color=('white', 'green'),
                        background_color='black').read(close=True)
