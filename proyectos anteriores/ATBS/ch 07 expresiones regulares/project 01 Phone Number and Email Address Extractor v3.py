import re
import pyperclip

texto_a_buscar = pyperclip.paste()


re_correo = r'''(           # Aquí creamos el grupo que engloba a todo, para luego pillarlo en el findall
            (\w+\.){,2}     # Dejamos que pueda haber expresiones tipo info.  juan.miguel.  ... antes de la arroba
            \w+@            # texto que va antes de la arroba
            (\w+\.){1,2}    # subdominios después de la arroba... como mucho ponemos 2...
            [a-zA-Z]{2,4}   # texto final con la terminación del dominio, pongo de 2 a 4 caracteres alfabéticos...
            )'''
patron = re.compile(re_correo, re.VERBOSE)
coincidencias = patron.findall(texto_a_buscar)
lista_coincidencias = [coincidencia[0] for coincidencia in coincidencias]
texto_resultado_correo = '\n'.join(lista_coincidencias)


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
lista_coincidencias = [coincidencia[0] for coincidencia in coincidencias]
texto_resultado_telefono = '\n'.join(lista_coincidencias)

texto_resultado_total = '\n'.join(['Correos encontrados:', texto_resultado_correo, '\n',
                                   'Teléfonos encontrados:', texto_resultado_telefono])


pyperclip.copy(texto_resultado_total)

