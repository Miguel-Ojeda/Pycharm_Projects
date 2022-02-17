'''
EXERCISE 14 ■ Restaurant

In this exercise, I want you to create a new constant dict, called MENU, representing
the possible items you can order at a restaurant.

The keys will be strings, and the values will be prices (i.e., integers).

You should then write a function, restaurant, that asks the user to enter an order:
 If the user enters the name of a dish on the menu, the program prints the price
and the running total. It then asks the user again for their order.
 If the user enters the name of a dish not on the menu, the program scolds the
user (mildly). It then asks the user again for their order.
 If the user enters an empty string, the program stops prompting and prints the
total amount.
For example, a session with the user might look like this:
Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order: elephant
Sorry, we are fresh out of elephant today.
Order: <enter>
Your total is 17
'''

MENU = {'pasta': 10, 'pizza': 8, 'paella': 11, 'te': 2, 'cafe': 1, 'cola': 2.50, 'bocata': 3.50, 'sandwich': 2.50}

def restaurant():
    total = 0
    while True:
        pedido = input('Order: ').lower().strip()
        if not pedido:
            break
        elif pedido not in MENU.keys():
            print(f'Lo siento, en nuestro menú no tenemos "{pedido}".')
            continue
        else:
            precio = MENU[pedido]
            total += precio
            print(f'El precio de {pedido} es {precio}. De momento el total es {total}')


    print(f'Your total is {total}')


restaurant()