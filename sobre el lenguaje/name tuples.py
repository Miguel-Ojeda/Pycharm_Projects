# namedtuples son un tipo adicional de container (está en collections) que incluye la posibilidad de nombrar
# a las componentes de las tuplas, aparte de referirnos a ellas por el índice como siempre

# SOn un nuevo tipo de objetos, que tenemos que crear nosotros
# Para crear estas nuevas tuplas personalizadas, lo hacemos utilizando la función namedtuple...
# Lo que hace está función realmente es crear por nosotros una nueva clase de objeto...
# la forma de utilizarlo será...
# Clase_que_nos_creará = namedtuple(Nombre_que_queremos_para_la_clase, 'name_comp_1 name_comp_2 ... name_comp_n')
# Ejemplos...


from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Con esto estamos creando un nuevo tipo de objeto... no ninguna instancia concreta...

# El primer argumento, 'Car' (typename) es el nombre que queremos dar a la clase...
# Realmente Python no sabe como vamos a llamar al objeto de retorno... (en este caso lo hemos llamado
# también Car a la variable, pero podemos llamarlo como quisiéramos,.... por eso la función namedtuple(
# necesita tb como argumento que le digamos como queremos llamar a la clase que está creando!!!

# Por qué pasamos los nombres que queremos para las dcomponentes como una cadena???
# Poruqe la función namedtupla está hecha de forma que luego invoca al método split() para obtener
# los nombres que queremos para nuestras componentes de la tupla...

# Obs... también podemos pasarle directamente una lista con los nombres para los componentes de la namedtuple
# Lo anterior es equivalente a ...
# Car = namedtuple('Car', ['color', 'mileage'])

# O sea, e primer argumento es el typename... el nombre que queremos darle al objeto que vamos a crear que namedtuple
# Si el segundo parámetros es una cadena... obtendrá los nombres de las componentes con split()
# si el segundo parámetro es una lsita, pues obtendrá los nombres de los items de la lista...


# Ahora es fácil crear nuevo objetos del tipo definido...
car_1 = Car('red', 350)

# Podremos acceder a las componentes de dos formas...
# Con componentes como siempre... o como a miembros de una clase...
print(car_1.color, ' = ', car_1[0])
print(car_1.mileage, ' = ', car_1[1])

# Si vemos el tipo, ya no es una tupla
print(type(car_1))
# <class '__main__.Car'>

# Pero podemos fácilmente obtener un objeto tupla si quisiéramos...
# tuple(car_1)

# El operador splat * para desempaquetar funciona como en las tuplas...
print(*car_1)  # >>> red 350

# Realmente, la forma de implementar namedtuples internamente es como si fueran clases...

# Como son clases, realmente podemos crear namedtuples derivadas... para poder añadirle
# métodos adicionales... aunque es mejor utilizar el método de la composición y ya está
# o sea crear una nueva clase que incluya en sus atributos alguna tupla de estas creads...

# Podemos crear fácilmente named_tuplas derivadas de otras... hierarchies of namedtuples..
# usando the base tuple’s _fields property:
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
# Esto realmente es crear una nueva namedtuple con los campos de car y los nuevos que queramos...
# o sea, lo que estamos haciendo realmente es...
# ElectricCar = namedtuple('ElectricCar', 'color mileage charge'),
# pero de forma más rápida...


# Aparte de la propiedad _fields tenemos otras interesantes...
# todas estas propiedades empiezan con _ pero son para usarlas!!! no se entienden aquí como internas
# _asdict() :   --> nos muestra la named tupla pero como si fuera un diccionario...!!!
print(car_1._asdict())  # >> {'color': 'red', 'mileage': 350}

# _replace() nos crea una shallow copy de la namedtuple y nos permite reemplazar algunos valores...
car_2 = car_1._replace(color='blue')
print(car_2) # --> Car(color='blue', mileage=350)

# Lastly, the _make() classmethod can be used to create new instances of a namedtuple from a sequence or iterable:
car_3 = Car._make(['red', 999])
print(car_3) # --> Car(color='red', mileage=999)




