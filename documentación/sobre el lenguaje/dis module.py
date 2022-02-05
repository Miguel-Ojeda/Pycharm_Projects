# dis --> Disassembler for Python bytecode
# Lo que hace es, al texto de un programa en sintaxis Python, nos muestra como
# quedaría en bytecode....

# Ejemplo de uso...
def myfunc(alist):
    return len(alist)

# No sé pq no sirve...
# pero desde el modo de comando sí sirve...

import dis

# dis.dis(myfunc)
# --->
# 2           0 LOAD_GLOBAL              0 (len)
#               2 LOAD_FAST                0 (alist)
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE

