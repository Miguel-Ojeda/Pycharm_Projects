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
texto_resultado = '\n'.join(lista_coincidencias)





pyperclip.copy(texto_resultado)

