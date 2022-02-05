import pandas as pd

# Veamos como crear un data frame para una serie temporal (time series)
# tendremos uun data frame con time series data en una columna (en esto caso van a ser temperaturas) a lo largo del día
# y un date_time row INDEX

# Columna con los datos para el dataframe
temp_c = [8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0, 9.1, 12.8, 15.3, 19.1,
          21.2, 22.1, 22.4, 23.1, 21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]

'''
Ahora nos toca crear el date_time index. Para ello utilizaremos la función pd.date_range
Algunos de los argumentos:
start nos dice cuando queremos empezar (está en el formato ISO 8601
AÑO-MES-DÍA HH:MM:SS   Ejem 2022-09-16 08:42:23)
https://en.wikipedia.org/wiki/ISO_8601
periods nos dice cuántos valores queremos
frequency= cuanto tiempo pasa entre cada dato..
'''
date_time_index = pd.date_range(start='2022-01-01 00:00:00', periods=24, freq='H')
# Nos crea un objeto de tipo .... DatetimeIndex
# o sea, creamos 24 valores, empezando el 1 de enero de 2022 a las 00, y cada valor es una hora después del anterior
print(date_time_index)
print(type(date_time_index))
'''
DatetimeIndex(['2022-01-01 00:00:00', '2022-01-01 01:00:00',
               '2022-01-01 02:00:00', '2022-01-01 03:00:00',
               '2022-01-01 04:00:00', '2022-01-01 05:00:00',
               '2022-01-01 06:00:00', '2022-01-01 07:00:00',
               '2022-01-01 08:00:00', '2022-01-01 09:00:00',
               '2022-01-01 10:00:00', '2022-01-01 11:00:00',
               '2022-01-01 12:00:00', '2022-01-01 13:00:00',
               '2022-01-01 14:00:00', '2022-01-01 15:00:00',
               '2022-01-01 16:00:00', '2022-01-01 17:00:00',
               '2022-01-01 18:00:00', '2022-01-01 19:00:00',
               '2022-01-01 20:00:00', '2022-01-01 21:00:00',
               '2022-01-01 22:00:00', '2022-01-01 23:00:00'],
              dtype='datetime64[ns]', freq='H')
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
'''

# Ahora ya es fácil crear el panda
df_temperaturas = pd.DataFrame(data={'temp_c': temp_c}, index=date_time_index)
print(df_temperaturas)
# Ya tenemos el dataframe con la time_series de las temperaturas, acompañada del tiempo donde se realizó la medición
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

# Cuando el dataframe tieen un DatetimeIndex podemos hacer slices del data_frame fácilmente!!
# Es como siempre, con el accesor [] al que podemos poner rebanadas...
# por eejmplo, de las 6 de la mañana hasta las 3 de la tarde
print(df_temperaturas['2022-01-01 06':'2022-01-01 15'])
'''                     temp_c
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
'''
# El panda sabe que como las rows están etiquetas como time series, interpreta los strings que le damos como tiempo
# en el ISO 8601

# Cuando tenemos timeseries data podemos hacer varias cosas interesantes... por ejemplo

# Resample!!! con el parámetro rule
# Esto conlleva la reconversión del Timeindex que estamos usando...
# Con rule le decimos como queremos reconvertir los intervalos...
# Por ejemplo, para tomar intervalos de 6h en vez de los que tenemos horarios...
# Entonces sólo habría 4 grupos...
# La función resample realmente tiene muchísimas variaciones!!

resampler = df_temperaturas.resample(rule='6h')
print(type(resampler))
# <class 'pandas.core.resample.DatetimeIndexResampler'>

# Obviamente resample no puede devolvernos así como está un dataframe...
# tan solo resamplea el tiempo!!
# No puede devolvernos un data frame pq para cada grupo debemos decirle
# como calcular el valor!!!

# Tenemos muchísimas opcioens, calcular la media, sumar, max, ...
# Por ejemplo, para resamplear cada 6 horas, calculando el valor a mostrar con la media...

df_resample = df_temperaturas.resample(rule='6h').mean()
print(df_resample)
'''
                        temp_c
2022-01-01 00:00:00   6.616667
2022-01-01 06:00:00  11.016667
2022-01-01 12:00:00  21.283333
2022-01-01 18:00:00  12.016667

Ya tenemos el índice cada 6 horas, y la temperatura la media de cada grupo de 6 horas!!
O sea, el resample crea grupos... les asigna un tiempo como le digamos...
'''


# Ahora veamos cómo hacer ROLLING-WINDOW ANALYSIS
'''Se utiliza cuando los datos tienen fluctuaciones muy rápidas a corto plazo, con lo que nos intersa
suavizar esas oscilaciones...
Estas variaciones tan rápidas podrían ocurrir a corto plazo en la bolsa, 
'''
'''
Para hacer el rolling usaremos el método rolling, especificando window=tamaño para la ventana que queremos

Funciona parecido al resample... rolling() no nos devuelve un dataframe!! 
sino un objeto tipo <class 'pandas.core.window.rolling.Rolling'>

Luego, en ese objeto, aplicamos el método que queramos para suavizar, y así nos devolverá el dataframe
'''
rolling_object = df_temperaturas.rolling(window=3)
print(rolling_object)
# Rolling [window=3,center=False,axis=0,method=single]
# Por supuesto, el método rolling admite muchos más parámetros que vale la pena investigar!!

# Ahora, para obtener el dataframe, pues simplemente decirle
# el método para la función a suavizar, por ejemplo, la media.
df_suavizado = df_temperaturas.rolling(window=3).mean()
print(df_suavizado)
'''
                       temp_c
2022-01-01 00:00:00        NaN
2022-01-01 01:00:00        NaN
2022-01-01 02:00:00   7.300000
2022-01-01 03:00:00   6.766667
2022-01-01 04:00:00   6.400000
2022-01-01 05:00:00   5.933333
2022-01-01 06:00:00   5.400000
2022-01-01 07:00:00   5.066667
2022-01-01 08:00:00   6.300000
2022-01-01 09:00:00   8.966667
2022-01-01 10:00:00  12.400000
2022-01-01 11:00:00  15.733333
2022-01-01 12:00:00  18.533333
2022-01-01 13:00:00  20.800000
2022-01-01 14:00:00  21.900000
2022-01-01 15:00:00  22.533333
2022-01-01 16:00:00  22.166667
2022-01-01 17:00:00  20.666667
2022-01-01 18:00:00  18.133333
2022-01-01 19:00:00  15.933333
2022-01-01 20:00:00  13.933333
2022-01-01 21:00:00  12.433333
2022-01-01 22:00:00  11.033333
2022-01-01 23:00:00  10.100000
'''

# Como vemos, para los dos primeros valores pone NaN, ya que no existe la ventana de dimensión 3 al principio
# pq estamos empezando a obtener los datos desde dos medidas anteriores, y no existen!!!
# O se,a por defecto la ventana de un valor es ese valor y los ANTERIORES necesarios para completar la ventana

# También podemos calcular una ventana CENTRADA en nuestro valor!!
df_suavizado = df_temperaturas.rolling(window=3, center=True).mean()
print(df_suavizado)
# Ahora la ventana estará compouesta por el dato, su anterior y su posterior
# Aquí se nos generará un NaN con el primer dato (pq no tiene anterior) y con el último (pq no tiene posterior)







