# Utilizaremos el módulo para subprocesos...
# Para empezar un programa simplemente... subproceess.Popen()
# Iniciará el proceso que le digamos e inmediatamente retornará!!
# Funciona simplemente como un lanzador del programa que le digamos...
# hasta podremos lanzar varias instancias del programa

import subprocess
subprocess.Popen('C:/Windows/System32/calc.exe')
subprocess.Popen('C:/Windows/explorer.exe "C:\\Users\\Angel Ojeda\\Documents\\Miguel"')

'''
El objeto de retorno es un objeto Popen, en el que podemos utilziar dos métodos: poll() y wait()

El método wait() bloquea nuestro programa hasta que el que hemos lanzado haya terminado

El método poll retorna rápido..-- > nos da None si el programa que lanzamos todavía está en marcha
Si ya ha terminado nos retorna un entero con el exit code (0 si fue bien todo, o otro número para indicar
el error....
'''

# Ejemplo con wait(): lanzamos el mspaint y esperamos hasta que lo cerremos....
paint_process = subprocess.Popen('C:/Windows/system32/mspaint.exe')
paint_process.wait()
# Esto provoca que el programa se detenga hasta que acabe el proceso paint!!!

print('Ya ha terminado MSPAINT')
