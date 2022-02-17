"""Income tax in many countries is not a flat percentage,
but rather the combination of different tramos...
So a country might not tax you on your first $1,000 of income,
and then 10% on the next $10,000, and then 20% on the next $10,000,
and then 50% on anything above that.

Write a function that takes someone’s income and returns the amount
of tax they will have to pay, totaling the percentages from various brackets.
"""

from collections import namedtuple

Tramo = namedtuple('Tramo', 'base tope tasa')



# Lo voy a hacer no como módulo, sino aquí mismo...
TASAS = [Tramo(0, 10_000, 0),  # Hasta 10_000 euros no se paga nada
         Tramo(10_000, 25_000, 0.10),  # De los 10_000 hasta 20_000 se paga el 10 %
         Tramo(25_000, 60_000, 0.18),
         Tramo(60_000, 100_000, 0.27),
         Tramo(100_000, 200_000, 0.40),
         Tramo(200_000, 500_000, 0.50),
         Tramo(500_000, None, 0.55)]

       # Ahora debo realizar una función que me desglose, para un dinero dado,
# qué cantidad tengo en cada uno de los tramos anteriores

def calculate_tax(income):
    desglose_income_por_tramos = []
    desglose_tasa_por_tramos = []
    for tramo in TASAS:

        if tramo.tope is None or income <= tramo.tope:
            # Estamos en el último tramo aplicable...
            desglose_income_por_tramos.append(income - tramo.base)
            desglose_tasa_por_tramos.append((income - tramo.base) * tramo.tasa)
            break
        else:  # income > tramo.tope:
            desglose_income_por_tramos.append(tramo.tope - tramo.base)
            desglose_tasa_por_tramos.append((tramo.tope - tramo.base) * tramo.tasa)

    print(desglose_income_por_tramos)
    print(desglose_tasa_por_tramos)


def calculate_tax_v2(income):
    """Simplificaremos todo_ sólo calculando la tasa.... sin desglose..."""
    tasa = 0
    for tramo in TASAS:

        if tramo.tope is None or income <= tramo.tope:
            tasa += (income - tramo.base) * tramo.tasa

        else:  # income > tramo.tope:
            tasa += (tramo.tope - tramo.base) * tramo.tasa

    return tasa






calculate_tax(600_000)
tasa = calculate_tax_v2(600_000)
print(f'La tasa por 600_000 euros es {tasa:_}')