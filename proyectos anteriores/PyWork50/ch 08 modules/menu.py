"""
Ejercicio 37
La función menú toma un número indeterminado de keyword arguments
Los values representan las funciones que se pueden ejecutar
Se le pregunta al usuario la opción que quiere ejecutar
y luego se ejecuta la función asociada a la key que eleigió
"""


def menu(**funciones_a_elegir):
    while True:
        print('Qué función desea ejecutar?')
        for key in funciones_a_elegir:
            print(key, end='\t')
        opcion = input('\nElija su opción: ')
        if opcion not in funciones_a_elegir:
            print('Esta opción no es válida')
            continue
        print(f'Ejecutando función {opcion} ...')
        return funciones_a_elegir[opcion]()


# Después de ver la solución de Reuven, similar pero algo más elegante
# De 11 líneas pasamos a 7, y es incluso más claro (lo mío es más confuso)
def menu_v2(**funciones_a_elegir):
    while True:
        option_string = ' / '.join(funciones_a_elegir)   # es lo mismo que poner funciones_a_elegir.keys()
        opcion = input(f'Elija una opción ( {option_string} ): ')
        if opcion in funciones_a_elegir:
            return funciones_a_elegir[opcion]()

        print('Esta opción no es válida')



def generador_funciones(cadena):
    # creamos clousures para hacer todo_ rápido
    def fun():
        return cadena

    return fun


if __name__ == '__main__':
    f_hola = generador_funciones('Hola como estás')
    f_adios = generador_funciones('Adiós, nos vemos pronto')
    f_estudiar = generador_funciones('Estoy estudiando el nuevo capítulo')
    f_jugar = generador_funciones('Estoy jugando al fútbol')
    f_correr = generador_funciones('Salgo a correr')

    # print(f_hola())
    # print(f_adios())
    # print(f_estudiar())
    # print(f_jugar())
    # print(f_correr())
    resultado = menu_v2(hola=f_hola, adios=f_adios, estudiar=f_estudiar, jugar=f_jugar, correr=f_correr)
    print(f'Resultado --> "{resultado}"')
