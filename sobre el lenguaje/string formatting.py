# Hay 4 métodos, de más antiguo a más moderno son ...

#1 – “Old Style” String Formatting: con el operador %
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# es similar al C con printf
name = 'Mike'
print('Hola, %s' % name)
# Resultado: Hola, Mike
# Lo que hace el operador es reemplazar lo que va después en la cadena en el lugar apropiado
# Realmente lo que ve la función print es la cadena 'Hola, Mike'...
# previamente el operador % a reemplazado %s con el valor almacenado en name...
# La s le indica que pase el valor a string con la función str()

value = 123000
print('El código es: %s' % value)
print('El código es: %x' % value)  # x hace que convierte a string con lowercase hexadecimal
print('El código es: %X' % value)  # x hace que convierte a string con uppercase hexadecimal

# Podemos aplicar el operador % a un sólo valor.. si fueran a varios hay que ponerlos en una tupla...
print('Hola %s... El código es: 0X%X' % (name, value))

# Muchísimas opciones, aunque ya obsoleto... preferible métodos más modernos...
# De todas formas, consultar docs...

# Método 2: “New Style” String Formatting
# https://docs.python.org/3/library/stdtypes.html#str.format    Aquí está la función str.format() que hace todo
# https://docs.python.org/3/library/string.html#string-formatting   Format String Syntax !!!
# Esta sintaxis además es compartida tb por el método 4!!!
# Ahora ya pasamos totalmente de los %
# Lo que se ha hecho es crear un método, que se aplica a las strings...
# El método es str.format() y es similar a los % pero mucho más elegante...
# En la cadena original, lo que vayamos a sustituir está en {}.
# Dentro de los paréntesis indicaremos el orden (si pasamos a format parámetros posicioneles)
# o la 'key', si pasamos a format parámetros keyword....
cadena_base = 'Hola {0}, cómo estás esta {1}. Mañana me voy a {2}'
cadena_1 = cadena_base.format('Juan', 'tarde', 'Luxemburgo')
cadena_2 = cadena_base.format('Luisa', 'noche', 'Cantabria')
print(cadena_1)
print(cadena_2)
# Muy potente la opción con keyword params...
name = 'Miguel'
error = 5876342
print('Hola {name}, hay un error tipo 0x{error:x}!'.format(name=name, error=error))

# Método 3 – Literal String Interpolation (Python 3.6+)
# Una nueva forma de formatear strings... se llama Formatted String Literals... (f-Strings)
# es muy potente... nos deja meter directamente ya las expresiones dentro de los literales
a = 5
b = 10
print(f'Hola {name}... Five plus ten is {a + b} and not {2 * (a + b)}.')
# Realmente esto lo transforma el parser al recorrer el programa... cambia lo que está en {} al valor apropiado...
# Lo que es genial es que estas f-strings soportan la sintaxis anterior del método 2...
# https://docs.python.org/3/library/string.html#string-formatting   Format String Syntax !!!
print(f"Hey {name}, there's a {error:#x} error!")

# 4 – Template Strings
# Es más simple realmente, y menos potente, pero para muchos casos es lo indicado...
# Funciona con templates... por lo que habrá que importar la clase Template!!!
from string import Template
# Simplemente definimos un template (que es una cadena que incluye campos especiales...
# y luego llamamos al método substitute para que sustituya esos campos por lo que le digamos...
t = Template('Hello, cómo estás $name? Ayer vi a $name2, te manda recuerdos...')
name2 = 'Juana'
resultado = t.substitute(name='Miguel', name2=name2)
# Obs. el primer name2 es el nombre del keyword arg, el segundo el del objeto... obviamente no tienen pq ser igual
print(resultado)
# observar que estos templates no permiten nada como convertir a hexadecimal, etc...
# si lo necesitamos tenemos que hacerlo nosotros!!!
t = Template('Hello, cómo estás $name? Oye, el programa dio el error $error!!')
t.substitute(name=name)





