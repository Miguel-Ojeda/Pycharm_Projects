''' ¿Pero y qué pasa si la función que queremos invocar con un nuevo hilo necesita que le pasemos argumentos???

Se puede pasar al crear el objeto thread... en args pasaremos una lista de argumentos, y en kwargs un diccioanrio
con los keyword arguments...
'''

import threading
import time

# sleep_con_print(1, 2, 3, 4, sep=' /// ')
def sleep_con_print(*args, **kwargs):
    time.sleep(2)
    # print(*args, sep=kwargs['sep'])
    print(*args, **kwargs)
    print('finalizado sleep con prin')

print('empiezo el programa / hilo principal')
thread = threading.Thread(target=sleep_con_print, args=[1, 2, 3, 4], kwargs={'sep': ' XXXX '})
thread.start()
print('termino el programa (hilo principal)')


