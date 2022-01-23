import pandas as pd
import numpy as np

# Datos
temp_c = [8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0, 9.1, 12.8, 15.3, 19.1,
          21.2, 22.1, 22.4, 23.1, 21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
# DatetimeIndex
date_time_index = pd.date_range(start='2022-01-01 00:00:00', periods=24, freq='H')
# Creación del dataframe
df_temperaturas = pd.DataFrame(data={'temp_c': temp_c}, index=date_time_index)

'''
                   temp_c
2022-01-01 00:00:00     8.0
2022-01-01 01:00:00     7.1
2022-01-01 02:00:00     6.8
2022-01-01 03:00:00     6.4
2022-01-01 04:00:00     6.0
2022-01-01 05:00:00     5.4
2022-01-01 06:00:00     4.8
2022-01-01 07:00:00     5.0
2022-01-01 08:00:00     9.1
2022-01-01 09:00:00    12.8
2022-01-01 10:00:00    15.3
2022-01-01 11:00:00    19.1
2022-01-01 12:00:00    21.2
2022-01-01 13:00:00    22.1
2022-01-01 14:00:00    22.4
2022-01-01 15:00:00    23.1
2022-01-01 16:00:00    21.0
2022-01-01 17:00:00    17.9
2022-01-01 18:00:00    15.5
2022-01-01 19:00:00    14.4
2022-01-01 20:00:00    11.9
2022-01-01 21:00:00    11.0
2022-01-01 22:00:00    10.2
2022-01-01 23:00:00     9.1
'''

# Para visualizar los dataframes, el módulo Panda utiliza la librería matplotlib
# Por ello, el interfase para visualizar los pandas es muy similar al de matplotlib

# Método pandas.plot()
df_temperaturas.plot()
'''Algunos ejemplos de uso de argumentos para el método plot
kind='line' (para dibujar líneas, es el defecto), 
color='g' (para usar el color green de línea), 
style='.-'  (nos dice que queremos un estilo de línea con puntos)
mfc='k' (para usar el negro en el interior de los puntitos
mfc es una lias para marker_face_colors
ms=15 (marker size=)

Ejemplo:
df.temperature.plot(kind='line', color='g', style='.-', mfc='k', ms=10)
Si queremos dibujar con la clase kind='line', podíamos tb hacer hecho...
df.temperature.plot.line(color='g', style='.-', mfc='k', ms=10)

Lo anterior nos mostraría la gráfica...

Si queremos guardarla... a lo anterior hay que decirle que queremos obtener la gráfica
y guardarla...
'''
# Obtener la gráfica... y guardarla...
df_temperaturas.plot.line(color='g', style='.-', mfc='k', ms=10).get_figure().savefig('temperatures.png')
# podemos guardar en muchos formatos... pdf, svg, cambiar dpi, ...
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
df_temperaturas.plot.line(color='g', style='.-', mfc='k', ms=10).get_figure().savefig('temperatures.svg')
df_temperaturas.plot.line(color='b', style='.-', mfc='r', ms=15).get_figure().savefig('temperatures_2.svg')

# No sé porqué pero no se genera la salida gráfica, imagino que habrá que crear algún objeto pantalla
# en cualquier caso, sí que se generan las 3 ficheros! están en el directorio!!


# Vamos a ver ahora un histograma con los datos de los candidatos al trabajo....
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


# Creemos un histograma basado en la columna py-score
# Como antes, tenemos dos opciones...
# 1) df.plot(kind='hist'....
# 2) df.plot.hist(
df['py-score'].plot.hist(bins=5, alpha=0.8, )
