import re
import pyperclip

texto_a_buscar = pyperclip.paste()


re_correo = r'((\w+\.){,2}\w+@(\w+\.){1,2}[a-zA-Z]{2,4})'
patron = re.compile(re_correo)

coincidencias = patron.findall(texto_a_buscar)
lista_coincidencias = [coincidencia[0] for coincidencia in coincidencias]
texto_resultado = '\n'.join(lista_coincidencias)





pyperclip.copy(texto_resultado)

