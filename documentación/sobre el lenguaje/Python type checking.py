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
# circumference_2('hola')
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
import random

# Otro ejemplo para anotar una función de game_001
SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


'''
Observar, que para anotar las tuplas, indicaremos Tuple[t1, t2, t3...]
En cambio, con listas, son mutables, no podemos saber el número de elementos!!
por tanto, lo único que podríamos hacer, si son todas del mismo tipo
sería poner List[type] ... o si no sabemos pues list simplemente
'''

# Qué pasa si nuestra función utiliza algún tipo de secuencia (lista, tupla, ...)
# pero nos da igual realmente el tipo ....
# Pues usamos typing.sequence!!!
from typing import Sequence


def square(elems: Sequence[float]) -> List[float]:
    return [x ** 2 for x in elems]


'''
Type Aliases

Si anotamos esta función...
def deal_hands(deck):
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
    
quedaría...

def deal_hands(
    deck: List[Tuple[str, str]]
) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
    
ESTO ES REALMENTE HORRIBLE... para solucionarlo podemos usar type aliases...
O sea, damos alias para referirnos de forma más sencilla a tipos compuestos
'''
from typing import List, Tuple

# Creamos dos alias
Card = Tuple[str, str]
Deck = List[Card]
print(Card)
# typing.Tuple[str, str]
print(Deck)
# typing.List[typing.Tuple[str, str]]

# Ahora ya anotamos cómodamente...
# La función anterior...
def create_deck_2(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

# y la nueva...

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])


# También debemos anotar (si queremos claro) el tipo de retorno
# cuando no se retorna nada (siempre se retornará en este caso None)
def play(player_name: str) -> None:
    print(f"{player_name} plays")

ret_val = play("Filip")
# Aquí nos avisa Pycharm: function play doesn't return anything

# También podemos anotar funciones que nunca retornan con un return
from typing import NoReturn

def black_hole() -> NoReturn:
    raise Exception("There is no going back ...")


'''             Any

En el juego de cartas, tenemos esta función
def choose(items):
    """Choose and return a random item"""
    return random.choice(items)
choose() works for both lists of names and lists of cards
(and any other sequence for that matter).
One way to add type hints for this would be the following:
'''
from typing import Any


def choose(items: Sequence[Any]) -> Any:
    return random.choice(items)

# Esta solución tiene algunos problemas, que mejoraremos...

'''SUBTIPOS
One important concept is that of subtypes.
Formally, we say that a type T is a subtype of U if the following two conditions hold:
1: Every value from T is also in the set of values of U type.
1. Todos los valores del subtipo están en el tipo
2: Every function from U type is also in the set of functions of T type.
2. Toda función del Tipo es tb. función del subtipo

The importance of subtypes is that a subtype can always pretend to be its supertype.
For instance, the following code type checks as correct:
def double(number: int) -> int:
    return number * 2
print(double(True))  # Passing in bool instead of int
'''

'''COVARIANT, CONTRAVARIANT, INVARIANT
What happens when you use subtypes inside composite types?
For instance, is Tuple[bool] a subtype of Tuple[int]?
Si lo fuera, sería válido utilizar Tuple[bool] cuando esperamos Tuple[int]
The answer depends on the composite type, and whether that type is covariant,
contravariant, or invariant.

Tuple is covariant.
This means that it preserves the type hierarchy of its item types:
Tuple[bool] is a subtype of Tuple[int] because bool is a subtype of int.

List is invariant.
Invariant types give no guarantee about subtypes.
While all values of List[bool] are values of List[int],
you can append an int to List[int] and not to List[bool].
In other words, the second condition for subtypes does not hold,
and List[bool] is not a subtype of List[int].

Callable is contravariant in its arguments.
This means that it reverses the type hierarchy.
You will see how Callable works later, but for now think of Callable[[T], ...]
as a function with its only argument being of type T.
An example of a Callable[[int], ...] is the double() function defined above.
Being contravariant means that if a function operating on a bool is expected,
then a function operating on an int would be acceptable.

No hace falta entender todo esto, pero básicamente lo importante es tener claro
que todo esto de subtipos 
'''
'''
Consistent Types
The type T is consistent with the type U if T is a subtype of U or either T or U is Any.
This means that you can use Any to explicitly fall back to dynamic typing, describe types that are too complex to describe in the Python type system, or describe items in composite types.
For instance, a dictionary with string keys that can take any type as its values
can be annotated Dict[str, Any].
'''

'''
Type Variables
A type variable is a special variable that can take on any type, depending on the situation.
Nos deja definir un nuevo tipo!!!

Let’s create a type variable that will effectively encapsulate the behavior of choose():
'''
# Ahora, nuestra función podría quedar mejor así... pq si, el tipo de variable
# que le damos es una secuencia de un tipo, pues la salida será del mismo tipo
'''
from typing import Sequence, TypeVar
Choosable = TypeVar("Choosable")

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
reveal_type(name)
'''

# You can constrain type variables by listing the acceptable types:
# Ahora queda mucho mejor todo!!
'''
# choose.py
import random
from typing import Sequence, TypeVar

Choosable = TypeVar("Choosable", str, float)

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

reveal_type(choose(["Guido", "Jukka", "Ivan"]))
reveal_type(choose([1, 2, 3]))
reveal_type(choose([True, 42, 3.14]))
reveal_type(choose(["Python", 3, 7]))
'''
# Ahora, ya queda claro que Choosable sólo puede ser str o float!!
# que es lo que queríamos...





