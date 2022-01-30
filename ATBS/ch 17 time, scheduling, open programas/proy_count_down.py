#! python
import sys
import time
import subprocess

# Primero veamos si nos han pasado un número como argumento adicional... entonces esos serán los segundos
if len(sys.argv) == 2 and sys.argv[1].isdecimal():
    time_left = int(sys.argv[1])
else:
    time_left = 60

while time_left > 0:
    print(time_left, end='-')
    time.sleep(1)
    time_left = time_left - 1

# Ahora, reproducimos el fichero alarm.wav
# para ello utilizaremos Popen con la opción start (es el iniciador de programas en windows, en mac y linux son otros<9
subprocess.Popen(['start', 'files/alarm.wav'], shell=True)