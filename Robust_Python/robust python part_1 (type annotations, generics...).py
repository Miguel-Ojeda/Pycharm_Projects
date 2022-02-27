"""
LIBRO ROBUST PYTHON
Fantástico, esto es de la parte primera, que trata de transmitir información,
comunicar, utilizando los tipos...
"""
'''
Optional se usa cuando queremos apuntar que, por ejemplo, el valor a retornar es de un determinado tipo
o simplemente None.
'''
import random
def dispense_frank_v2() -> Optional[Frank]:
    if random.random() <= 0.8:
        return Frank('frankfourt')
    else:
        return None

'''
En lugar de Optional[Frank] podíamos haber puesto también Frank | None
o Union[Frank, None]

Lo bueno es que el entorno nos avisa de fallos.
Por ejemplo, si queremos usar el método XXX en el objeto devuelto, nos avisa
que None no tiene definido ese método.

Lo mismo haría mypy (si usarmos --strict-optional), con lo que nos obliga a tener
en cuenta los casos en los que el objeto es None (es como un chivato que nos avisa
que puede haber peligro)
'''

# ---------------------------  U n i o n
'''
Union se usa cuando el tipo puede ser uno de varios...
Union type; Union[X, Y] is equivalent to X | Y and means either X or Y.
'''
from typing import Union
def hora_es(entero: int) -> Union[int, str]:
# Equivalente a def hora_es(entero: int) -> int | str:
    if entero < 18:
        return entero
    else:
        return 'NOCHE'

# ----------------------------  L i t e r a l    T y p e s
'''
Literal Types
Podemos utilizar esto para costreñir todavía más el tipo...
Por ejemplo, queremos que sea enteror, pero unos valores concretos...
O algunas cadenas sólo....
'''
from typing import Literal

@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool

@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: set[Literal["Mustard", "Ketchup"]]
'''
Aquí, instruímos al typechecker (o a pycharm o al IDE) para que
sepa los valores que es válido que tome la variable

Por supuesto, nada impide ejecutar el código si esto no es así
Sólo son type annotations que sirven para indicar type hints
Pero Todo_ es opcional
'''
# ---------------------------------   NewType
'''
NewType
Sirve para crear un nuevo tipo... derivado de otro, conservando todos sus métodos
'''

class HotDog:
    # ... snip hot dog class implementation ...
    def dispense_to_customer_v1(hot_dog: HotDog):
        # note, this should only accept ready-to-serve hot dogs.
    '''¿Cómo hacemos para que sea sencillo que sólo entregue hotdogs preparados?
    Podríamos crear un nuevo tipo...'''

    # Ahora ya podemos hacer
    from typing import NewType
    ReadyToServeHotDog = NewType("ReadyToServeHotDog", HotDog)
    def dispense_to_customer_v2(hot_dog: ReadyToServeHotDog):
'''
O sea, para crear un nuevo tipo, simplemente hay que decirle un tipo existente
desde el que queremos crear el nuevo
El nuevo tipo tendrá todos los mismos campos y métodos que el tipo del que se derivó
Lo bueno, es que, en este caso, aunque un ReadyToServeHotDog sigue siendo un hotdog,
lo contrario no es cierto... o sea, no podremos utilziar hotdogs si la función espera
encontrar un ReadyToServeHotDog
'''
'''
Otra aplicación...
Separating a str from a SanitizedString, to catch bugs like SQL injection vulnerabilities.
By making SanitizedString a NewType, I made sure that only properly sanitized strings were
operated upon, eliminating the chance of SQL injection.
O sea, hacemos una función que ejecuta sql pero que el argumento que acepte sea
un nuevo tipo, sanitizedstring, .... así, si lo llamamos con una string cualquiera
que no esté revisada previamente, nos avisará (adevertencia solo, claro) del error
'''

# -----------------  A l i a s e s
'''
Sirven para resumir... no crear nada nuevo (a diferencia de NewType), son sólo una abreviatura
'''
# For example:
from typing import Union
IdOrName = Union[str, int]
ApuntesContables = Union[dict[int, User], list[dict[str, User]]]

# --------------  F i n a l    T y p e s
'''Final Types
Lo usamos para indicar que la variable no puede indicar otro valor
'''
VENDOR_NAME: Final = "Viafore's Auto-Dog"
VENDOR_NAME += 'lasdjf'
'Cuando ejecutamos mypy nos avisa,, también el entorno IDE, claro'

# ---------------------------
'''
Anotación de colecciones
podemos anotar colecciones de formas similares a esta...
'''
var: dict[str, int]  #si queremos usar un dict cuyas claves sean str y values sean int
var: list[str]  # lista donde los ítmes son string
var: set(Myclass)  # conjunto cuyos elementos con del tipo Myclass o lo que queramos

# ----  T y p e D i c t
'''
TypedDict viene muy bien cuando queremos anotar datos, pero son heterogéneos
(tb para lo mismo, y quizás mejor, utilizar dataclasses)
'''
from typing import TypedDict, Dict
class Range(TypedDict):
    min: float
    max: float

