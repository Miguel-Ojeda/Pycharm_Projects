import pyinputplus as pyip

# Let’s create a program that poses 10 multiplication problems to
# the user, where the valid input is the problem’s correct answer

import random
import time
numberOfQuestions = 10
correctAnswers = 0

# vamos a elegir números al azar para que en cada iteración nos tenga
# que contestar el  resultado de la multipliacion de los dos números eleigods

for questionNumber in range(numberOfQuestions):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    prompt = f'Cuántos es {num_1} x {num_2} = '

    # queremos que al preguntarle, sólo sea válida la respuesta correcta...
    # es sencillo, simplemente tenemos que utilizar la función
    # inputStr() con el parámetro allowRegexes... dando como único valor permmitido
    # la expresión regular que consiste en el valor correcto de la multiplicación...
    # y que empiece y termine con ese valor... para que no pueda introducir otra cosa...
    # para ello utilizaremos....: la string .... ^valor$
    # recordar del chap 7 que ^ indica que el inicio de la cadena debe ser el que le digamos
    # y $ lo mismo, que para hacer match la cadena debe terminar...
    # con esto tenemos que lo único que admitiremso será el resultado correcto...

    resultado_correcto = str(num_1 * num_2)
    regex = f'^{resultado_correcto}$'

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=[regex],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3,
                      )
                      # cada regex bloqueada lleva en su tupla un mensaje asociado a mostrar
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:  # esto ocurre si no hay excepciones... o sea, el usuario acierta antes del límite
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)  # Brief pause to let user see the result.

print(f'Has acertado {correctAnswers} de {numberOfQuestions} preguntas')
