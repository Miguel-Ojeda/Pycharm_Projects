import pandas as pd

# Creemos primero un panda como hicimos en 01...
data = { 'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
         'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'],
         'age': [41, 28, 33, 34, 38, 31, 37],
         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
         }
# También creamos una lista con las labels para las filas (es opcional, si no se llamarían 0, 1, 2, 3, ...
row_labels = [101, 102, 103, 104, 105, 106, 107]
# tb serviría row_labels = range(101, 108)

df = pd.DataFrame(data=data, index=row_labels)
'''Ya tenemos nuestro df
       name         city  age  py-score
101  Xavier  Mexico City   41      88.0
102     Ann      Toronto   28      79.0
103    Jana       Prague   33      81.0
104      Yi     Shanghai   34      80.0
105   Robin   Manchester   38      68.0
106    Amal        Cairo   31      61.0
107    Nori        Osaka   37      84.0
'''

# Ahora veamos como guardarlo en un csv...
# Es directo!! con método .to_csv()
df.to_csv('job_candidates_v2.csv')
'''parámetros
path_or_buf: Any | None = None,
           sep: str = ",",
           na_rep: str = "",
           float_format: str | None = None,
           columns: Sequence[Hashable] | None = None,
           header: bool | list[str] = True,
           index: bool = True,
           etc ----
           
Algunas cosas interesantes

path_or_buf – File path or object, if None is provided the result is returned as a string.
sep – String of length 1. Field delimiter for the output file.
na_rep – Missing data representation.
float_format – Format string for floating point numbers.
columns – Columns to write
header – Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.
index – Write row names (index).
index_label – Column label for index column(s) if desired. If None is given, and `header` and `index` are True,
then the index names are used. A sequence should be given if the object uses MultiIndex.
If False do not print fields for index names. Use index_label=False for easier importing in R.
'''
# Observar qué, realmente si simplemente damos el nombre del fichero hace lo que se espera...
'''
,name,city,age,py-score
101,Xavier,Mexico City,41,88.0
102,Ann,Toronto,28,79.0
103,Jana,Prague,33,81.0
104,Yi,Shanghai,34,80.0
105,Robin,Manchester,38,68.0
106,Amal,Cairo,31,61.0
107,Nori,Osaka,37,84.0
'''
# Si quisiéramos que lo pusiera un label tb. al index...
df.to_csv('job_candidates_v3.csv', index_label='MI_INDICE')
'''
MI_INDICE,name,city,age,py-score
101,Xavier,Mexico City,41,88.0
102,Ann,Toronto,28,79.0
103,Jana,Prague,33,81.0
104,Yi,Shanghai,34,80.0
105,Robin,Manchester,38,68.0
106,Amal,Cairo,31,61.0
107,Nori,Osaka,37,84.0
'''

# Si no quisiéramos que guardara la columna con los índices...
df.to_csv('job_candidates_sin_indices.csv', index=False)
'''
name,city,age,py-score
Xavier,Mexico City,41,88.0
Ann,Toronto,28,79.0
Jana,Prague,33,81.0
Yi,Shanghai,34,80.0
Robin,Manchester,38,68.0
Amal,Cairo,31,61.0
Nori,Osaka,37,84.0
'''

# Por supuesto, para crear un df desde un csv se hace igual de fácil...
# Por ejemplo, con la versión guardada normal, o sea, con la columna index pero sin un label para index...

nuevo_df = pd.read_csv('job_candidates_v2.csv')
print(nuevo_df)
'''
   Unnamed: 0    name         city  age  py-score
0         101  Xavier  Mexico City   41      88.0
1         102     Ann      Toronto   28      79.0
2         103    Jana       Prague   33      81.0
3         104      Yi     Shanghai   34      80.0
4         105   Robin   Manchester   38      68.0
5         106    Amal        Cairo   31      61.0
6         107    Nori        Osaka   37      84.0
'''
# Cuidado, ha leído todo_ el csv, pensando que eran datos y ya está, con lo que
# le ha puesto nombre a la primera columna (pq todas las columnas deben tener identificado) y ademña
# ha creado los index, pq todo df debe tener index para identificar las filas...
# NO ES ESTO LO QUE QUERÍAMOS:.. para arreglaro decirle simplemente que ya tenemos una columna de index!!
nuevo_df_2 = pd.read_csv('job_candidates_v2.csv', index_col=0)
# Logicamente, si nuestro csv ya tiene una columna de index, pues la utilziamos...
# Si no tuviera, y todos fueran datos, pues no, claro
# En este caso, ya está bien creado...
print(nuevo_df_2)
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


