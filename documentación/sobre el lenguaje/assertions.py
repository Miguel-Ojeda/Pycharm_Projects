# An assertion is a sanity check to make sure your code isn’t doing something
# obviously wrong.

# Sólo las utilizaremos en la fase de desarrollo... nos indican que ha surgido
# en el código una condición que debería ser imposible... pero no es por algo que
# el usuario haya hecho mal, en cuyo caso podríamos elevar una excepción con raise...
# sino por nuestro código es defectuoso!!
# Por tanto, cuando ya esté terminado, pues no tieen sentido, debería estar quitado...
# Sintaxis: assert <expresión a evaluar> [, expresión a mostrar si falla]
# Ejemplo: assert 10 > 15, 'Ha ocurrido un error'

# ejemplo:
def par(x):
    if x % 2 == 0:
        return True
    elif x % 2 == 1:
        return False
    else:
        assert False, ('This should never happen.... esta funcióhn sólo se aplica para números enteros!!')

print(par(8))
print(par(9))
# Aquí cantará error
# print(par(9.5))

# observar que los asserts pueden ser deshabilitados on la opción -O o con la opción -OO
# evidentemente, por esta causa nunca deberíamos usar asserts para validación de los datos requeridos a usuarios...
# además de que realmente los asserts son para fallos nuestros en el código...

# cuidado, observar que si aplicamos el assert a una tupla, sea lo que sea los elementos, siempre va a dar True
# Las tuplas siempre se evalúan en Python a True

# Esto nunca va a fallar!!!
# assert (1 ==2, 'La tupla siempre va a ser verdad')
# aquí sí!!!
# assert 1 == 2, 'ufff'


# Otro ejemplo con simulación de semáforos...
# suponemos los semáforos en las esquinas entre calles... por ejemplo, entre market y 2nd...
# cada cruce tiene dos luces... una en sentido vertical de circulación y otra en horizontal...
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

# Ahora definimos una función que estará mal...
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

# Hemos cometido un error de programación, porque por eemplo, si hacemos un switch veamos lo que pasa...
switchLights(market_2nd)
# Tenemos!! la luz norte sur en amarillo, y la este oeste en verde!!!
# Podría haber una colisión, ya que las dos direcciones podrían moverse!!
# Esto es incorrecto, hemos programado mal el semáforo...
print(market_2nd)

# Podríamos detectar que pasa algo raro en el semáforo si hubiéramos diseñado
# la función con asserts, para detectar que hemos programado mal algo...
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

# Ahora definimos una función que estará mal...
def switchLights_con_assert(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    # Si está bien diseñado el cambio de luces en el cruce, al menos uno de las direcciones debería estar en rojo...
    assert 'red' in stoplight.values(), 'Cuidado, ninguna dirección está en rojo!!' + str(stoplight)

switchLights_con_assert(market_2nd)

# gracias al assert hemos descubierto que hemos programado mal la función!!!
# es un mecanismo de seguridad que permite comprobar que el código es correcto
# cuando hemos terminado de corregir tod. pues deberíamos quitar los asserts....