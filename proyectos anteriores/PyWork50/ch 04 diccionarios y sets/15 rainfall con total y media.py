'''
Wwrite a function, get_rainfall, that tracks rainfall in a number of cities.
Users of your program will enter the name of a city;
if the city name is blank, then the function prints a report (which I’ll describe) before exiting.
If the city name isn’t blank, then the program should also ask the user how much
rain has fallen in that city (typically measured in millimeters). After the user enters
the quantity of rain, the program again asks them for a city name, rainfall amount,
and so on—until the user presses Enter instead of typing the name of a city
'''

# Si ponemos blanco, nos da el reporte con los datos del diccionario...
# Si ponemos una ciudad, pues nos pregunta el dato para completar ese valor...
# Si ya existiera, pues se suma para acumularse...

# Ahora, además de calcular el total, tenemos que calcular la media...
# para ello, por ejemplo (aunque hay más formas, como calcularla y actualizarla a cada paso...
# hay una solución guardando asociada a cada ciudad, no el total, sino una lista con todos los datos!!!
# La solución más sencilla sería con defaultdict...
# pero hagámoslo con el normal...
# es básicamente un diccionario donde los values son listas que contienen todas las medidas de cada día....

RAIN = dict()

def get_rain_fall():
    RAIN = dict()
    while True:
        city = input('Enter a city name: ').strip().lower()
        # podríamos comprobar tb si el nombre tiene letras, etc... pero no es el objetivo del ejercicio
        if not city:
            break
        else:
            lluvia = input('Cuál es la cantidad de lluvia en ml / m2 ? ')
            # también podríamos haber veriticado que todo va ok con un try
            # quiza´s es esta más sencillo, pq podíamos convertir incluso a float!
            if lluvia.isdigit():
                lluvia = int(lluvia)
            else:
                print('No has introducido una cantidad válida....')
                continue
            if not city in RAIN:
                RAIN[city] = []
            RAIN[city].append(lluvia)

            # La opción que puse al principio es un poco peor...
            '''
            if city in RAIN.keys():
                RAIN[city].append(lluvia)   # agregamos un ítem a la lista con la lluvia de ese día...
            else:  # la ciudad no existe!! pues iniciamos la lista!!!
                RAIN[city] = [lluvia]
            '''
            # No sirve similar al ejericio original
            # RAIN[city] = RAIN.get(city, []).append(lluvia)
            # porque el método get al aplicarse en RAIN, si no existe devuelve []
            # y luego a esta lista vacía se le agrega un valor...
            #       PERO EL MÉTODO APPEND NO DEVUELVE EL VALOR   !!
            # QUIZás serviría con  list ( ................................)
        '''
        Con el defaultdict sería....
        from collections import defaultdict
        RAIN = defaultdict(list)  para crearlo
        RAIN[city].append(lluvia)   para actualizar!!!
        '''
    for city, lista_lluvia in RAIN.items():
        print(40*'--')
        print(f'La cantidad de lluvia acumulada en "{city}" es de {sum(lista_lluvia)} ml/m2')
        print(f'La lluvia por días ha sido {lista_lluvia}')
        media = float(sum(lista_lluvia)) / len(lista_lluvia)
        print(f'La media diaria ha sido de {media:.2f} ml/m2')
        print(40*'--')



get_rain_fall()