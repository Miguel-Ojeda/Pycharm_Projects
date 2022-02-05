import re
import pyperclip

texto_a_buscar = pyperclip.paste()
# print(texto_a_buscar)
# texto_a_buscar = 'sub.info@nostarch.com'

# re_correo = r'\w+@(\w+\.){1,2}[a-zA-Z]{2,4}'
# re_correo = r'\w{4}@w+\.com'
# re_correo = r'info@nostarch\.com'
# re_correo = r'\w+@nostarch\.com'
# re_correo = r'\w+@\w+\.com'
# re_correo = r'\w+@(\w+\.){1,2}[a-zA-Z]{2, 4}'
re_correo = r'((\w+\.){,2}\w+@(\w+\.){1,2}[a-zA-Z]{2,4})'
patron = re.compile(re_correo)

# print(patron.findall('info@nostarch.com'))
# print(patron.search('info@nostarch.com'))
# mo = patron.search('sub.info@nostarch.com')
# print(mo.group())
# mo = patron.search('info@nostarch.com')
# print(mo.group())
# lista_correos = []
#
# print("HOLA")
# lineas = texto_a_buscar.split('\n')
# print(lineas)
# for linea in lineas:
#     coincidencias_linea = patron.findall(linea)
#     for coincidencia in coincidencias_linea:
#         print(coincidencia[0])

coincidencias = patron.findall(texto_a_buscar)
for coincidencia in coincidencias:
    print(coincidencia[0])

# print(lista_correos)
#
# texto_al_portapapeles = '\n'.join(lista_correos)
#
# mo = patron.search('sub.info@nostarch.com')
# print(mo.group())

# pyperclip.copy(texto_al_portapapeles)

