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
'''
        name         city  age  py-score  django-score  js-score
101  Xavier  Mexico City   41      88.0          71.0      71.0
102     Ann      Toronto   28      79.0          95.0      95.0
103    Jana       Prague   33      81.0          88.0      88.0
104      Yi     Shanghai   34      80.0          79.0      79.0
105   Robin   Manchester   38      68.0          91.0      91.0
106    Amal        Cairo   31      61.0          91.0      91.0
107    Nori        Osaka   37      84.0          80.0      80.0
'''

# Se hace parecido a con los numpy arrays
# Obtengamos un objeto series multiplicando una columna *2
series_o = 2 * df['js-score']
print(series_o)
'''
101    142.0
102    190.0
103    176.0
104    158.0
105    182.0
106    182.0
107    160.0
'''
# Podemos hacer cualquier operación, sumar restar multiplicar dividir... y se aplicará a cada componente
series_o = df['js-score'] / 2 + 5
print(series_o)
'''Name: js-score, dtype: float64
101    40.5
102    52.5
103    49.0
104    44.5
105    50.5
106    50.5
107    45.0
---> Name: js-score, dtype: float64
'''

# Observar que el objeto series coge sus atributos como nombre, index, del dataframe y del series del que se creó
# En el caso anterior, conserva el name del elemento con el que se creó...

suma = df['js-score'] + df['django-score'] + df['py-score']
# Lógicamente suma, aquí, no va a tener nombre, porque proviene de tres columnas!!
print(suma)
'''
101    230.0
102    269.0
103    257.0
104    238.0
105    250.0
106    243.0
107    244.0
dtype: float64
'''

# Podemos hacer operaciones con las columnas de esta forma, y aprovechar el series object para crear un nueva columna
# por ejemplo, queremos calcular una total score haciendo una media ponderada con los tres tests que tenemos...

df['total-score'] = 0.30 * df['django-score'] + 0.40 * df['py-score'] + 0.30 * df['js-score']
print(df)
'''       name         city  age  py-score  django-score  js-score  total-score
101  Xavier  Mexico City   41      88.0          71.0      71.0         77.8
102     Ann      Toronto   28      79.0          95.0      95.0         88.6
103    Jana       Prague   33      81.0          88.0      88.0         85.2
104      Yi     Shanghai   34      80.0          79.0      79.0         79.4
105   Robin   Manchester   38      68.0          91.0      91.0         81.8
106    Amal        Cairo   31      61.0          91.0      91.0         79.0
107    Nori        Osaka   37      84.0          80.0      80.0         81.6
'''

# Veamos otra forma de crear la misma columna de los totales con funciones de numpy
# PARECE MUCHO MÁS DIFÍCIL, PERO ES UN MÉTODO MUY POTENTE TAMBIÉN
# Primero creamos un series object con los pesos que va a tener cada columna para calcular la media
wgts = pd.Series(data=[0.4, 0.3, 0.3], index=['py-score', 'django-score', 'js-score'])
# creamos con esto un series object compatible con la estructura del dataframe
print(wgts)
'''
py-score        0.4
django-score    0.3
js-score        0.3
dtype: float64
'''

# Observar que podemos obtener fácilmente un sub-data frame con las columnas que nos interesan de esta forma
df_columnas_para_la_media = df[wgts.index]
print(df_columnas_para_la_media)
'''
     py-score  django-score  js-score
101      88.0          71.0      71.0
102      79.0          95.0      95.0
103      81.0          88.0      88.0
104      80.0          79.0      79.0
105      68.0          91.0      91.0
106      61.0          91.0      91.0
107      84.0          80.0      80.0
'''

# realmente lo anterior es lo mismo que hacer...
df_columnas_para_la_media_2 = df[['py-score', 'django-score', 'js-score']]
print(df_columnas_para_la_media_2)

# Si ahora multiplicamos estas 3 columnas, este subdataframe, por el objeto weights...
# o sea, multiplicamos la primera columna, por el primer valor de wgts, la segunda ...
resultado = df[wgts.index] * wgts
print(resultado)
'''
     py-score  django-score  js-score
101      35.2          21.3      21.3
102      31.6          28.5      28.5
103      32.4          26.4      26.4
104      32.0          23.7      23.7
105      27.2          27.3      27.3
106      24.4          27.3      27.3
107      33.6          24.0      24.0
'''
# Ya sólo nos quedaría utilizar la función np.sum para sumar
# por defecto, la función suma por columnas...
print(np.sum(resultado))
'''
py-score        216.4
django-score    178.5
js-score        178.5
dtype: float64
'''
# Evidentemente no es esto lo que queremos
# Queremos que sume las 3 columnas para terminar el cálculo de la media ponderada!!
# Para arreglarlo le decimos que suma no verticalmente, cada columna, sino horizontalmente, las columnas entre sí
print(np.sum(resultado, axis=1))
'''
101    77.8
102    88.6
103    85.2
104    79.4
105    81.8
106    79.0
107    81.6
dtype: float64
'''

# Hagámoslo todo_ entonces por el segundo método, con numpy, pero más rápido...
# creando sobre la marcha la columna, y añadiéndola...
# repitamos todo_ resumido...
wgts = pd.Series(data=[0.4, 0.3, 0.3], index=['py-score', 'django-score', 'js-score'])
df['nuevo_total'] = np.sum(df[wgts.index] * wgts, axis=1)
print(df)

# Aunque este método parece más difícil, lo bueno es que es superrápido meter los datos apropiados
# para cambiar la media si tuviéramos que hacerlo... ¡¡está todo_ en el object series wgts...!!