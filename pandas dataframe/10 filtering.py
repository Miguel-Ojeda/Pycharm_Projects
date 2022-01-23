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

# Recordemos que, por ejemplo, df['py-score'] es un panda series..
# Pues bien, si comprobamos una condición en un panda series... ---> NOS DEVUELVE OTRO PANDA SERIES OBJECT!!!
# Que nos va a servir de filtro ...

print(df['py-score'])
filtro = df['py-score'] >= 80
print(filtro)
'''
df['py-score'] ---->
101    88.0
102    79.0
103    81.0
104    80.0
105    68.0
106    61.0
107    84.0
Name: py-score, dtype: float64

FILTRO   df['py-score'] >= 80 --->
101     True
102    False
103     True
104     True
105    False
106    False
107     True
Name: py-score, dtype: bool
'''

# Pues un filtro es simplemente un panda series como el anterior, que nos dice True o False y esto va a indicar
# si el dato con ese label lo queremos seleccionar o no en el dataframe
# En el ejemplo, el pandas series tiene True en 101, 103, 104, 107...
# O sea, es un filtro que nos servirá para seleccionar esas filas!!!

# Para utilizar el filtro simplemente sería....   panda[filtro]
# En nuestro caso quedaría...

# df_filtrado = df[   df['py-score'] >= 80    ]
# Para que quede más claro es mejor...
df_filtrado = df[filtro]
print(df_filtrado)
'''
Al aplicar el filtro, nos quedan las filas que tienen True en el filtro....

       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
103    Jana       Prague   33      81.0          88.0      88.0         85.2
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''

# Otro ejemplo
filtro = (df['py-score'] >= 80) &  (df['total-score'] >= 80)
# Ahora obligamos a que saquen >=80 en los dos tests!!
# No sirve con el and... pq el and sirve si a la izquierda y a la derecha tenemos un valor cierto
# o falso, y en este caso tenemos panda series objetos!!!
# Además, si no lo ponemos entre paréntesis no sirve... porque intentaría aplicarlo con los números
# AL ponerlo entre paréntesis se fuerza que el bitwise & se aplica al df completo
# y en panda se ha sobrecargado el operador & para que funcione bien!!

print(filtro)
'''
101    False
102    False
103     True
104    False
105    False
106    False
107     True
dtype: bool
'''
print(df[filtro])
'''
     name    city  age  py-score  django-score  js-score  total-score
103  Jana  Prague   33      81.0          88.0      88.0         85.2
107  Nori   Osaka   37      84.0          80.0      80.0         81.6
'''

# Podemos usar tb. el bitwise operator OR  --> |
# Que saque al menos 80 en alguno de esos dos tests...
filtro = (df['py-score'] >= 80) | (df['total-score'] >= 80)
print(df[filtro])
'''
       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
103    Jana       Prague   33      81.0          88.0      88.0         85.2
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''

# También podemos cambiar valores cuando se cumple alguna condición
'''Este método nos permite mirar si se cumple una condición.---  y SI NO SE CUMPLE, PONER UN VALOR POR DEFECto'''
# pOR EJEMPLO, si tenemos el series objecto de la columna django-score y queremos que se nos devuelva
# lo mismo si la columna py-score es mayor que 80... pero si no, que se ponga 0 en django-score!!
print(df['py-score'].where(cond=df['py-score'] > 80, other=0.0))
# NOS DEVOLVERÍA ESTE SERIES OBJECT... (no se cambia nada, tan sólo se crea otro objeto)
'''
101    88.0
102     0.0
103    81.0
104     0.0
105     0.0
106     0.0
107    84.0
'''

# También tenemos el método filtro... cojamos 3 columnas...
# filter(items, like, regex, axis, ...)

sub_df = df.filter(items=['py-score', 'dj-score', 'js-score'])
print(sub_df)
'''
     py-score  js-score
101      88.0      71.0
102      79.0      95.0
103      81.0      88.0
104      80.0      79.0
105      68.0      91.0
106      61.0      91.0
107      84.0      80.0
'''
# Podríamos haber hecho lo anterior también así, más fácil con like
# que coge columnas con labels que contengan la cadena especificada
sub_df = df.filter(like='score')  # bueno tb. cogería total-score
print(sub_df)

# Por defecto el filtro nos va a buscar columnas, el axis=1 es el defecto!!!
# Se podría hacer lo mismo para filtrar por... si tuvieran nombre adecuados, claro
# Aquí no tiene sentido...  vamos a cambiar los índices para ver un ejemplo...
df.index = ['01-01', '01-02', '02-01', '02-02', '02-03', '03-01', '03-02']
print(df)
'''
         name         city  age  py-score  django-score  js-score  total-score
01-01  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
01-02     Ann      Toronto   28      79.0          95.0      95.0         88.6
02-01    Jana       Prague   33      81.0          88.0      88.0         85.2
02-02      Yi     Shanghai   34      80.0          79.0      79.0         79.4
02-03   Robin   Manchester   38      68.0          91.0      91.0         81.8
03-01    Amal        Cairo   31      61.0          91.0      91.0         79.0
03-02    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''

# Vamos a filtrar, quedándonos con las filas cuyo label sea 02-....
print(df.filter(like='02-', axis=0))
'''
        name        city  age  py-score  django-score  js-score  total-score
02-01   Jana      Prague   33      81.0          88.0      88.0         85.2
02-02     Yi    Shanghai   34      80.0          79.0      79.0         79.4
02-03  Robin  Manchester   38      68.0          91.0      91.0         81.8
'''

# PODEMOS USAR FILTRADO TAMBIÉN CON EXPRESIONES REGULARES!!!
# Volvemos a dejar los índices como estaban...
df.index = range(101, 108)
# Se puede hacer cualquier cosa, pero, como ejemplo sencillo, cojamos las filas 104, 105, 106
print(df.filter(regex='10[456]', axis=0))
'''
      name        city  age  py-score  django-score  js-score  total-score
104     Yi    Shanghai   34      80.0          79.0      79.0         79.4
105  Robin  Manchester   38      68.0          91.0      91.0         81.8
106   Amal       Cairo   31      61.0          91.0      91.0         79.0
'''

'''
Resumen
Forma 1 de filtrado: panda[condicion en columnas
Ejemplo df[ df['py-score'] >= 24  ]; más cómodo df[filtro]
Se pueden usar operadores lógicos bitwise AND(&), OR(|), NOT(~), XOR (^)
pero entonces colocar entre paréntesis los operandos 







'''

