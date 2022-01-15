# Cogeremos el texto del portapapeles
# volveremos a dejar en el portapapeles todo_ el texto pero con los DNI enmascarados....
import re
import pyperclip

regex_DNI = r'''(\d{2})   # primer grupo con dos caracteres.... que utilizaremos para mostrar....
                \.?       # puede haber luego un separador .
                \d{3}
                \.?        # puede haber luego un separador .
                \d{3}      # tres últimos dígitos
                \-?         # puede haber la rayita...
                ([a-zA-Z]) # el final debe ser la letra... la ponemos en un grupo para mostrarla...
            '''

patron_DNI = re.compile(regex_DNI, re.VERBOSE)
texto_a_enmascarar = pyperclip.paste()
# mo = patron_DNI.findall('Hola mi DNI es 42.435.678-A, 42345678A  42.234.657A')
cadena_resultante = patron_DNI.sub(r'\1******\2', texto_a_enmascarar)
print('Enmascarando los DNI encontrados en el portapapeles...')
print('Copiando el resultado al portapapeles...')
pyperclip.copy(cadena_resultante)
