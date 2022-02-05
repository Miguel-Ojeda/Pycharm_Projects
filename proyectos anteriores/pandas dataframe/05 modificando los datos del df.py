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

# cambiemos las notas del test...
# accedemos a los datos con el accesor .loc
# a las 4 primeras filas les pondremos 40, 50, 60, 70, y a las otras un 0
df.loc[:104, 'py-score'] = [40, 50, 60, 70]
df.loc[105:, 'py-score'] = 0  # no hace falta pasarle la lista con varios 0, él ya lo hace solo...
print(df)
'''
101  Xavier  Mexico City   41      40.0
102     Ann      Toronto   28      50.0
103    Jana       Prague   33      60.0
104      Yi     Shanghai   34      70.0
105   Robin   Manchester   38       0.0
106    Amal        Cairo   31       0.0
107    Nori        Osaka   37       0.0
'''
# También lo podíamos haber hecho todo de un solo paso, claro
# Por ejemplo...
df.loc[:, 'py-score'] = [10, 20, 30, 40, 50, 60, 70]
print(df)
# otra opción válida sería una tupla, array, arange, range , etc
df.loc[:, 'py-score'] = range(30, 100, 10)
print(df)
'''
  name         city  age  py-score
101  Xavier  Mexico City   41        30
102     Ann      Toronto   28        40
103    Jana       Prague   33        50
104      Yi     Shanghai   34        60
105   Robin   Manchester   38        70
106    Amal        Cairo   31        80
107    Nori        Osaka   37        90
'''

# Si utilizamos el acceso .iloc podemos acceder a la última columna con la puntuación
# tanto indicando el índice 3, como el -1, tal como hacemos con las listas, etc...
df.iloc[:, -1] = np.linspace(20, 50, len(df))
# también podríamos haber puesto el número de filas con df.shape[0] pero es más sencillo con len
print(df)

# También podremos lógicamente cambiar rows del mismo modo...
# Vamos a cambiar la última fila, pero antes la guardamos
old_row = df.loc[107]
# Ahora la cambiamos por algo
df.loc[107] = ['Juanito', 'Las Palmas', 49, 75]
print(df)
'''
        name         city  age  py-score
101   Xavier  Mexico City   41      20.0
102      Ann      Toronto   28      25.0
103     Jana       Prague   33      30.0
104       Yi     Shanghai   34      35.0
105    Robin   Manchester   38      40.0
106     Amal        Cairo   31      45.0
107  Juanito   Las Palmas   49      75.0
'''
# Interesante: tb. podemos cambiar una fila utilzando un diccioanrio
# Así no tendremos ni que recordar el orden de las columnas...
df.loc[107] = {'age': 29, 'py-score': 300, 'city': 'Paris', 'name': 'Miguel'}
print(df)
'''
       name         city  age  py-score
101  Xavier  Mexico City   41      20.0
102     Ann      Toronto   28      25.0
103    Jana       Prague   33      30.0
104      Yi     Shanghai   34      35.0
105   Robin   Manchester   38      40.0
106    Amal        Cairo   31      45.0
107  Miguel        Paris   29     300.0
'''
df.loc[107] = {'py-score': 90, 'city': 'Las Palmas de G. C.'}
print(df)
# Cuidado, como hemos dicho que queríamos asignar toda la fila, pero sólo hemos proporcionado
# valores para dos de las 4 columnas, los otros valores quedan como NaN
'''
101  Xavier          Mexico City  41.0      20.0
102     Ann              Toronto  28.0      25.0
103    Jana               Prague  33.0      30.0
104      Yi             Shanghai  34.0      35.0
105   Robin           Manchester  38.0      40.0
106    Amal                Cairo  31.0      45.0
107     NaN  Las Palmas de G. C.   NaN      90.0
'''
# Lo corregimos, por ejemplo, con una lista (podríamos usar cualquier cosa, un diccioanrio, etc)
df.loc[107, ['name', 'age']] = ['Miguel', 49]
print(df)
'''
       name                 city   age  py-score
101  Xavier          Mexico City  41.0      20.0
102     Ann              Toronto  28.0      25.0
103    Jana               Prague  33.0      30.0
104      Yi             Shanghai  34.0      35.0
105   Robin           Manchester  38.0      40.0
106    Amal                Cairo  31.0      45.0
107  Miguel  Las Palmas de G. C.  49.0      90.0
'''

# Dejemos la fila como estaba...
df.loc[107] = old_row
print(df)  # última fila queda --> 107    Nori        Osaka  37.0      50.0

# Cambiemos un valor concreto, por ejemplo la ciudad de Ann
df.loc[102, 'city'] = 'Madrid'
print(list(df.loc[102]))  # la fila quedaría ['Ann', 'Madrid', 28.0, 25.0]

# Imagino que si es un valor sólo pues mejor utilizar los métodos at...
df.at[105, 'name'] = 'Robin Hood' # De Robin pasamos a Robin Hood
df.iat[5, 1] = 'El Cairo'  # De Cairo pasamos a El Cairo
print(df)
'''
           name         city   age  py-score
101      Xavier  Mexico City  41.0      20.0
102         Ann       Madrid  28.0      25.0
103        Jana       Prague  33.0      30.0
104          Yi     Shanghai  34.0      35.0
105  Robin Hood   Manchester  38.0      40.0
106        Amal     El Cairo  31.0      45.0
107        Nori        Osaka  37.0      50.0
'''
