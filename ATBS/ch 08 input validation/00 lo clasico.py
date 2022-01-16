# Lo típico para validar una entrada sería, dependiendo del caso... algo similar a esto...

while True:
    age = input('Enter your age: ')
    try:
        age = int(age)
    except:   # o except ValueError: casi mejor
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# Pero en este tema usaremos un módulo con muchas utilidades que nos facilita mucho esto...
# The PyInputPlus Module
#
# Incluye funciones similares al clásico input, pero encargadas de recoger
# datos numéricos, fechas, correos, ...  de forma que si el usuario no mete
# datos válidos vuelve a repetirle, incluye opciones como límite de repeticiones, límite de tiempo
# funciones personalizadas para validar datos, ....