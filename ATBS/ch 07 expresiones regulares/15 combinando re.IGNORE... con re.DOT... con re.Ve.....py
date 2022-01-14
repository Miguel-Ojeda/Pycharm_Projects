# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# Para combinar estas opciones utilizaremos el pipe |

# Ejemplo
import re
patron = re.compile('foo', re.IGNORECASE | re.DOTALL)  # utiliza bitwise operators.... es antiguo...

