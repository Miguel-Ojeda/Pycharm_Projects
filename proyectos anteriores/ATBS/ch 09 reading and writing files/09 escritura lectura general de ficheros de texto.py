""" Se hace con lo clásico...
open()
operaciones...
close()

Mucho mejor, utilizar contextos, pq si lo hacemos con el método clásico
si ocurriera algo que impidiera el close (una excepción no atendida, un olvido de hacer close(), etc)
se quedaría el recurso abierto

Para utilizar el contexto es supersencillo
With lo que hace es crear un contexto de forma que, al salir del contexto, automáticamente,
el objeto con el que se entró (en este caso, un fichero devuelto con open())
es liberado automáticamente!!!

with open(----) as file:
    operaciones a realizar...

Esto garantiza que, pase lo que pase, como, obviamente vamos a salir del contexto,
siempre, pase lo que pase, se va a liberar el recurso!!!
"""
from pathlib import Path
# La función open(string_fichero) devuelve un objeto tipo File que tiene métodos para leer, etc...
# Por supuesto, tb open acepta un objeto path, pq automáticamente el objetopath se convertirá a string
# Para este ejemplo, hemos creado en Documentos un fichero con un soneto de Shakespeare...
path_soneto = Path.home() / 'Documents' / 'soneto_29.txt'

# FORMA 1
with open(path_soneto) as file:
# También podríamos haber hecho, evidentemente
# with open('C:/Users/Miguel/Documents/el_quijote.txt'):
# Como no le hemos dicho nada, el fichero se abre en modo lectura... 'r'
# Lo podíamos haber explicitado incluso así... open(path_quijote, 'r')
    '''
Ahora podemos utilizar varios métodos sobre este objeto fichero...
fichero.read() lee TODO EL CONTENIDO DEL FICHERO y devuelven una string con todo el contenido...
fichero.readlines() devuelve una lista donde cada item es una línea del fichero...
    '''
    contenido = file.read()
    # O sea, leemos TODO_ el fichero de golpe!!

print(contenido)

# FORMA 2
# Otra forma con readlines...
with open(path_soneto) as file:
    lineas = file.readlines()
    # Esto es una lista donde cada item es una línea
    # Cada item/línea termina de por si ya con newline, excepto la última línea!!!!
for num_linea, linea in enumerate(lineas):
    print(f'Línea {num_linea}: {linea}', end='')  # Ponemos end nada pq ya de por sí la línea acaba en newline

# FORMA 3
print('\nForma 3... iterando en el fichero... es por líneas')
with open(path_soneto) as file:
    for linea in file:
        print(linea, end='')  # fin nada pq ya la línea incluye el newline

# ---------------------AHORA VEAMOS LA ESCRITURA---- es similar...
# Hay que abrirlo para escribir, hay que decirlo... podemos elegir el
# mode append 'a' (añade contenido) o el modo de escritura 'w' ... que machaca lo que haya!!!
# Evidentemente si el fichero no existiera, ambos modos, 'w' y 'a' hacen lo mismo, crear uno nuevo!!
# Si ya existiera, 'a' añade al final, mientras que 'w' machaca e inicia un nuevo fichero...

# IMportante, al escribir, no se añade automáticamente la nueva línea!!
path = Path.home() / 'spam.txt'
with open(path, 'w') as file:
    file.write('Escribo una línea y paso a la siguiente\n')
    file.write('Ahora la segunda línea pero sigo en la segunda... ')  # Aquí no pongo newline!!!
    file.write('y ahora sigo un poco más en la segunda línea!!')
# El resultado es --->
# Escribo una línea y paso a la siguiente
# Ahora la segunda línea pero sigo en la segunda. y ahora sigo un poco más

with open(path, 'a') as file:
    file.write('termino la segunda\n')
    file.write('y paso a la tercera...  ')  # Aquí no pongo newline!!!
    file.write('sigo en la tercera y fin.')





