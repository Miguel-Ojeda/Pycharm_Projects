import pandas
import pandas as pd
import numpy as np

# Creemos nuestro df para trabajar...
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

# Veamos la inserción y borrado de filas y columnas...
# Antes de nada, tener claro que una row o una columna es un panda Series object
print(type(df.loc[104])) # --> <class 'pandas.core.series.Series'>
print(type(df.city))  # ..> <class 'pandas.core.series.Series'>
print(type(df['age']))  # --> <class 'pandas.core.series.Series'>

# Entonces un Series object es realmente como un array de numpay
# pero que también tiene labels para facilitar el acceso
print(np.array(df.city))  # ['Mexico City' 'Toronto' 'Prague' 'Shanghai' 'Manchester' 'Cairo' 'Osaka']
print(df.city)
'''
101    Mexico City
102        Toronto
103         Prague
104       Shanghai
105     Manchester
106          Cairo
107          Osaka
Name: city, dtype: object
'''
# Observar que el Series object es realmente lo mismo, pero con los labels que nos facilitan el acceso
'''
Un Series object consta de:
**  datos (sería simpelmente los datos puros como el array). En el anterior,
    los datos son: Mexico City, Toronto, Prague...
**  index (son 'índices' o labels que nos facilitan el acceso a los datos...
    En este caso los index son 101, 102, 103...
**  un name: en este caso el name es city...

Estos datos los rellena todos el accesor que estamos usando desde el dataframe...
Pero si queremos crear un Series Object, debemos de darlo nosotros todo...
'''

''' Hombre, no es imprescindible, claro, si no vamos a insertarlo en un dataframe existente...
Podríamos crearlo sin más, y que cogiera el name y los inddices por defecto'''
s1 = pd.Series([5, 6, 7])
print('Creando un Series Object sin especificar ni name ni índexes...')
print(s1)
'''
0    5
1    6
2    7
dtype: int64
'''
# Lo que sucede, como vemos, es que no se le asigna ningún nombre y, además, los índices son los números empezando en 0



print(np.array(df.loc[105]))
print(df.loc[105])
'''
name             Robin
city        Manchester
age                 38
py-score          68.0
Name: 105, dtype: object
'''
'''En este caso, el Series object consta de:
    Data: Robin, Manchester, 38, 68.0m
    index de acceso: name, city, age, py-score
    name: 105
'''

# Como los Series objects tienen los index/labels es muy fácil acceder a los datos
# Por ejemplo, si tenemos este Series Object anterior que representa los datos de Robin...
robin_row_as_numpy_array = np.array(df.loc[105])
robin_row_as_Series_Object = df.loc[105]
# para acceder a la edad es muy fácil con las labels que incluye el Series Object
# print(f'La edad de robin es {robin_row_as_Series_Object["age"]}')
print(f'La edad de robin es {robin_row_as_Series_Object.age}')
# Evidentmente, tb. podemos acceder al objeto series con el índice
print(f'La edad de robin es {robin_row_as_Series_Object[2]}')
# En cambio con el numpy array tenemos que contar a ver qué lugar ocupa el dato
print(f'La edad de robin es {robin_row_as_numpy_array[2]}')

# Además, el objeto series tb. tiene guardada la información sobre su nombre...
print(df.loc[105])
'''
name             Robin
city        Manchester
age                 38
py-score          68.0
----->   Name: 105, dtype: object
'''
print(df.age)
'''101    41
102    28
103    33
104    34
105    38
106    31
107    37
----> Name: age, dtype: int64
'''
# En la última línea está el nombre del objeto series, que nos indica que es el objeto con label 105
print(df.loc[105].name)  # 105
print(df.age.name)  # age


# CONCLUSIÓN IMPORTANTE
# Podemos considerar que un data frame es simplemente una colección de series objects
# Ya sean los series objects las filas, o las columnas... con todos esos series objects
# realmente tendríamos todo_ el dataframe


# Ahora, por fin, utilizando esto, como un dataframe es simplemente una colección de series ob
# pues veamos como añadir un series object más al dataframe.-... empezamos añadiendo filas...

# Añadimos una nueva fila...

# Por supuesto para que esto sirva, al crear el Series Ob., además de dar los datos
# debemos indicar unos index compatibles, y un name adecuado...

# Como en este caso vamos a añadir un nuevo candidato...
# 'John', 'Lisboa', 32, 81   (el nombre, la ciudad, la edad y la puntuación
# Pues los índices que nos facilitan el acceso debemos ponerles que sean
# name, city, age, py-score... o sea, los índices serán --> df.columns!!
# y el 'nombre' de la fila, para que sea consistente, pues será en este caso
# 108, que sigue la numeración existente... (en otros casos pueden ser strings, etc

# Según todo_ lo que hemos comentado, el series sería el siguiente!!
john = pd.Series(data=['John', 'Lisboa', 32, 81], index=df.columns, name=108)

print(john)
'''
name          John
city        Lisboa
age             32
py-score        81
Name: 108, dtype: object
'''
# Vemos que es similar a lo obtenido cuando hacemos, por ejemplo df.loc[105]
# O sea, va a ser 'compatible' con nuestro df existente...

# Ahora toca agregarlo!! usaremos el método append
# Pero cuidado, no se agrega al dataframe existente 'in place' como se hace con las listas!!
# Sino que crea otro y nos devuelve el objeto... con lo que
# habrá que recogerlo... o sea, no vale con hacer como con las listas... df.append(...)
# Tendremos que hacer...
df = df.append(john)
print(df)




# O sea, los datos que tiene el series object y el numpy array son los mismos
# pero el series object añade una capa adicional (los index y el name) que nos facilitan
# el acceso a los datos y su inserción en un dataframe

# Por supuesto, para inser
'''
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
102     Ann      Toronto   28      79.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
105   Robin   Manchester   38      68.0
106    Amal        Cairo   31      61.0
107    Nori        Osaka   37      84.0
108    John       Lisboa   32      81.0
'''

# Si quisiéramos borrarla, pues usamos el método drop()
# Como antes, la transofrmación no es inplace--- sino que se crea y devuelve un nuevo objeto
# para el método drop como argumento darle las labels en una lista...
df.drop(labels=108)
print(df)
# Esto no funciona, necesitamos, como antes...
df = df.drop(labels=108)
print(df)

# Otra posibilidad equivalente es simplemente utilizar la opción inplace
# df.drop(labels=108, inplace=True) , aquí ya no es necesario poner df = df.drop(....)

# Al drop los labels podemos darle un valor, o varios si queremos
print(df.drop(labels=[104, 106]))
# Eliminamos ahora las filas con labels 104, 106
'''
101  Xavier  Mexico City   41      88.0
102     Ann      Toronto   28      79.0
103    Jana       Prague   33      81.0
105   Robin   Manchester   38      68.0
107    Nori        Osaka   37      84.0
'''


# Vamos a insertar a John otra vez... pero con una name de 100
john = pd.Series(data=['John', 'Lisboa', 32, 81], index=df.columns, name=100)
df = df.append(john)
print(df)

# Observa que, pese a que el name vaya antes.... lo coloca al final del df!!



