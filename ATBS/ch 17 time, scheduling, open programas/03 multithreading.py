# Por defecto, los programas Python tienen sólo un hilo!!
# Para crear un nuevo hilo, habrá que crear un objeto tipo thread...

import threading
import time


def take_a_nap():
    time.sleep(5)
    print('despierta')


print('Start of program.')
thread_obj = threading.Thread(target=take_a_nap)
# target es un objeto callable, que va a ser luego ejecutado por el método run
thread_obj.start()  # sólo se puede llamar una vez el start por objeto thread...
print('End of program')

'''
El resultado es éste!!.
Start of program.
End of program.
Wake up!

O sea, empieza el program, el thread original.. imprime start of programa...
Lanza un hilo secundario
Sigue el original y termina con print end of program
Luego termina el hilo secundario que lanzamos imprimiendo despierta!!

Cuidado: hay que poner take_a_nap.... a veces pycharm nos añade los paréntesis y entonces, lógicamente, no sirve
'''