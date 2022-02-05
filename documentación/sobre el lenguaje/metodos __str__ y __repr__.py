# El método __str__ es lo que se invoca por defecto (si lo hemos definido, claro) cuando intentamos mostrar
# el objeto con print. Ejemplo...

class Coche_0:
    def __init__(self, color, kilometraje):
        self.color = color
        self.kilometraje = kilometraje

# SI ahora creamos una instancia y queremos imprimirlo veamos que pasa...
coche_0 = Coche_0('rojo', 5000)
print(coche_0)
# >>> <__main__.Coche_0 object at 0x000001E0D4627D00>
# No es muy bonito, la verdad...
# lo que ha pasado es que, al intentar imprimir se ha intentado
# realmente hacer print(str(coche_0))
print(str(coche_0))
# Pero como no hemos definido como hacerlo en nuestra clase, pues no sabe y siemplemente muestra lo básico del objeto

# Implementemos el método __str__ que realmente se invoca cuando alguien hace str(objeto)
class Coche_1:
    def __init__(self, color, kilometraje):
        self.color = color
        self.kilometraje = kilometraje

    def __str__(self):
        # La función str debe retornar la conversión a string del objeto que queramos...
        # en este caso, hacemos simplemente....
        return f'Tenemos un coche de color {self.color} con {self.kilometraje} kilómetros acumulados'

coche_1 = Coche_1('rojo', 5000)
print(coche_1)
# >>> Tenemos un coche de color rojo con 5000 kilómetros acumulados

# EL problema es que con implementar el método str para el objeto ¡¡ NO BASTA !!
# Por qué ??
# A veces, se invoca el método repr!!
# Por ejemplo, cuando ponemos simplemente:
# >>> coche_1

# Hay dos métodos realmente que controlan cómo convertir objetos a strings:
# el método __str__
# el método __repr__  se usa, entre otros, cuando queremos inspeccionar un objeto en la consola

# Interesante observar que siempre, objetos como listas o diccionarios usan el método __repr__

# Si implementamos los dos métodos, y queremos asegurarnos de que se invoque el que queramos...
# podemos elegirlo nosotros....!!!
class Coche_2:
    def __init__(self, color, kilometraje):
        self.color = color
        self.kilometraje = kilometraje

    def __str__(self):
        # La función str debe retornar la conversión a string del objeto que queramos...
        # en este caso, hacemos simplemente....
        return f'Método __str__ Tenemos un coche de color {self.color} con {self.kilometraje} kilómetros acumulados'

    def __repr__(self):
        # La función str debe retornar la conversión a string del objeto que queramos...
        # en este caso, hacemos simplemente....
        return f'Método __repr__ Tenemos un coche de color {self.color} con {self.kilometraje} kilómetros acumulados'



coche_2 = Coche_2('rojo', 5000)
print(coche_2)
print(str(coche_2))
print(repr(coche_2))


# Por qué existen 2 métodos que devuelven un strings sobre un objeto..??
# Porque tienen distinta utilidad...
# La string de repr debe ser algo que no deje lugar a la ambigüedad de lo que es el objeto, y su contenido, etc...
# __repr__ debe darnos más información, y más concreta, sin ambigüedad...
# veamos como se implementa con algún de la Python's standard library
import datetime
today = datetime.date.today()
print(today) # o también print(str(today))
# >>> 2022-01-07
print(repr(today))
# >>> datetime.date(2022, 1, 7)
# Realmente, podríamos poner la salida generada por repr en el ejemplo anterior,
# y es un código válido en Python con el que conseguiríamos crear el mismo objeto!!!

# Pero no hay que seguir esta regla, sería demasiado trabajo para implementar
# de esta forma nuestros repr !!!

# Como vemos, repr nos da info mucho más completa,
# no es lo clásico que querríamos imprimir para el usuario de la app
# En cambio, la string de __str__ es más 'amigable' para el usuario...

# Qué hacer, implementar los dos métodos???
# Pues, si implementamos repr ya con eso nos bastaría, porque cuando Python
# no encuentra el método __str__ utiliza el __repr__  (no hace lo mismo a la inversa!!!)

# Podríamos implementar un __repr__ estándar de esta forma...
# y no tendríamos necesidad de implementar el __str__ si no quisiéramos...

class Coche_3:
    def __init__(self, color, kilometraje):
        self.color = color
        self.kilometraje = kilometraje

    def __repr__(self):
        # La función str debe retornar la conversión a string del objeto que queramos...
        # en este caso, hacemos simplemente....
        return (f'{self.__class__.__name__}('    # Hacemos esto, en vez de escribir Coche_3 para que sea reusable
                f'{self.color!r},'  # Ahora pondríamos todos los valores... usando !r para utilizar la string que 
                f'{self.kilometraje!r})')  # devuelve repr() en lugar de la que devuelve str()...

coche_3 = Coche_3('azul', 1250)

print(coche_3)  # como no existe el método __str__ se utilizará el __repr__ !!
# >>> Coche_3('azul',1250)
# Otro ejemplo utilizando la definición anterior del repr...

class Tres_Coches:
    def __init__(self, coche1, coche2, coche3):
        self.coche1 = coche1
        self.coche2 = coche2
        self.coche3 = coche3

    def __repr__(self):
        # de una forma muy rápida, implementamos el repr...
        return (f'{self.__class__.__name__}('  
                f'{self.coche1!r},'    # observar que utilizamos la string repr(coche1)!!!!
                f'{self.coche2!r},'
                f'{self.coche3!r})')

car1 = Coche_3('azul', 1200)
car2 = Coche_3('verde', 5200)
car3 = Coche_3('naranja', 12000)

tres_coches = Tres_Coches(car1, car2, car3)
print(tres_coches)
# >>> Tres_Coches(Coche_3('azul',1200),Coche_3('verde',5200),Coche_3('naranja',12000))


