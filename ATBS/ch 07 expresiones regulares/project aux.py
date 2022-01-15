import re
import pyperclip

texto_a_buscar = pyperclip.paste()

# está mal, porque si no hay código de área NO TIENE QUE HABER SEPARADOR!!!!
re_telefono = r'''(   # Abrimos para crear el grupo que contiene todo... para mostrar en findall
                (\d{3}|\(\d{3}\))?   # el grupo de área es opcional!! puede ser 345 o (345) 
                (\s|\.|-)? # opcional el separador tras el código de área...
                (\d{3}) # primeros 3 dígitos del número
                (\s|\.|-) # obligatorio separador!!!
                (\d{4}) # últimos 4 dígitos del número!!
                (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extensión??? 
                )'''
re_telefono = r'''(   # Abrimos para crear el grupo que contiene todo... para mostrar en findall
                # el grupo de área es opcional, va.. con su separador del resto puede
                # el código de área puede ser  345 o (345) 
                ((\d{3}|\(\d{3}\))(\s|\.|-)?)?   
                (\d{3}) # primeros 3 dígitos del número
                (\s|\.|-) # obligatorio separador!!!
                (\d{4}) # últimos 4 dígitos del número!!
                (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extensión??? 
                )'''

patron = re.compile(re_telefono, re.VERBOSE)

coincidencias = patron.findall(texto_a_buscar)
for coincidencia in coincidencias:
    print(coincidencia[0])
# print(coincidencias)
# lista_coincidencias = [coincidencia[0] for coincidencia in coincidencias]
# texto_resultado = '\n'.join(lista_coincidencias)
# print(texto_resultado)





# pyperclip.copy(texto_resultado)