class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float
    otro_val: dict[str, int]

class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation

# --------------------- G e n e r i c s
'''
GENERICS!!!!
A generic type indicates that you don’t care what type you are using. However, it helps
restrict users from mixing types where inappropriate
'''
'''
Ejemplo: si tenemos una función que retorna una lista, pero en orden inverso....
y puede actuar en cualquier tipo de lista de entrada....
'''
def reverse(coll: list) -> list:
    return coll[::-1]
'''
Para anotarla, indicando que las listas de entrada y salida deben usar el mismo tipo para los ítmes como 
 lo hacemos, si se puede aplicar en cualquier tipo de ítem...???
 Usanndo generics...mismo tipo, sin especificar...
'''
from typing import TypeVar
T = TypeVar('T')  # Hacemos que T sea un nuevo tipo de datos genérico, sin especificar...
def reverse(coll: list[T]) -> list[T]:
# Hemos anotado que los ítems de la lista de entrada y los de salida deben ser del mismo tipo
    return coll[::-1]
'''
Podemos usar nuestras clases con genéricos, así nos ahorramos escribir código muchas veces
Para ello, nuestra clase debe heredar Generics[var_gen_1, var_gen_2, etc] para que pueda
conocer el tipo de los argumentos a usar, etc...
'''
'''
Ejemplo, queremos hacer un stack con listas
el stack vale para cualquier tipo de ítem, lógicamente
pero, por ejemplo, el pop nos debe dar el mismo de tipo de ítem tb
y el push debe usar el mismo tipo de ítem!!!
Lo hacemos fácil con un genérico
'''
from typing import TypeVar, Generic, List
T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    def __repr__(self) -> str:
        return repr(self._container)

# Otro ejemplo, aquí como usaremos dos tipos genéricos
# la clas debe derivar de Genercis[gener_1, gener_2]
from collections import defaultdict
from typing import Generic, TypeVar
Node = TypeVar("Node")  # variable genérica 1
Edge = TypeVar("Edge")  # variable genérica 2
# directed graph
class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node, list[Edge]] = defaultdict(list)
    def add_relation(self,node: Node, to: Edge):
        self.edges[node].append(to)
    def get_relations(self, node: Node) -> list[Edge]:
        return self.edges[node]

# Otro uso para generics
'''While generics are often used for collections, you can technically use them for any type.
For example, suppose you want to simplify your API error handling. You’ve already forced
your code to return a Union of the response type and an error type like so:

def get_nutrition_info(recipe: str) -> Union[NutritionInfo, APIError]:
# ...
def get_ingredients(recipe: str) -> Union[list[Ingredient], APIError]:
#...
def get_restaurants_serving(recipe: str) -> Union[list[Restaurant], APIError]:
# ...

But this is unneccessarily duplicated code. You have to specify a Union[X, APIError] each time,
where only X changes. What if you wanted to change the error response class, or force users
to handle different types of errors separately? Generics can help with deduplicating these types:
T = TypeVar("T")
APIResponse = Union[T, APIError]
def get_nutrition_info(recipe: str) -> APIResponse[NutritionInfo]:
# ...
def get_ingredients(recipe: str) -> APIResponse[list[Ingredient]]:
#...
def get_restaurants_serving(recipe: str) -> APIResponse[list[Restaurant]]:
# ...
Now you have a single place to control all of your API error handling. If you were to
change it, you can rely on your typechecker to catch all the places needing changes.
'''

'''
Modifying Existing Types
Cuidado, si queremos modificar algunos tipos builtin, como dict, para por ejemplo
cambiar el método __get__item, igual todo no sale como hemos planeado, pq están optimizaod
con código inline, y esto hace que igual nuestra implementación no se ejecute
Por ello, si queremos modificar algún tipo existente, es mejor que lo hagamos


Si es un objeto tipo dicccionario: pues utilizar collections.UserDict
Si es un objeto tipo lista, pues override los métodos que nos hagan falta de collections.UserList
Si es un objeto string, pues override collections.UserString
Pero, y si es un diccioanrio??? no existe, de momento, collections.UserSet
Pero podemos modificarlos desde las ABC....
'''
# Modificando un set desde las ABC ABSTRACT BASE CLASSES...
'''
Para implementar un comportamiento personalizado de un set, podemos heredar el set de abc
deberemos implementar __contains__, __iter__, __len__
'''
# En este ejemplo queremos implementar un conjunto que funcione con los elementos
# que tiene, pero que en las operaciones (pertenencia, etc) contemple tb alias
# de los elementos....
import collections.abc

class AliasedIngredients(collections.abc.Set):
    def __init__(self, ingredients: set[str]):
        self.ingredients = ingredients
    def __contains__(self, value: str):
        return value in self.ingredients or any(alias in self.ingredients
                                            for alias in get_aliases(value))
    def __iter__(self):
        return iter(self.ingredients)
    def __len__(self):
        return len(self.ingredients)
