# Manejo del portapapeles...
import pyperclip

# pyperclip.copy('Esto irá al portapapeles')
esto_cogera_lo_que_hay_en_el_portapapeles = pyperclip.paste()
print(esto_cogera_lo_que_hay_en_el_portapapeles)
lineas = esto_cogera_lo_que_hay_en_el_portapapeles.split('\n')
for index, linea in enumerate(lineas):
    print(f'Línea {index}: {linea}')