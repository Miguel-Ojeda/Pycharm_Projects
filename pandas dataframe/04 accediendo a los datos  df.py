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

# Ya vimos en la intro (01...) que podemos acceder a las columnas de 2 formas...
print(df['name'])
print(df.city)  # sólo válido si la col. tiene nombre de identificador válido; no podríamos hacer esto con py-score
# Recordemos que nos da un Series Object, con labels los índices, y como valores los distintos valores de la col
'''
101    Mexico City
102        Toronto
103         Prague
104       Shanghai
105     Manchester
106          Cairo
107          Osaka
Name: city, dtype: object'''


# Acceso a rows con el accesor .loc[label_name de la fila en el index]
print(df.loc[105])  # Loc nos devuelve tb un objeto Series
'''
Name: city, dtype: object
name             Robin
city        Manchester
age                 38
py-score          68.0
Name: 105, dtype: object
'''
print('df.loc[105] --> ', type(df.loc[105]))
# Es un objeto series...
# <class 'pandas.core.series.Series'>

# PORQUE ES SóLO UNA FILA... si fueran varias, como veremos, sería un dataframe




# Pero loc es más potente, nos permite recuperar subsets de nuestro data frame
# DataFrame.loc[ row_labels_list, col_labels_list] y podemos obtener así el subset que queramos!!!
# [ , ] esto es como en los array bidimensionales de numpy!!
# Por ejemplo para obtener todas las rows y algunas columnas...
sub_data = df.loc[:, ['name', 'py-score']]
print(type(sub_data)) #  <class 'pandas.core.frame.DataFrame'> NOS RETORNA UN NUEVO DATAFRAME!!!!
print(sub_data)
'''
      name  py-score
101  Xavier      88.0
102     Ann      79.0
103    Jana      81.0
104      Yi      80.0
105   Robin      68.0
106    Amal      61.0
107    Nori      84.0
'''

# O sea, si con .loc retornamos varias filas, el objeto que tenemos ya sería un dataframe...
print(df.loc[105:106])
print('df.loc[105:106] --> ', type(df.loc[105:106]))
'''
      name        city  age  py-score
105  Robin  Manchester   38      68.0
106   Amal       Cairo   31      61.0
df.loc[105:106] -->  <class 'pandas.core.frame.DataFrame'>
'''

# Podemos fácilmente, p ejemplo, elegir filas basadas en criterios..
# por ejemplo, filas con índice par

sub_df = df.loc[ [index for index in df.index if index % 2 == 0]  ]
# Equivalente sería sub_df = df.loc[ [index for index in df.index if not index % 2]  ]
print(sub_df)
'''
     name      city  age  py-score
102   Ann   Toronto   28      79.0
104    Yi  Shanghai   34      80.0
106  Amal     Cairo   31      61.0
'''

# Otro ejemplo, con selección de columnas concretas...
sub_df = df.loc[[index for index in df.index if index % 2 == 0], ['name', 'age']]
print(sub_df)
'''
     name  age
102   Ann   28
104    Yi   34
106  Amal   31
'''

# Otro ejemplo, subconjunto formado por las personas que obtuvieron al menos 80 puntos...
sub_df = df.loc[[index for index in df.index if df.loc[index]['py-score'] >= 80]]
print(sub_df)
'''
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
107    Nori        Osaka   37      84.0
'''

# También podemos acceder a datos del data frame de forma cómoda utilizando integer indices, en vez de labels
# Para ello utilziar el accesor iloc (integer loc)...
# Es lo mismo, pero utilizando índices en vez de labels!!
# Por ejemplo queremos ver la primera fila, mostrando la primera yh tercera columna...
sub_df = df.iloc[0, [0, 2]]
print(sub_df)
'''
name    Xavier
age         41
Name: 101, dtype: object
'''
# Para extraer el subset con la gente que sacó a partir de 80...
# Con accesor loc  -->  sub_df = df.loc[[index for index in df.index if df.loc[index]['py-score'] >= 80]]
sub_df = df.iloc[[index for index in range(df.shape[0]) if df.iloc[index, 3] >= 80]]

print(sub_df)
'''
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
107    Nori        Osaka   37      84.0
'''

# Extraer las 3 primeras filas, pero sólo para columna con el nombre y la edad
sub_df = df.iloc[:3, [0, 2]]
print(sub_df)
'''
       name  age
101  Xavier   41
102     Ann   28
103    Jana   33
'''

# Resumen importante.
# el accesor loc utiliza, para acceder, los labels
# el acceso loc utilzia, para acceder, los indices!


# Ejemplo para acceder al elemento de la fila con label 105 y cuya columna tien label city
dato_individual = df.loc[105, 'city']
print(dato_individual)


# ACCESORS ESPECIALIZADOS PARA RECUPERAR UN SOLO DATO: .at    .iat
# funcionan igual que .loc  .iloc pero solo le podemos pasar una row y una columna
# para de esta forma, acceder a un valor (el cruce de la fila y la columna)
# se usan pq, aunque tb se podría con .loc .iloc, están especializados y son más eficientes, ...

# Pero.... si queremos acceder sólo a un dato a un método recomendado, no este!!
# Tenemos el accesor .at !!
# Se escribiría igual, pero está optimizado para acceder a un elemento concreto...
dato_individual = df.at[105, 'city']
print(dato_individual)
# también, podemos acceder a un dato individual por sus índices con el accesor iat
dato_individual = df.iat[4, 1]
print(dato_individual)

