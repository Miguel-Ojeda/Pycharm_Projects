# Python Workouts tema 7
"""Puede venir bien, por claridad, partir las comprehensions en varias líneas de esta forma...
"""
lista_cuadrados_impares = [x * x  # Expresión
                           for x in range(10)  # iteración
                           if x % 2]  # condición
print(lista_cuadrados_impares)
# >>> [1, 9, 25, 49, 81]


# Esta técnica nos permite entender fácilmente expresiones anidadas como la siguiente
lista_pares = [(x, y)  # expresión
               for x in range(10)  # iteración 1
               if x % 2  # condición 1
               for y in range(5)  # iteración 2
               if y % 3]  # condición 2

print(lista_pares)
# >>> [(1, 1), (1, 2), (1, 4), (3, 1), (3, 2), (3, 4), (5, 1), (5, 2), (5, 4),
# (7, 1), (7, 2), (7, 4), (9, 1), (9, 2), (9, 4)]

"""Otro ejemplo, supongamos que tenemos un diccionario donde las claves son los países que
he visitado, y los valores asociados, las ciudades que he visitado en cada uno de los países"""
all_places = {'USA': ['Philadelphia', 'New York', 'Cleveland', 'San Jose', 'San Francisco'],
              'China': ['Beijing', 'Shanghai', 'Guangzhou'],
              'UK': ['London'],
              'India': ['Hyderabad'],
              'Spain': ['Madrid', 'Barcelona', 'Las Palmas', 'Gijón']}
# ¿Cómo obtener una lista con todas las ciudades?
all_cities = [city
              for pais, ciudades in all_places.items()
              for city in ciudades]
print(all_cities)
# ['Philadelphia', 'New York', 'Cleveland', 'San Jose', 'San Francisco', 'Beijing',
# 'Shanghai', 'Guangzhou', 'London', 'Hyderabad', 'Madrid', 'Barcelona', 'Las Palmas', 'Gijón']

# Lo mismo, pero para obtener la lista ordenada (primero ordena por país, luego, tb. dentro de cada país..
all_cities = [city
              for pais, ciudades in sorted(all_places.items())
              for city in sorted(ciudades)]
print(all_cities)
# ['Beijing', 'Guangzhou', 'Shanghai', 'Hyderabad', 'Barcelona', 'Gijón',
# 'Las Palmas', 'Madrid', 'London', 'Cleveland', 'New York', 'Philadelphia', 'San Francisco', 'San Jose']

'''
Importante!!! Las list comprehensions producen esa lista, crean un objeto lista
con todos esos ítems... esto podría llegar a ocupar mucho espacio en la memoria
Por ello mucha gente utiliza, en vez de list comprehensions, prefieren usar generator expresiones,
que, aunque similares a las list comprehensions, van con paréntesis, y no producen la lista
ni ningún objeto, sino que, en cada llamada van produciendo el item siguiente...
'''
import sys
# Ejemplo con list comprehensions...
suma = sum([x*x for x in range(100_000)])
print(suma)
# >>> 333328333350000
# Aquí, simplemente para crear la suma, hemos creado la lista de 100_000, que ocupa bastante memoria
print(sys.getsizeof([x*x for x in range(100_000)]))
# En concreto, ocupa, en mi ordenador.... 800_984 bytes de memoria...

# Otra forma de hacerlo sin utilizar nada de memoria sería, como decimos, con generator expressions
suma = sum((x*x for x in range(100000)))
print(suma)
# >>> 333328333350000
# Aquí no se crea ningún objeto... simplemente
# se le pasa a la función suma un objeto generador...
# (Antes se le pasaba una lista entera en memoria, que ocupaba 800_984 bytes
# Ahora se le pasa un objeto generador que ocupa...
print(sys.getsizeof((x*x for x in range(100000))))
# >>> 104
# que ocupa simplemente 104 bytes... el generador, que ocupa 104 bytes
# es capaz de ir generando todos los números necesarios para la función
# suma, sobre la marcha, uno a uno, sin ocupar memoria adicional!!!

# Además, se pondemos en una función una generator expresion como único argumento
# se puede quitar el paréntesis exterior... osea, podíamos haber puesto...
suma = sum(x*x for x in range(100000))

