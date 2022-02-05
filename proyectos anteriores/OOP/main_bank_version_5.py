from bank import *

oBank = Bank()

joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print("La cuenta de Joe es la id ", joesAccountNumber)

maryAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPassword')
print("La cuenta de Mary es la id ", maryAccountNumber)

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press c to close an account')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] # grab the first letter
    print()

    if action == 'b':
        oBank.balance()

    elif action == 'd':
        oBank.deposit()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
