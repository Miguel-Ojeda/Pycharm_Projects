# https://realpython.com/python-type-checking/
# muy bueno!!


import math
'''
¿Cómo añadir type hints a una función?
Type hints: indicadores de tipos... es algo opcional, el intérprete no los tiene en cuenta!!
Lo podemos hacer de varias formas:
con anotaciones (lo recomendado y moderno)
y con type comments (compatible para python antiguo)
Son sólo indicaciones, el intérprete las ignorará, aunque nos avisarán los ides, linters y mypy
'''

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


'''Aquí está como se indican tipos de una función:
def headline(text: str, align: bool = True) -> str:
'''
headline('Hola como estás', align='Falso')
'''
Pycharm nos deja poner lo anterior, aunque destaca align='Falso' para indicarnos
que detecta tipo equivocado, ...  
Nos da mensaje... Expected type 'bool', got 'str' instead!!
pese a todo_, el intérprete ejecuta el código sin problema...
como align es una cadena no nula se interpretará como True y ya está
'''
'''
Si queremos hacer un static type checking podemos usar Mypy
pip install mypy y luego, para comprobar el script
mypy script...
Por ejemplo, cuando lo hago con este fichero... nos dice...


$ mypy 'Type checking.py'
Type checking.py:14: error: Argument "align" to "headline" has incompatible type "str"; expected "bool"
Found 1 error in 1 file (checked 1 source file)
'''

'''Vale la pena utilizar type hinsts??

                POSITIVO:
type hints help catch certain errors
Type hints improve IDEs and linters
Type hints help you build and maintain a cleaner architecture
In libraries that will be used by others, especially ones published on PyPI, type hints add a lot of value.
Other code using your libraries need these type hints to be properly type checked itself.
For examples of projects using type hints see cursive_re, black, our own Real Python Reader, and Mypy itself.
In bigger projects, type hints help you understand how types flow through your code, and are highly recommended.
Even more so in projects where you cooperate with others.

                NEGATIVO
Type hints take developer time and effort to add
Type hints introduce a slight penalty in start-up time.
If you need to use the typing module the import time may be significant, especially in short scripts.
Type hints add little value in short throw-away scripts.

Lo ideal, pues, es utilizar GRADUAL TYPING... (poco a poco, en lo más importante, o el código
más complicado que más se va a beneficiar de esto...)
'''

'''
Annotations
A partir de Python 3.0, son una forma de asociar expresiones arbitrarias
a los argumentos de funciones y el tipo de retorno de funciones.
Es lo que usamos para añadir los type hints, como hemos visto antes...

También, de forma similar, se puede utilizar las anotaciones para indicar
type hints en variables dentro de una función...
'''

# Podemos tener acceso a todas las anotaciones de un módulo utilizando
# el diccionario __anotattions__

pi: float = 3.142


def circumference(radius: float) -> float:
    return 2 * pi * radius

print(circumference.__annotations__)
# {'radius': <class 'float'>, 'return': <class 'float'>}

'''
Type Comments
Observar que las anotaciones son nuevas, a partir de Python 3
en python anteriores tendríamos que usar Type comments
Nos sirven para indicar type hints en Python anteriores (y en los modernos, claro)
import math
La anterior función, quedaría, con Type comments...
'''


def circumference_2(radius):
    # type: (float) -> float
    return 2 * math.pi * radius

# Observar que Pycharm lo detecta!!!
circumference_2('hola')
# Nos dice, expected type 'float', got 'str' instead

# Lo detecta mypy??   SÍ, tb...
'''
$ mypy 'Type checking.py'
Type checking.py:17: error: Argument "align" to "headline" has incompatible type "str"; expected "bool"
Type checking.py:96: error: Argument 1 to "circumference_2" has incompatible type "str"; expected "float"
Found 2 errors in 1 file (checked 1 source file)
'''
# IMPORTANTE: esto son simplemente comentarios para el intérprete, por tanto
# no se van a incorporar a __anottations__

'''IMPORTANTE:
para indicar type hints usar obviamente, las anottations en lugar de los type comments
pq son más sencillas y claras, y el intérprete las recoge en anottations...
'''

'''
                        MÓDULO TYPING   (tipos compuestos)



Hemos visto que podemos indicar type hints con anotaciones así...

names: list = ["Guido", "Jukka", "Ivan"]
version: tuple = (3, 7, 1)
options: dict = {"centered": False, "capitalize": True}
'''

'''
Pero, no está todo indicado...
Por ejemplo, names es una lista, sí, pero, qué tipo tiene names[0] ??
version es una tupla, vale, pero qué tipo tiene version[2]
que´tipo tiene options['centered']
'''

'''
Para hacer anotaciones más exhaustivas hay que utilizar el módulo typing
Nos sirve para indicar tipos de elementos correspondientes a tipos compuestos'''

# Usando el ejemplo anterior, podemos hacer una anotación completa así!!
from typing import Dict, List, Tuple
names: List[str] = ["Guido", "Jukka", "Ivan"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}

'''
En typing se incluyen además Counter, Deque, FrozenSet, NamedTuple, and Set
y muchas más cosas que iremos viendo
'''
