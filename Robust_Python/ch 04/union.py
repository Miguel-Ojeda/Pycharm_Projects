from typing import Union


# Error!!! el retorno debe ser int.... habrá que arreglarlo!!
def hora_es_v0(entero: int) -> int:
    if entero < 18:
        return entero
    else:
        return 'NOCHE'


def hora_es_v1(entero: int) -> int | str:
    if entero < 18:
        return entero
    else:
        return 'NOCHE'


def hora_es_v2(entero: int) -> Union[int, str]:
    if entero < 18:
        return entero
    else:
        return 'NOCHE'
