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
