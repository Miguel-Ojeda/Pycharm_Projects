# is nos sirve para saber si dos objetos son el mismo!!
# En cambio, == es para saber si su VALOR es el mismo...
# Ejemplo
lista_1 = [2, 3, 5]  # El objeto tiene una referencia, lista_1
lista_2 = lista_1   # creamos una nueva referencia para el mismo objeto, ya tiene 2 referencias: lista_2 y lista_1
lista_3 = lista_1.copy()   # creamos un nuevo objeto (que es un duplicado); tiene una referencia, lista_3

print(lista_1 is lista_2)   # True
print(lista_1 is lista_3)   # False

# Existe un tipo especial de datos: es el tipo NoneType
# Este tipo sólo tiene un valor posible: None
# En cualquier programa sólo existe como mucho un objeto None...
# Si asignamos None a una variable, pues va a apuntar a ese objeto, con lo que la variable y None van a ser lo mismo
variable = None
print(type(variable))  # <class 'NoneType'>

# Si queremos saber si una variable es None tenemos 2 opciones!!
# La primera, es la de siempre...
print(variable == None)   # Sale True, lógicamente...
# Pero cuidado... esto podría (en algunos casos raros) darnos True incluso si la variable no valiera
# None... dependiendo de si han sobrecargado el operador ==   (aunque sería muy raro).

# Lo que nunca va a fallar, y se ha convertido en el modo Pythonic de hacerlo sería...
# variable is None
print(variable is None)   # ESTO NUNCA VA A FALLAR:::: True

# Por qué funciona....?
# Porque sólo existe, para la clase NoneType, un sólo valor... por tanto, cuando asignamos a una variable
# el valor None, la variable apunta al objeto None, el único objeto None que existe para todo_ el programa...


# NO usar el método de 'is' para saber si una variable es True o False...
# Método Unpythonic...
if variable == True:
    print('Es cierto')

# Método Pythonic:
if variable:
    print('Es cierto')





