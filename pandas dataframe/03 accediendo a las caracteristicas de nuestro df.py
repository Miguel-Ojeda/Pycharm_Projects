import pandas as pd
import numpy as np

# Creemos nuestro df
data = { 'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
         'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
         'age': [41, 28, 33, 34, 38, 31, 37],
         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
         }
row_labels = [101, 102, 103, 104, 105, 106, 107]
df = pd.DataFrame(data=data, index=row_labels)
'''
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
102     Ann      Toronto   28      79.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
105   Robin   Manchester   38      68.0
106    Amal        Cairo   31      61.0
107    Nori        Osaka   37      84.0
'''

# Acceder a los índics con .index
print(df.index)  # Int64Index([101, 102, 103, 104, 105, 106, 107], dtype='int64')
print(df.index[3])  # --> 104
print('Los índices son: ', end='')
for indice in df.index:
    print(indice, end=', ')
print()
# Los índices son: 101, 102, 103, 104, 105, 106, 107,

# Lo mismo con las columnas, accedemos con
print(df.columns)  # Index(['name', 'city', 'age', 'py-score'], dtype='object')
print(df.columns[1])  # city

 # Tanto df.index como df.columns son index objects, que también son secuencias
 # a las que podemos acceder como hemos visto por la notación para listas [],
# y también podremos iterar en ellos en un for, etc.
# PERO CUIDADO, SON INMUTABLES!!! no puedo hacer df.columns[1] = 'CIUDAD'
try:
    df.index[0] =1001
except Exception as err:
    print('Uff, no se puede cambiar un índice, da ', err)
try:
    df.columns[1] = 'CIUDAD'
except Exception as err:
    print('Uff, no se puede cambiar una columna, da ', err)
# Nos dirá, en cada caso... 
# Uff, no se puede cambiar una columna, da  Index does not support mutable operations
# O sea, los objetos Index no soportan operaciones mutables

# PERO Sí QUE SE PUEDEN CAMBIAR ENTERO, claro, no cambiamos el Index en sí,
# sino que creamos otro nuevo y lo asignamos a los atributos del df
df.index = np.arange(10, 17)
df.columns = np.array(['Nombre', 'Ciudad', 'Edad', 'Puntuación'])
print(df)
'''
    Nombre       Ciudad  Edad  Puntuación
10  Xavier  Mexico City    41        88.0
11     Ann      Toronto    28        79.0
12    Jana       Prague    33        81.0
13      Yi     Shanghai    34        80.0
14   Robin   Manchester    38        68.0
15    Amal        Cairo    31        61.0
16    Nori        Osaka    37        84.0
'''

# Otro atributo fundamental de los dataframes es .values
# Nos retorna un 2-dim numpy arragy... donde cada row del array es una row del dataframe
values = df.values
print(repr(values))
'''
array([['Xavier', 'Mexico City', 41, 88.0],
       ['Ann', 'Toronto', 28, 79.0],
       ['Jana', 'Prague', 33, 81.0],
       ['Yi', 'Shanghai', 34, 80.0],
       ['Robin', 'Manchester', 38, 68.0],
       ['Amal', 'Cairo', 31, 61.0],
       ['Nori', 'Osaka', 37, 84.0]], dtype=object)
'''
# También podemos hacer el método to_numpy() que hacer realmente lo mismo
print(df.to_numpy())
'''
[['Xavier' 'Mexico City' 41 88.0]
 ['Ann' 'Toronto' 28 79.0]
 ['Jana' 'Prague' 33 81.0]
 ['Yi' 'Shanghai' 34 80.0]
 ['Robin' 'Manchester' 38 68.0]
 ['Amal' 'Cairo' 31 61.0]
 ['Nori' 'Osaka' 37 84.0]]
'''
# La documentación recomienda que para acceder al lovs valores utilicemos el método to_numpy
# porque podremos pasar parámetros adicionales para configurar la conversión
# Por ejemplo, podemos decirles a qué tipo convertir si hay varios tipos de datos, o
# si queremos hacer una copia de los datos o no... etc
# Otro ejemplo
new_df = pd.DataFrame({"A": [1, 2], "B": [3, 4], 'C': [5, 3], 'D': [8, 1]})
print(new_df)
'''
   A  B  C  D
0  1  3  5  8
1  2  4  3  1
'''
# Ahora pasamos a un array
array = new_df.to_numpy()
print(array)
'''
   A  B  C  D
0  1  3  5  8
1  2  4  3  1
 '''
