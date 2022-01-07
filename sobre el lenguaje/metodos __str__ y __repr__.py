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