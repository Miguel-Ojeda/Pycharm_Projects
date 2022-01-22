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

# La idea es similar a lo que hacemos para añadir o quitar un ítem de un dictionary
# Por ejemplo, añadamos la puntuación de cada candidato en el test de javascript...
df['js-score'] = [74, 82, 79, 91, 87, 80, 63]
print(df)
'''
       name         city  age  py-score  js-score
101  Xavier  Mexico City   41      88.0        74
102     Ann      Toronto   28      79.0        82
103    Jana       Prague   33      81.0        79
104      Yi     Shanghai   34      80.0        91
105   Robin   Manchester   38      68.0        87
106    Amal        Cairo   31      61.0        80
107    Nori        Osaka   37      84.0        63
'''

# También podemos añadir, en vez de una lista, un valor que se va a repetir siempre...
df['total-score'] = 0.0
print(df)
'''
       name         city  age  py-score  js-score  total-score
101  Xavier  Mexico City   41      88.0        74          0.0
102     Ann      Toronto   28      79.0        82          0.0
103    Jana       Prague   33      81.0        79          0.0
104      Yi     Shanghai   34      80.0        91          0.0
105   Robin   Manchester   38      68.0        87          0.0
106    Amal        Cairo   31      61.0        80          0.0
107    Nori        Osaka   37      84.0        63          0.0
'''

# Al añadir, se añaden a la derecha... si queremos insertarla en un sitio concreto, podemos utilizarlp
# con el método insert, indicando el lugar de la columna...
df.insert(loc=4, column='django-score', value=[54., 69., 82, 73., 56., 89, 54])
print(df)
'''
      name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          54.0        74          0.0
102     Ann      Toronto   28      79.0          69.0        82          0.0
103    Jana       Prague   33      81.0          82.0        79          0.0
104      Yi     Shanghai   34      80.0          73.0        91          0.0
105   Robin   Manchester   38      68.0          56.0        87          0.0
106    Amal        Cairo   31      61.0          89.0        80          0.0
107    Nori        Osaka   37      84.0          54.0        63          0.0
'''

# Para borrar columnas es como en los diccioanrios---> del DataFrame[label_col]
# Borremos la columna total_score
del df['total-score']
print(df)

# También podemos borrar un columna con el método pop... -> la extrae del dataframe... (la quita)
# y a la vez nos la retorna... útil si queremos quitarla pero a la vez recuperarla...
# Creamos
df['total-score'] = np.linspace(60, 92, 7)
# y ahora la extraemos... será un objeto Series, lógicamente...
extraccion = df.pop('total-score')
print(extraccion)
print(type(extraccion))
'''
101    60.000000
102    65.333333
103    70.666667
104    76.000000
105    81.333333
106    86.666667
107    92.000000
Name: total-score, dtype: float64
<class 'pandas.core.series.Series'>
'''

# También podemos borrar varias columnas a la vez, con el drop method
# Es el método que ya vimos para eliminar las filas... pero por defecto intenta eliminar filas
# Por tanto, para eliminar columnas habrá que indicarle que el eje es el de las columnas
# con axis = 1
# axis 1 indica que queremos quitar cols, inplace para que actualice el propio objeto
df.drop(labels='age', axis=1, inplace=True)
# Eliminamos dos cols más
df.drop(labels=['city', 'js-score'], axis=1, inplace=True)
print(df)
'''
       name  py-score  django-score
101  Xavier      88.0          54.0
102     Ann      79.0          69.0
103    Jana      81.0          82.0
104      Yi      80.0          73.0
105   Robin      68.0          56.0
106    Amal      61.0          89.0
107    Nori      84.0          54.0
'''