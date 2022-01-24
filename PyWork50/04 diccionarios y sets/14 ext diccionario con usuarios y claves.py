'''
Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry.
(Note: This is a nice little exercise, but please never store unencrypted passwords. It’s a major security risk.)
'''

# Diccionario que mantiene el usuario y la clave de los usuarios...
LOGIN = {'iris': 'iris-clave', 'carlos': 'carlos-clave', 'miguel': 'miguel-clave',
         'angel': 'angel-clave', 'mariate': 'mariate-clave', 'joel': 'joel-clave'}

while True:
    login = input('Introduzca su nombre de usuario: ').strip()
    if not login:
        # Apretó enter o espacios  ---> salimos
        break
    elif login not in LOGIN.keys():
        print('En nuestro sistema no existe ningún usuario con ese nombre')
        continue
    clave = input('Introduzca su clave: ').strip()
    if clave == LOGIN[login]:
        print(f'Bienvenido al sistema, {login}')
    else:
        print(f'Acceso rechazado, clave errónea')
