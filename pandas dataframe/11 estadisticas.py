import pandas
import pandas as pd
import numpy as np

# Creemos nuestro df para trabajar...
data = {'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
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


# El método describe nos da mucha información estadística que podemos utilizar....
# df.describe() nos devuelve un nuevo data frame con informaicón estadística respecto a nuestro dataframe
print(df.describe())
'''
             age   py-score  django-score   js-score  total-score
count   7.000000   7.000000      7.000000   7.000000     7.000000
mean   34.571429  77.285714     85.000000  85.000000    81.914286
std     4.429339   9.446592      8.544004   8.544004     3.815507
min    28.000000  61.000000     71.000000  71.000000    77.800000
25%    32.000000  73.500000     79.500000  79.500000    79.200000
50%    34.000000  80.000000     88.000000  88.000000    81.600000
75%    37.500000  82.500000     91.000000  91.000000    83.500000
max    41.000000  88.000000     95.000000  95.000000    88.600000
'''

# Podemos invocar tb. métodos en series o en el data frame entero...
# por ejemplo los métodos mean, std, min, count, max,
# Cuando aplicamos estos métodos a una columna, el resultado será un valor
# Cuando aplicamos estos métodos a todo el dat frame, el resultado será un series object...
list = [df.age.mean(), df['py-score'].mean(), df['total-score'].std(), df.mean(numeric_only=True)]
for item in list:
    print(item)

'''
34.57142857142857
77.28571428571429
3.8155072058764627

Al aplicar la media al dataframe (solo valores numéricos), nos devuelve un objeto Series!!
age             34.571429
py-score        77.285714
django-score    85.000000
js-score        85.000000
total-score     81.914286
dtype: float64
'''