# Pero cuidado, el array podría compartir los datos con el data frame!!!
array[1][1] = 1_000_000
'''
[[1 3 5 8]
 [2 4 3 1]]
'''
print(new_df)
# Al cambiar el array, hemos cambiado el dataframe!!!
'''
   A        B  C  D
0  1        3  5  8
1  2  1000000  3  1
'''

# Cuidado, a veces aunque dejemos el defecto, que es copy=False, así y todo_ pues va a crear otro
# array independiente... pero si quisiéramos asegurarnos de que son independiente usar copy=True
new_df = pd.DataFrame({"A": [1, 2], "B": [3, 4], 'C': [5, 3], 'D': [8, 1]})
# Creemos ahora el array con datos independientes!!
array = new_df.to_numpy(copy=True)
# Ahora, al modificar el array, no afectará al dataframe
array[1][1] = 1_000_000
print(array)
'''
[[      1       3       5       8]
 [      2 1000000       3       1]]
'''
print(new_df)
'''
   A  B  C  D
0  1  3  5  8
1  2  4  3  1
'''

# Otro método interesante que nos da información sobre el tipo de contenido del dataframe es df.dtypes
# Este método nos dice qué tipo de datos hay en cada columna!!
# Esto nos retorna un objeto Series, con los nombres de las columnas como labels, y tipo de datos como values
print(df.dtypes)
'''
Nombre         object
Ciudad         object
Edad            int64
Puntuación    float64
dtype: object
'''

# Si queremos cambiar los tipos a usar en un data frame se puede hacer,
# creando un nuevo data type que sea como el original, pero con los tipos que le digamos...
# Para ello, simplemente, en el parámetro dtype tenemos que darle un diccionario, especificando
# como keys las columnas del df que queremos cambiar, y como value el valor que queremos usar ahora
# Por ejemplo... si queremos ahorrar memoria podríamos crear un nuevo dataframe con los tipos de
# edad y puntuación a 32 bits...
new_vals = {'Edad': np.int32, 'Puntuación': np.float32}
df_1 = df.astype(new_vals)
# El df_ se verá igual, pero estamos ahorrando...
print(df_1.dtypes)
'''
Nombre         object
Ciudad         object
Edad            int32
Puntuación    float32
dtype: object
'''
# Otro ejemplo más bestia... supongamos que queremos pasar de los decimales del test,
# y que queremos convertir la columna de edad a strings...
df_2 = df.astype({'Edad': str, 'Puntuación': int})
print(df_2)
'''    Nombre       Ciudad Edad  Puntuación
10  Xavier  Mexico City   41          88
11     Ann      Toronto   28          79
12    Jana       Prague   33          81
13      Yi     Shanghai   34          80
14   Robin   Manchester   38          68
15    Amal        Cairo   31          61
16    Nori        Osaka   37          84
'''
# YA NO TENEMOS LOS DECIMALES DE LA PUNTUACIÓN-
# ADEMÁS, LA EDAD AHORA NO SON NÚMEROS; SINO strings... (aunque no se ve en la captura)
print(df_2.dtypes)
'''
Nombre        object
Ciudad        object
Edad          object <----
Puntuación     int32 <----
'''

# Otros atributos sencillos, similares a los que tiene numpy son
# df.ndim --> 2 dimensiones del dataframe
# df.size --> 28 cuántos datos contiene el dataframe (cuántas 'celdas' o valores contiene?)
# df.shape --> (7, 4) cuántas filas y cuántas columnas
print(df)
dimensiones, (rows, cols), size = (df.ndim, df.shape, df.size)
print(f'El df tiene {dimensiones} dimensiones: {rows} filas y {cols} columnas, en total {size} elementos')
# El df tiene 2 dimensiones: 7 filas y 4 columnas, en total 28 elementos

# Otro método interesante es .memory_usage() que nos da un Series Object, con el index y los column names
# como los labesl del series object, y lo que ocupa en memoria como values..
# Veamos la comparación entre los 3 dataframes df (el original) y df_1 df_2
for dataframe in (df, df_1, df_2):
    print(dataframe.memory_usage())

'''
El dataframe original, con las columnas edad y puntuación a 64 bits...
Index         56
Nombre        56
Ciudad        56
Edad          56
Puntuación    56
dtype: int64

El dataframe que cambiamos para ahorrar memoria, con edad y puntuación a 32 bits...
Index         56
Nombre        56
Ciudad        56
Edad          28
Puntuación    28
dtype: int64

El último dataframe que convertimos... donde almacenamos los textos como strings y la puntuación como entero
Index         56
Nombre        56
Ciudad        56
Edad          56
Puntuación    28
dtype: int64
'''