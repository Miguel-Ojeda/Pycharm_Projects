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
            # Otra opción a usar el get para asegurarnos de que existe, o si no, que nos devuelva 0
            # sería utilziar un collections.defaultdict que se inicializa automáticamente con un
            # valor por defecto cuando utilizamos alguna key que todavía no estaba utilizada!!
            RAIN[city] = RAIN.get(city, 0) + lluvia

        '''
        La verisón con el defaultdict sería resumida...
        from collections import defaultdict
        RAIN = defaultdict(int)  --> esto crea un defauldict que, cuando no existe valor para la clave
                                     le asigna el valor nulo según el type, en este caso, para int, sería 0
        Luego, a la hora de actualizar el valor es simplemente...
        RAIN[city] += lluvia
        NO HACE FALTA COMPROBAR SI EXISTE ANTES, no da error (como sucede con el diccionario normal si no usamos get)
        sino que, si no existe, pues es como si valiera 0
        '''
    for city, lluvia in RAIN.items():
        print(f'La cantidad de lluvia acumulada en "{city}" es de "{lluvia} ml / m2')


get_rain_fall()