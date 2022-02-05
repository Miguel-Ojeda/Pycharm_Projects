# Recordar q cuando ocurre alguna excepción, tanto si ocurre automáticamente porque no hemos
# tenido cuidado, o porque la provocamos nosotros con raise...
# lo que pasa es que va saliendo de todas las funciones hasta
# que se encuentra algún bloque try / except apropiado...
# Si no encuentra ninguno, sigue saliendo al nivel superior, hasta que hace crash....

# Si queremos nosotros invocar excepciones podemos hacerlo de 3 formas
# Opción 1: una excepción de un error concreto...
# raise <ExceptionName>('<Any string to describe the error>')
# Ejemplo: raise ValueError('You need to specify an integer')

# Opción 2: una excepción genérica... no muy adecuado....
# raise Exception('The amount cannot be a floating-point number')

# Opción 3: una excepción hecha a medida por nosotros...
# # Define a custom exception
# class <CustomExceptionName>(Exception):
#     pass
# raise <CustomExceptionName>('llljdkafjdklfjdkl')

# Ver página 77 del libro Object Oriented Python (no starch press)
# Lo mejor es crear una excepción personalizada...

# También ver capítulo 11 de Automate the boring stuff



# Un ejemplo...
class Abort_box_print(Exception):
    pass

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Abort_box_print('Symbol must be a single character string.')
    if width <= 2:
        raise Abort_box_print('Width must be greater than 2.')
    if width % 2 == 0:
        raise Abort_box_print('El ancho debe ser impar')
    if height <= 2:
        raise Abort_box_print('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * ((width - 2)//2)  + symbol + ' ' * ((width - 2)//2) + symbol)
        print(symbol * width)

for sym, w, h in (('*', 7, 4), ('O', 21, 5), ('x', 7, 7), ('ZZ', 3, 3), ('@', 5, 6),):
    try:
        boxPrint(sym, w, h)
    except Abort_box_print as err:
        print('An exception happened: ' + str(err))
