TASA = {'Chico': 0.50, 'Groucho': 0.70, 'Harpo': 0.50, 'Zeppo': 0.40}


def calculate_tax_v0(price, province, hour):
    precio_final = price * (1 + TASA[province] * hour / 24)
    return precio_final


# CUidado, si nos pasa una hora mal, se obtiene un resultado raro, pero no tendría sentido!!
# por ejemplo, si ponemos hora 27 serviría....
# En los módulos es importante llevar el control de errores... así que...


class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


def calculate_tax_v1(price, province, hour):
    if hour < 0:
        raise HourTooLowError(f'Hour of {hour} is < 0')
    elif hour >= 24:
        raise HourTooHighError(f'Hour of {hour} is >= 24')

    precio_final = price * (1 + TASA[province] * hour / 24)
    return precio_final


'''Hacer esta modificación tan sencilla nos asegura que la gente use bien nuestro módulo!!!
Si no, si pusiera una hora incorrecta nadie le advertiría del error, tendría un precio final
incorrecto pero nadie se daría cuenta.
No es necesario hacer esto para verificar que la provincia existe, pq si se equivoca
ya el programa provocará automáticamente una excepción'''
