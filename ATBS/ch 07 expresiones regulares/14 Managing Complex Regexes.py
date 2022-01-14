# Managing Complex Regexes  --> re.VERBOSE

# Si la expresión regular que tenemos que escribir es complicada, conviene ponerla en varias líneas
# e ir explicando los pasos que estamos dando...!!
# Para hacer esto hay que decirle a re.compile que
# IGNORE LOS ESPACIOS EN BLANCO Y LOS COMENTARIOS en medio de la expresión....
# Lo hacemos dando como el segundo argumento la opción re.VERBOSE

# Ejemplo, si queremos crear un patrón utilziando esta esxpresión regularr..
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# Sería muy complicado de entender... mejor hacer...
import re
r_string = '''(
            (\d{3}|\(\d{3}\))? # area code
            (\s|-|\.)? # separator
            \d{3} # first 3 digits
            (\s|-|\.) # separator
            \d{4} # last 4 digits
            (\s*(ext|x|ext.)\s*\d{2,5})? # extension
            )'''

phoneRegex = re.compile(r_string, re.VERBOSE)

# Observar que usamos '''  para construir una cadena multilínea y poder ir partiendo la expresión regular
# a lo largo de varias líneas, e ir explicando todo bien...