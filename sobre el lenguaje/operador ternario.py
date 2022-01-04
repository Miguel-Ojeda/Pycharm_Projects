# Forma clásica de escribir el código...
# Pythonic way...
condition = True
if condition:
    message = 'Access granted'
else:
    message = 'Access denied'

# Podemos acortar el código con el Python’s “Ugly” Ternary Operator
valueIfTrue = 'Access granted'
valueIfFalse = 'Access denied'
condition = True
message = valueIfTrue if condition else valueIfFalse

# Es una sintaxis 'rara', la hicieron adrede así...
# Por qué la introdujeron (en Python 2.5) pese a que va en contra de... beautiful is better than ugly?
# Había mucha demanda por lo visto...



