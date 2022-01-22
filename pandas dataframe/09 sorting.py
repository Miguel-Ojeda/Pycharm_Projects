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
df['django-score'] = [71, 95, 88, 79.0, 91, 91, 80]
df['js-score'] = [71, 95, 88, 79.0, 91, 91, 80]
wgts = pd.Series(data=[0.4, 0.3, 0.3], index=['py-score', 'django-score', 'js-score'])
df['total-score'] = np.sum(df[wgts.index] * wgts, axis=1)
'''
       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
103    Jana       Prague   33      81.0          88.0      88.0         85.2
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
106    Amal        Cairo   31      61.0          91.0      91.0         79.0
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''

# Para ordenar, por columnas o rows, usaremos el método sort_values
'''
sort_values(by, axis=0, ascending=True, inplace=False, ...)
Devuelve un data frame, a no ser que hagamos el cambio inplace...

by puede ser una string (si queremos ordenar por una fila o col) o una lista con las strings de varias filas o cols

axis=0 or 'index' --> por defecto ordena por valores de una (o varias) columnas, con lo que va a ordenadr las filas!!
axis=1 or 'columns' cambiaría el orden de las columnas, utilizando para ello una (o varias) filas...
Esto podría no tener sentido si los datos son de distinto tipo en las distintas columnas, como ocurre en nuestro df
'''
# Ordenamos por el js-score
# Aunque los cambios no se guardan...
resultado = df.sort_values(by='js-score')
print(resultado)
'''
       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
103    Jana       Prague   33      81.0          88.0      88.0         85.2
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
106    Amal        Cairo   31      61.0          91.0      91.0         79.0
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
'''

# Podemos ordenar descendente...
resultado = df.sort_values(by='js-score', ascending=False)
print(resultado)  # Al revés

# Podremos ordenadr por una segunda columna, para romper los empates
# Esto significa que priorizamos por la primera, pero si hay empate miramos la segunda
# Haremos que ambas sean descendentes el criterio de ordenación...
resultado = df.sort_values(by=['js-score', 'py-score'], ascending=[False, False])
print(resultado)
'''
       name         city  age  py-score  django-score  js-score  total-score
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
106    Amal        Cairo   31      61.0          91.0      91.0         79.0
103    Jana       Prague   33      81.0          88.0      88.0         85.2
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
'''

# Vamos ahora a ordenar las columnas... basándonos en alguna fila...
# en este caso no tiene sentido pq en cada fila hay distinto tipo de valores
# Así que antes de nada vamos a extraer un df solo con números...
sub_df = df[['age', 'py-score', 'django-score', 'js-score', 'total-score']]
print(sub_df)
# Es más rápido obtener lo anterior con el iloc....
sub_df = df.iloc[:, 2:6]

'''
     age  py-score  django-score  js-score  total-score
101   41      88.0          71.0      71.0         77.8
102   28      79.0          95.0      95.0         88.6
103   33      81.0          88.0      88.0         85.2
104   34      80.0          79.0      79.0         79.4
105   38      68.0          91.0      91.0         81.8
106   31      61.0          91.0      91.0         79.0
107   37      84.0          80.0      80.0         81.6
'''

# Ahora, como tenemos todo numérico, si tiene sentido ordenar las columnas utilizando los valores de una fila...
# Tendremos que decir que queremos ordenadr por columnas!!!
# En este ejemplo, vamos a ordenar inplace... o sea, el propio data frame va a quedar ordenado...
sub_df.sort_values(by=101, ascending=False, axis='columns', inplace=True)
print(sub_df)
'''
     py-score  django-score  js-score  age
101      88.0          71.0      71.0   41   <---- Las columnas están ordenadas según la fila 101, de mayor a menor
102      79.0          95.0      95.0   28
103      81.0          88.0      88.0   33
104      80.0          79.0      79.0   34
105      68.0          91.0      91.0   38
106      61.0          91.0      91.0   31
107      84.0          80.0      80.0   37
'''
