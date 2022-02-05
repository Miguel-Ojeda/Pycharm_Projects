import time

'''
Queremos escribirnos un stopwatch cronómetro que haga...:
1.  Track the amount of time elapsed between presses of the enter key,  
    with each key press starting a new “lap” on the timer.
2.  Print the lap number, total time, and lap

Para conseguir esto, tenemos que manejar la KeyboardInterrupt
Por tanto, nuestro código deberá ir métido en un try sin fin (imagino)
'''


input('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
print('empezamos...')
vueltas = 0
inicio_vuelta = time.time()

try:
    while True:
        input()
        fin_de_vuelta = time.time()
        elapsed_time = fin_de_vuelta - inicio_vuelta
        vueltas += 1
        print(f'Total vueltas: {vueltas} / tiempo última vuelta: {round(elapsed_time, 2)}')
        inicio_vuelta = fin_de_vuelta
except KeyboardInterrupt:   # O sea, apretó control - C que es para interrumpir un programa
    # Handle the Ctrl-C exception to keep its error message from displaying
        print('Hasta luego')







