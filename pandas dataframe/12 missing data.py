import pandas as pd
import numpy as np
'''
Creemos un dataframe de una columna sola, x, con varios valores que representan las contestaciones
de varias personas, pero UNA DE ELLAS NO HA CONTESTADO, y obtenemos [1, 2, , 4] falta una respuesta!!
Cuando vayamos a crear el dataframe NO PODEMOS PONER ESTO, NOS DARÍA ERROR de sintaxis!!
df = pd.DataFrame(data={x: [1, 2, , 4]})  --> ERROR

¿Cómo arreglarlo? Tenemos que poner NaN (not a number)

numpy.nan del módulo numpy
float('nan') que está en Python
math.nan  que está en el módulo math...
Usaremos la opación de numpy....
'''
df = pd.DataFrame(data={'x': [1, 2, np.nan, 4]})
print(df)
'''
     x
0  1.0
1  2.0
2  NaN
3  4.0
'''

# Cuando queremos hacer algún cálculo estadístico, el comportamiento por defecto sería ignorar ese dato...
print(df.mean())  # --> x    2.333333
print(df.mean(skipna=False))  # --> x   NaN
# Lógicamente, vemos que como no hay valor, en los cálculos nos va a dar como resultado tb. NaN
# Pero podemos solucionarlo utilizando... .fillna(value=)
# Nos devuelve un nuevo df
df_relleno = df.fillna(value=0)
print(df_relleno)
# y ya aquí podríamos calcular la media con todo_ si quisiéramos...

# Si quisiéramos modificar el dataframe original, para rellenar los NaN podríams usar la opción inplace
# df.fillna(value=0, inplace=True)

# También podemos especificar formas alternativas de rellenar los valores NaN con method
# Por ejemplo, para rellenar los NaN utilizando el valor anterior encontrado sería method='ffill' (forward fill)
# en el forward fill se rellena para alante, o sea, si falta un valor, el previo se empuja y rellena el hueco
# en este caso el NaN se rellenaría con un 2
df_relleno = df.fillna(method='ffill')
print(df_relleno)
# También podríamos utilizar un backward fill method='bfill'

# También podemos rellenar los NaN interpolando los valores perdidos con los conocidos..
# en el caso anterior, como el que falta está entre un 2 y un 4, pues se haría la media, 3
print(df.interpolate())
'''
     x
0  1.0
1  2.0
2  3.0
3  4.0
'''

# También podríamos eliminar todos los NaN con el método dropna
# Nos sirve para eliminar cualquier fila (defecto axis=0) o columna (axis=1) que contenga algún NaN
print(df.dropna())
'''
     x
0  1.0
1  2.0
3  4.0
'''

# podemos hacerlo inplace, como casi siempre!!
df.dropna(inplace=True)
print(df)
'''
     x
0  1.0
1  2.0
3  4.0
'''





