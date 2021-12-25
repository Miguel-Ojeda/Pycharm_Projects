from account import *

# cuando tenemos un número indeterminado de objetos, es mejor crear una lista de objetos...
accounts_list = []


oAccount = Account('Joe', 100, 'JoesPassword')
accounts_list.append(oAccount)
print("La cuenta de Joe es la id 0")


oAccount = Account('Mary', 12345, 'MarysPassword')
accounts_list.append(oAccount)
print("La cuenta de Mary es la id 1")

accounts_list[0].show()
accounts_list[1].show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
accounts_list[0].deposit(50, 'JoesPassword')
accounts_list[1].withdraw(345, 'MarysPassword')
accounts_list[1].deposit(100, 'MarysPassword')

# Show the accounts
accounts_list[0].show()
accounts_list[1].show()


# creando una cuenta con datos suministrador por el usuario...
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

oAccount = Account(userName, userBalance, userPassword)
accounts_list.append(oAccount)

# Show the newly created user account
print('Created new account, account number is 2')
accounts_list[2].show()

# Let's deposit 100 into the new account
accounts_list[2].deposit(100, userPassword)
usersBalance = accounts_list[2].getBalance(userPassword)
print()
print("After depositing 100, the user's balance is:", usersBalance)
# Show the new account
accounts_list[2].show()
