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


# Métodos para iterar por columnas
# Es similar a los diccioanrios cuando usamos dict.items() que nos produce un generador para ir iterando...
# También nos devuelve un generador!!
print(type(df.items()))  # <class 'generator'>

# cada item es una tupla...   (col_label, col)

generador = df.items()   # Creamos el generador
# Ahora veamos el primer elemento devuelto
col_label, col_content = next(generador)
print('El nombre de la columna es ---> ', col_label)
print('El object series con el contenido de la columna es --->', col_content, sep='\n')
# Ahora el siguiente
col_label, col_content = next(generador)
print('El nombre de la columna es ---> ', col_label)
print('El object series con el contenido de la columna es --->', col_content, sep='\n')


# Por supuesto, mucho más fácil hacer la iteración con un for...
print('\n\nRecorriendo el dataframe por columnas...\n')
for col_label, col_content in df.items():
    print(f'Columna ---> "{col_label}"', 'SERIES OBJECT DE LA COLUMNA', col_content, sep='\n', end='\n\n')

# También podemos usar el método .iteritems() que hace lo mismo!!


# Iterando ahora en filas!!!
# el método es iterrows() que de la misma forma devuelve un generador con lo que todo es similar...
# Análogamente el generador va a ir devolviendo una tupla: (row_labe, row_content)
# row_content, lógicamente , va a ser un series object
print('\n\nRecorriendo el dataframe por filas...\n')
for row_label, row_content in df.iterrows():
    print(f'Fila ---> "{row_label}"', 'SERIES OBJECT DE LA FILA', row_content, sep='\n', end='\n\n')



# HAY OTRO MÉTODO MÁS PARA ITERAR POR FILAS MUY INTERESANTE
# .itertuples() nos devuelve un generador, de nuevo, pero el generador nos devuelve siempre un solo objeto
# que va a ser un named_tuple que representa a todos los contenidos de la fila, pero ya con labels
print('\n\nRecorriendo el dataframe por filas con namedtuples...\n')
for row in df.itertuples():
    print(row)

'''
Recorriendo el dataframe por filas con namedtuples...

Pandas(Index=101, name='Xavier', city='Mexico City', age=41, _4=88.0, _5=71.0, _6=71.0, _7=77.8)
Pandas(Index=102, name='Ann', city='Toronto', age=28, _4=79.0, _5=95.0, _6=95.0, _7=88.6)
Pandas(Index=103, name='Jana', city='Prague', age=33, _4=81.0, _5=88.0, _6=88.0, _7=85.19999999999999)
Pandas(Index=104, name='Yi', city='Shanghai', age=34, _4=80.0, _5=79.0, _6=79.0, _7=79.4)
Pandas(Index=105, name='Robin', city='Manchester', age=38, _4=68.0, _5=91.0, _6=91.0, _7=81.8)
Pandas(Index=106, name='Amal', city='Cairo', age=31, _4=61.0, _5=91.0, _6=91.0, _7=79.0)
Pandas(Index=107, name='Nori', city='Osaka', age=37, _4=84.0, _5=80.0, _6=80.0, _7=81.6)
'''

# Si quisiéramos que la named_tupla no tuviera el índice, pq nos da igual, pues podríamos decírselo
# Lo mismo, si queremos que la namedtupla sea de un tipo distinto a Panda, pues se lo decimos
# veamoslo...
for row in df.itertuples(index=False, name='Candidatos'):
    print(row, end='--> ')
    print(f'Name: {row.name}, City: {row.city}')

'''Candidatos(name='Xavier', city='Mexico City', age=41, _3=88.0, _4=71.0, _5=71.0, _6=77.8)--> Name: Xavier, City: Mexico City
Candidatos(name='Ann', city='Toronto', age=28, _3=79.0, _4=95.0, _5=95.0, _6=88.6)--> Name: Ann, City: Toronto
Candidatos(name='Jana', city='Prague', age=33, _3=81.0, _4=88.0, _5=88.0, _6=85.19999999999999)--> Name: Jana, City: Prague
Candidatos(name='Yi', city='Shanghai', age=34, _3=80.0, _4=79.0, _5=79.0, _6=79.4)--> Name: Yi, City: Shanghai
Candidatos(name='Robin', city='Manchester', age=38, _3=68.0, _4=91.0, _5=91.0, _6=81.8)--> Name: Robin, City: Manchester
Candidatos(name='Amal', city='Cairo', age=31, _3=61.0, _4=91.0, _5=91.0, _6=79.0)--> Name: Amal, City: Cairo
Candidatos(name='Nori', city='Osaka', age=37, _3=84.0, _4=80.0, _5=80.0, _6=81.6)--> Name: Nori, City: Osaka
'''

# Las named_tuplas son un objeto muy conveniente para acceder a nuestros datos, ya que no tenemos que recordar el orden
# sino utilizar los nombres asociados a cada componenete de la namedtuple
