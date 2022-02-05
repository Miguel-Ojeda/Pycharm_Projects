import sys
import time

# Constantes
MOSTRAR = '*****************'
ESPACIO = ' '
MAX_INDENT = 5

# Iniciamos variables
num_indentations = 0
increasing_indentation = True

try:
    while True:

        mostrar = ESPACIO * num_indentations + MOSTRAR
        print(mostrar)
        time.sleep(0.05)

        if increasing_indentation:
            if num_indentations < MAX_INDENT:
                num_indentations += 1
            else:
                num_indentations -= 1
                increasing_indentation = False
        else:
            if num_indentations > 0:
                num_indentations -= 1
            else:
                num_indentations += 1
                increasing_indentation = True

except KeyboardInterrupt:
    print('Bueno, hasta luego Lucas...')
    sys.exit()
