from account import *

# cuando tenemos un número indeterminado de objetos, es mejor crear una lista de objetos...
accounts_dict = {}
next_account_number = 0

oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = next_account_number
accounts_dict[joesAccountNumber]= oAccount
print("La cuenta de Joe es la id ", joesAccountNumber)
next_account_number += 1

oAccount = Account('Mary', 12345, 'MarysPassword')
maryAccountNumber = next_account_number
accounts_dict[maryAccountNumber]= oAccount
print("La cuenta de Mary es la id ", maryAccountNumber)
next_account_number += 1

accounts_dict[joesAccountNumber].show()
accounts_dict[maryAccountNumber].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accounts_dict[joesAccountNumber].deposit(50, 'JoesPassword')
accounts_dict[maryAccountNumber].withdraw(345, 'MarysPassword')
accounts_dict[maryAccountNumber].deposit(100, 'MarysPassword')

# Show the accounts
accounts_dict[joesAccountNumber].show()
accounts_dict[maryAccountNumber].show()


# creando una cuenta con datos suministrador por el usuario...
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

oAccount = Account(userName, userBalance, userPassword)
newAccountnumber = next_account_number
accounts_dict[newAccountnumber] = oAccount
print('Created new account, account number is ', newAccountnumber)
next_account_number += 1

# Show the newly created user account
accounts_dict[newAccountnumber].show()

# Let's deposit 100 into the new account
accounts_dict[newAccountnumber].deposit(100, userPassword)
usersBalance = accounts_dict[newAccountnumber].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# Show the new account
accounts_dict[newAccountnumber].show()


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
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
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = accounts_dict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('*** Deposit ***')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter the password: ')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        oAccount = accounts_dict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print('Your new balance is:', theBalance)

    elif action == 'o':
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for this account? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accounts_dict[nextAccountNumber] = oAccount
        print('Your new account number is:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == 's':
        print('Show:')
        for userAccountNumber in accounts_dict:
            oAccount = accounts_dict[userAccountNumber]
            print(' Account number:', userAccountNumber)
            oAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Please enter the amount to withdraw: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Please enter the password: ')
        oAccount = accounts_dict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
        if theBalance is not None:
            print('Withdrew:', userWithdrawalAmount)
            print('Your new balance is:', theBalance)

    else:
        print('Sorry, that was not a valid action. Please try again.')
        print('Done')
