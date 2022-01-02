class Prueba:
    def __init__(self):
        self.hola = 5
        self.mensaje = "Hola"
        # self.lista = [i for i in range(1, 10)]
        self.dict = {'uno': 1, 'dos': '222', self.mensaje: 'otro mensaje'}

    def __del__(self):
        print('borrando el objeto')

# cada objeto creado desde una clase tiene un diccionario asociado,
# donde lista las variables de la clase con sus valores
objeto = Prueba()
print(objeto.__dict__)
print(2*'\n')

# recordemos que podemos añadir más variables a nuestra instancia si necesitamos
objeto.otro_dato = [i**2 for i in range(1,6)]
print(objeto.__dict__)
print(2*'\n')

# Python reserva espacio adicional para que este diccionario pueda ir creciendo, por si necesitamos más espacio
# pero si tenemos claro que no vamos a añadir dinámicamente ninguna variable nueva a la clase
# lo que es aconsejable, y queremos crear muchos objetos... pues estaremos desperdiciando memoria
# por ejemplo, si tenemos la clase punto, con sólo variables x e y , y queremos crear 10_000 puntos
# para cada punto, el diccionario del objeto tendría esas dos variables, pero tb. mucho espacio adicional
# para ir creciendo... lo que sería una périda de espacio...

# cuando tenemos claro que las variables son las que son, y queremos ahorrar espacio (pq vamos a crear
# muchos objetos) conviene usar la técnica de los slots...
# Ejemplo
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # More methods

# De esta forma cuando creemos un punto, reservará espacio adicional para que el diccionario vaya creciendo...
punto1 = Point(2, -5)
punto1.otro_valor = [i for i in range(1,100)]
print(punto1.__dict__)

# si tenemos claro que no vamos a añadir nada nuevo, que es realmente lo normal...
# mejor hacemos, para optimizar memoria, slots...
class PointWithSlots():
    # Define slots for only two instance variables
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


punto2 = PointWithSlots(-2, 5)
print(punto2)
# Cuidado, ahora ya el objeto punto2 no tiene diccionario... lo siguiente daría error
# print(punto2.__dict__)
# En su lugar tieen slots!!

# lo siguiente daría error, porque lo que hace los slots es bloquear los atributos!!!
# punto2.otro_valor = 14

# con lo anterior optimizamos memoria, ya que el programa reserva justo la memoria necesaria para mantener
# el diccionario con los dos atributos definidos y sus valores...!!
# ejemplo:
lista_puntos = [PointWithSlots(i, 3 * i - 4) for i in range(1, 20_000)]
for punto in lista_puntos:
    print(punto)

# Hemos creado 20000 puntos sin desperdiciar espacio en diccionarios!! mediante slots!!