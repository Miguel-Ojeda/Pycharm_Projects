# For this exercise, write a Python function, format_sort_records, that takes the
# PEOPLE list and returns a formatted string that looks like the following:
# Trump Donald 7.85
# Putin Vladimir 3.63
# Xi Jinping 10.60

import operator

PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]

# ordenamos por apellidos y nombre...
for apellidos, nombre, tiempo in sorted(PEOPLE, key=operator.itemgetter(1, 0)):
    print(apellidos.ljust(10), nombre.ljust(10), f'{tiempo:.2f}'.rjust(5))

