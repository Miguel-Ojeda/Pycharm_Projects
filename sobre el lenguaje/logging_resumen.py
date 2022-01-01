# Es similar al uso del print para depurar programas, pero es muchísimo mejor porque luego no hace falta ir borrando
# los print, con el tiempo y peligro que conlleva si nos equivocamos
# Simplemente podríamos deshabilitar el print de forma fácil en una línea y ya estaría
# Además tiene más opciones ocnfigurables y nos da info más completa..

# Primero importar e inicializar ...
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Esto lo que hace es indicar que queremos que se muestren los logging con código igual o superior al level DEBUG
# mostrando una columna de tiempo, otra con el nivel del error y otra con los mensajes...

# Cada nivel tiene una función para mostrar los mensajes de error...
# realmente nosotros elegimos los niveles como queramos
# Los niveles son, de menor a mayor, son:
# Level               Logging function (función con la que mostraremos el mensaje)
# DEBUG               logging.debug()
# INFO                logging.info()
# WARNING             logging.warning()
# ERROR               logging.error()
# CRITICAL            logging.critical()

# Ahora, simplemente, en la parte del código que queramos hacer log, escribiremos, según el nivel...
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# Lo bueno que tiene esto es que, si por eejmplo, sólo queremos que se muestren los mensajes con prioridad
# igual o superior a ERROR, tan sólo hemos de cambiar la línea del loggin.basicConfig y poner...
logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s')
# SImplemente con esto, sin tocar el código, ya las otras líneas con logging de menos prioridad no aparecerían...

# Además, cuando queramos dehabilitar el logging, pues tenemos dos opciones:
# borrar del código fuente, o comentar log logging (que ahora ya no confundiremos con los print genuinos)
# o simplemente utilizar la funcion loggig.disable(logging.LEVEL_QUE_QUERQAMOS)
# Por eejmplo, si queremos deshabilitar todos los mensajes del log, simplemente pondríamos...
logging.disable(logging.CRITICAL)
# lo que hace es que no nos muestra desde critical hacia abajo, o sea no nos mostraría nada!!!

# Si queremos que los logging vayan a un fichero...
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



