'''
Python Tricks 8.3 Peeking Behind the Bytecode Curtain
'''

def greet(name):
    return 'Hello, ' + name + '!'

'''Cada función tiene un __code__ atributo... con el que podemos averiguar varias cosas...
Por ejemplo: 
    co_code (el código objeto que se crea, en formato máquina)
    co_consts: las constantes que se almacenan
    co_varnames: las variables
'''

print(greet.__code__.co_code)
# b'd\x01|\x00\x17\x00d\x02\x17\x00S\x00'
print(greet.__code__.co_consts)
# (None, 'Hello, ', '!')
print(greet.__code__.co_varnames)
# ('name',)

'''
Las constantes y el código se almacenan en distinto lugar por eficiencia... cuando toque, pues el código
cargará la constante donde esté... así, si una constante se utiliza en 20 sitios, pues sólo estará
ocupando memoria en un sitio... simplemente las guarda en una lookuptable aparte, y el código accede
a la constante que requiere cargándola utilizando el índex apropiado
Lo mismo sucede con los nombres de las variables!!!
'''

# De todas formas, el código __code__.co_code no está hecho para leerlo por humanos
# Para enterarnos de verdad debemos utilziar el módulo dis

import dis
codigo = dis.dis(greet)  # Ideal en el REPL simplemente
print(codigo)
'''
Recordar que todo esto son instrucciones para cargar en la VIRTUAL MACHINE, que es una estructura del tipo
stack, en la que sólo podemos hacer push o pop...

6           0 LOAD_CONST        1 ('Hello, ')
            # Carga en el stack de la VM la constante de índice 1 (hello)
            2 LOAD_FAST         0 (name)
            # Esto carga (push) el contennido de la variable de index 0, name, en el stack como elemento superior
            # Por ejemplo, supongamos que la variable name, tuviera el valor 'Miguel'      
            4 BINARY_ADD
            # Pops los dos ítems del stack, los concatena y los vuelve a meter...
            # o sea, ahora arriba en el stack está 'Hello, Miguel'                      
            6 LOAD_CONST        2 ('!')
            # Carga la constante de index 2, o sea, '!'
            8 BINARY_ADD
            # Hace pop con los dos valores que están, los concatena --> 'Hello, Miguel!' y vuelve a colocarlo arriba
            10 RETURN_VALUE
'''

