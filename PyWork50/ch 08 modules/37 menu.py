"""
write a new module called “menu” (in the file menu.py).

The module should define a function, also called menu.
The function takes any number of keyvalue pairs as arguments.
Each value should be a callable, a fancy name for a function or class in Python.

When the function is invoked, the user is asked to enter some input.

* If the user enters a string that matches one of the keyword arguments, the function associated
with that keyword will be invoked, and its return value will be returned to menu’s caller.
* If the user enters a string that’s not one of the keyword arguments, they’ll be given an
error message and asked to try again.

The idea is that you’ll be able to define several functions, and then indicate what user
input will trigger each function:

from menu import menu
def func_a():
return "A"
def func_b():
return "B"
return_value = menu(a=func_a, b=func_b)
print(f'Result is {return_value}')

In this example, return_value will contain A if the user chooses a, or B if the user
chooses b. If the user enters any other string, they’re told to try again. And then we’ll
print the user’s choice, just to confirm things
"""

# Haremos esto, pues, en el módulo menu.py