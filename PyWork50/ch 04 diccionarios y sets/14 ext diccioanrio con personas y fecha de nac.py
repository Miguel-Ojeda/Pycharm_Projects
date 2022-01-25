'''
Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects
https://docs.python.org/3/library/datetime.html?#module-datetime

Ask the user to enter the name of someone in your family, and have the
program calculate how many days old that person is.
'''
from datetime import date

# Diccionario que mantiene el usuario y la clave de los usuarios...
BIRTH_DAY = {'iris': date(1941, 9, 1), 'carlos': date(1971, 8, 21),
         'miguel': date(1968, 9, 16), 'angel': date(1932, 5, 6),
         'mariate': date(1965, 12, 27), 'joel': date(1990, 8, 10)}

# Para traducir el día de la semana que nos devuelve isoweekday()
# Lunes es un 1, etc
DIAS_SEMANA = {1: 'lunes', 2: 'martes', 3: 'miércoles', 4: 'jueves', 5: 'viernes', 6: 'sábado', 7: 'domingo'}

while True:
    persona = input('Escribe el nombre de un familiar: ').strip().lower()
    if not persona:
        break
    elif persona not in BIRTH_DAY.keys():
        print('Ufff, no conozco a esa persona...')
    else:
        nacimiento = BIRTH_DAY[persona]
        dias_vividos_v1 = date.today() - nacimiento      # ES UN timedelta
        dias_vividos_v2 = date.today().toordinal() - nacimiento.toordinal()  # Es un entero normal
        # print(type(dias_vividos_v1))
        # print(type(dias_vividos_v2))
        dia_semana_nacio = DIAS_SEMANA[nacimiento.isoweekday()]
        print(f'{persona.capitalize()} nació el {nacimiento}, un {dia_semana_nacio}')
        print(f"Ha vivido hasta el momento {dias_vividos_v2:,} días")


