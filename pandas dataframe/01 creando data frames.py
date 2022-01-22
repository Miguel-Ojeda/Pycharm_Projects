import pandas
import pandas as pd   # estándar

# Veamos varias formas de crear DataFrames

# Forma 1 utilizando 1 diccionario, que va a representar los datos de las columnas del dataframe
# Los values son listas que representan los distintos valores de la columna
data = { 'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
         'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
         'age': [41, 28, 33, 34, 38, 31, 37],
         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
         }
# También creamos una lista con las labels para las filas (es opcional, si no se llamarían 0, 1, 2, 3, ...
row_labels = [101, 102, 103, 104, 105, 106, 107]
# tb serviría row_labels = range(101, 108)

df = pd.DataFrame(data=data, index=row_labels)
print(df)
#        name         city  age  py-score
# 101  Xavier  Mexico City   41      88.0
# 102     Ann      Toronto   28      79.0
# 103    Jana       Prague   33      81.0
# 104      Yi     Shanghai   34      80.0
# 105   Robin   Manchester   38      68.0
# 106    Amal        Cairo   31      61.0
# 107    Nori        Osaka   37      84.0

# Si el DataFrame fuera muy grande, podemos ver los primeros o últimos elementos con -->
# los métodos .head(n), .tail(n=5)
print(df.head(3))

# Tenemos métodos para acceder a las labels de las columnas y de las filas...
print(df.index)  # Int64Index([101, 102, 103, 104, 105, 106, 107], dtype='int64')
print(df.columns)  # Index(['name', 'city', 'age', 'py-score'], dtype='object')

# Acceder a las columnas del DataFrame... como si fuera un diccionario, con el nombre de las columnas
cities = df['city']
print(type(cities))  # <class 'pandas.core.series.Series'>   es un Series object
print(cities)   # --> se muestra tb. la columna con los index!!
# 101    Mexico City
# 102        Toronto
# 103         Prague
# 104       Shanghai
# 105     Manchester
# 106          Cairo
# 107          Osaka
# Name: city, dtype: object

# Como este objeto Series incluye los índices, pues tenémos el atributo index que nos los muestra
print('Índices del objeto Series de la columna cities -->', cities.index)

# Otra forma de acceder a la columna, si el nombre de la columna es un identificador válido..-- > con .
print(df.city)
# Es lo mismo que lo anterior!! df['city']

# Observar que si queremos acceder a la columna 'py-score' podremos utilziar
# a) df['py-score']
# Pero no es posible df.py-score pq interpreta df.py (que no existe) - score !!!

# Cada columna es entonces un objeto Pandas.Series  (tb. va a ser así con las filas)
# Podremos acceder a un elemento concreto de la columna dando tb. su fila... ejemplo
print(cities[102])  # --> Toronto
print(df['age'][102])  # cogemos la columna edad y miramos a la fila 102 --> 28
print(df.name[102])  # cogemos de la columna nombre, la fila con index 102  --> Ann

# Acceder a filas!!!   Método .loc[index]
# No vale como antes.... df[fila]!!!
# Se hace con el método .loc
print(df.loc[105])
# No sirve con df[105] como hacíamos con las columnas!!!
# print(df[105])  --> ERROR!!

# El resultado, como antes es un objeto Pandas.Series...
# name             Robin
# city        Manchester
# age                 38
# py-score          68.0
# Name: 105, dtype: object
# INcluye los datos y tb. , en este caso, el nombre de cada campo!!


# FOrma 2 de crear un dataframe: es igual, un diccinario, donde para cada key la clave se indica, pero puede ser
# variado el método.... lista, array, ...
# Podemos usar como antes un diccionario, pero además de listas, como utilizamos antes para los values
# podemos tb. usar arrays de numpy, o incluso un sólo número (lo que indicará que se repetirá!!!)
import numpy as np  # IMPORTAMOS NUMPY para usar los arrays...
# Los arrays estos son en esto caso como listas... pero todo_ contiguo...
dict_2 = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
# Este caso, como la forma 1, los values del dict. son las columnas, pero no es necesario que sean todo_ listas
# como en la forma 1... pueden tb. ser arrays, o un número que se repita siemrpe...
# dict_2, como antes, nos va a describir las 3 columnas, x, y , z.... como z solo tiene 1 elemento, se va a repetir
df_2 = pandas.DataFrame(dict_2)
print(df_2)
#    x  y    z
# 0  1  2  100
# 1  2  4  100
# 2  3  8  100

# COmo no definimos la columna index, pues será por defecto 0, 1, 2, 3...
# Cambiemos esto ahora, definiendo la columna index, y cambiando además el orden de las columnas!!!
df_2b = pandas.DataFrame(dict_2, index=[100, 200, 300], columns=['z', 'y', 'x'])
print(df_2b)
#        z  y  x
# 100  100  2  1
# 200  100  4  2
# 300  100  8  3
# Observamos que con los mismos datos podemos obtener un df distinto, si cambiamos el index, o el orden de las cols.

# Forma 3: con una lista de diccionarios!!!
# Es parecido a la forma 1, pero aquí definimos, en lugar de un único dic, un diccionario por cada columna
# Obviamente, las keys de todos los diccioanrios son las mismas!!
dict_3 = [{'x': 1, 'y': 2, 'z': 100}, {'x': 2, 'y': 4, 'z': 100}, {'x': 3, 'y': 8, 'z': 100}]
pd_3 = pd.DataFrame(dict_3, index=['row_1', 'row_2', 'row_3'])   # Las cols ya las sabe!!!
print(pd_3)

# FOrma 4, una lista de listas / arrays / tuple , donde cada lista/arr/tup interior es una columna...
# Aquí no sabremos ni index, ni cols... si los queremos habrá que especificar...
list_4 = [[1, 2, 100], np.array([2, 4, 100]), (3, 8, 100)]
# crear un df utilizando una lista de listas!!! donde cada lista interior va a ser realmente una columna!!!
pd_4 = pd.DataFrame(list_4)
print(pd_4)
pd_4b = pd.DataFrame(list_4, columns=('c1', 'c2', 'c3'), index=['r1', 'r2', 'r3'])
print(pd_4b)

# FORMA 4b lo mismo, pero la estrucutra exterior, en vez de lista podría ser array de numpy
array_4c = np.array([[1, 2, 100], np.array([2, 4, 100]), (3, 8, 100)])
pd_4c = pd.DataFrame(array_4c, columns=('xx', 'yy', 'ZZ'))
print(pd_4c)
# xx  yy   ZZ
# 0   1   2  100
# 1   2   4  100
# 2   3   8  100

# Cuidado, como los datos para el df son un numpy array, si moficamos el array se modificará el dataframe!!
array_4c[1,1] = 100_000
print(pd_4c)
#    xx      yy   ZZ
# 0   1       2  100
# 1   2  100000  100
# 2   3       8  100

# Si no nos interesara esto, usar la opción copy!!!
# Esto hace que el dataframe se construya con una copia independiente totalmente del array
pd_4d = pd.DataFrame(array_4c, columns=('xx', 'yy', 'ZZ'), copy=True)



# Resumen:
# F1: gran diccionario; cada value va a ser una lista con los valores de cada columna
# F2: gran diccioanrio; cada value va a ser un elemento (lista, array, ..) con los valores de cada columna
# F3: un lista de diccioanrios, un diccioanrio por cada columna.... las keys de los diccionarios van a ser las columnas
