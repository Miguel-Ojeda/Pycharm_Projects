def yell(text):
    return text.upper() + '!!!!!!!!!'

print(yell('hello'))


bark = yell  # podemos asignar una función a una variable, ya que una función es, simplemente, un objeto más...

# ahora, tanto yell como bark apuntan a lo mismo, al objeto que define la función
print(yell)
print(bark)
print(type(yell))
print(type(bark))
print(bark('hola'))

# podemos borrar la variable original, yell y todavía seguir utilizando bark pq el objeto función sigue en memoria
del yell
print(bark('hola'))


def puntear(text=''):
    return '............' + text + '...........'


# podemos recuperar el identificador inicial de la función, utilizando el atributo __name__
# también, como es un objeto de tipo clase function... podemos referenciar otros de sus atributos...
print(bark.__name__)
print(bark.__annotations__)
print(bark.__doc__)
print(bark.__class__)
print(bark.__code__)
print(puntear())


def whisper(text):
    return text.lower() + '...'


# Almacenando objetos función en una lista...
lista_funciones = [bark, str.lower, str.upper, str.capitalize, whisper, puntear]
print(lista_funciones[0]('juanito'))
for funcion in lista_funciones:
    print(funcion, funcion('hello'))


def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


for funcion in lista_funciones:
    greet(funcion)

# ya hemos visto que una función puede ser el argumento de otra
# estas funciones se llaman funciones de alto orden, y su comportamiento se ve afectado por la función argumento...

# ejemplo clásico de función higher-order function: la función map
# Tiene dos argumentos: una función a aplicar, y una lista de elementos a los que se aplicará la función...
# el resultado es un objeto tipo map... Si queremos imprimirlo, antes conviene convertirlo en una lista...
mapa = map(puntear, ['uno', 'dos', 'tres'])
# imprimimos el tipo de objeto... ambas formas es lo mismo...
print(mapa.__class__)
print(type(mapa))
# creamos una lista...
map_list = list(mapa)
print(map_list)
for elemento in map_list:
    print(elemento)

print(puntear())
print(puntear())
print(puntear())
print(puntear())

for funcion in lista_funciones:
    lista = list(map(funcion, ['uno', 'dos', 'tres']))
    print(lista)


# funciones definidas dentro de funcioens!!!!
def speak(text, bool=True):
    def whisper(t):
        return t.lower() + '...interno...'

    def yell(t):
        return t.upper() + '!!!!! interno !!!!!'

    if bool:
        return whisper(text)
    else:
        return yell(text)


print(speak('hola'))
print(speak('hola', False))

# cómo acceder a una función definida dentro, desde fuera??? son objetos interiores, locales, escondidos...
# podemos devolver la referencia a una función definida interiormente....!!!!
def get_speak_func(volume=0):
    def whisper(text):
        return text.lower() + '......interior......'

    def yell(text):
        return text.upper() + '!!!!!! interior !!!!!'

    if volume > 0.5:
        return yell
    else:
        return whisper

funcion_interior = get_speak_func()
funcion_interior_2 = get_speak_func(1)
print(funcion_interior('como estás'))
print(funcion_interior_2('como estás'))


# imagino que esto es posible porque los objetos función, aunque estén definidos dentro,
# siguen existiendo pq hay variables que apuntan a ellas... su ref counter no es 0!!!
# o sea; podemos pasarle comportamientos a las funciones (higher-order functions)
# y también podemos retornar comporamientos... desde las funciones...
# veamos una función similar, mejorada, que no sólo devuleve la función, sino que las
# funciones interiores devueltas son directamente llamadas capturando el argumento de la función padre...
def get_speak_func_2(text, volume=0):
    # las funciones internas recuerdan el argumento 'text' de la función padre...
    # por tanto, pueden operar, sin pasarle ningún argumento, utilizando los del padre!!!!
    # a las funciones que recuerdan el contexto, incluso cuando el flujo del programa ya no está
    # en ese contexto se llaman clousures (lexical clousures): tienen memoria....  y podemos aprovecharla!!!
    def whisper():
        return text.lower() + '................'
    def yell():
        return text.upper() + '!!!!!!!!!!!!!!!!!!!!!!'
    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func_2('texto a utilizar'))
print(get_speak_func_2('texto a utilizar')())
print(get_speak_func_2('texto a utilizar', 1))
print(get_speak_func_2('texto a utilizar', 1)())

# otro ejemplo de clousures..
def make_adder(n):
    def add(x):
        return x + n  # recuerda el parámetro pasado a la función padre!! es una clousure!!!
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)

print(plus_3(19))
print(plus_5(10))
print(puntear())
print(puntear())
print(puntear())
print(puntear())

lista_funciones = [make_adder(i) for i in range(1, 11)]
for funcion in lista_funciones:
    print(funcion(10))


# haciendo que objetos se comporten como funciones... magic method __call__
class Adder:
    def __init__(self, n):
        self.n = n

    # con esto hacemos que el objeto se comporta, aparentemente,
    # como una función a la que podemos pasar argumentos
    def __call__(self, x):
        return self.n + x


print(puntear())
print(puntear())
adder_3 = Adder(3)
adder_5 = Adder(5)

print(adder_3(9))
print(adder_5(9))



