from random import randint

nombre = input("Hello! What's your name? ")

numero_secreto = randint(1,20)

print("Bueno, "+nombre+', I am thinking of a number between 1 and 20')

num_intento = 1
MAX_INTENTOS = 6

while num_intento <= MAX_INTENTOS:

    # print(f"Take a guess.Número de intento {num_intento} ------>  ")
    numero = input(f"Take a guess.Número de intento {num_intento} ------>  ")
    numero = int(numero)
    if numero == numero_secreto:
        break
    elif numero < numero_secreto:
        print("Your guess is too low.")
        num_intento += 1
    elif numero > numero_secreto:
        print("Your guess is too high.")
        num_intento += 1

if numero == numero_secreto:
    print(f"Felicidades, has acertado mi número, {numero_secreto}, utilizando para ello {num_intento} intentos")
else:
    print(f"Vaya, lo siento, el número máximo de intentos es {MAX_INTENTOS}")
    print(f"El número en el que había pensado era el {numero_secreto}")