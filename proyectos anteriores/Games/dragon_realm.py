import random
import time

def display_intro():
    print('''\nYou are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()


def choose_cave():
    cueva_elegida = ''
    # while cueva_elegida != '1' and cueva_elegida != '2':
    while cueva_elegida not in ['1','2']:
        cueva_elegida = input("A qué cueva te gustaría ir? (1/2) --> ")
    return cueva_elegida

def checkCave(chosenCave):
    print(f'You approach the cave {chosenCave}...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

def check_continua():
    continua = input("Continúas jugando? (y/n) --> ")
    if continua == 'yes' or continua == 'y':
        return True
    else:
        return False

play_again = True
while play_again:
    display_intro()
    cueva_elegida = choose_cave()
    checkCave(cueva_elegida)
    play_again = check_continua()



