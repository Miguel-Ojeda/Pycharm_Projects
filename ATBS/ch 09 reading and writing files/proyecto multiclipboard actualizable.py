# El proyecto consiste en modificar el programa el miniclipboard que teníamos
# que permitía, al invocarlos por ejemplo con python mcb <keyword>
# Copiar el mensaje asociado a keyword al portapapeles...
"""El programa recoge una palabra clave de entrada (agree, busy, upsell, despedida...
y copia al portapapeles el texto asociado a la misma
De esta forma implementamos de manera sencilla un mini portapapeles"""

# Ahora debemos ampliar este programa base para que el diccionario de palabras
# asociadas pueda ir creciendo... utilizando el módulo shelve
# Hay que añadirle la siguiente funcionalidad...
# 1. The command line argument for the keyword is checked.
# 2. If the argument is save, then the clipboard contents are saved to # the keyword.
# 3. If the argument is list, then all the keywords are copied to the clipboard.
# 4. Otherwise, the text for the keyword is copied to the clipboard.

# EL PROGRAMA ESTÁ EN mcb2.py