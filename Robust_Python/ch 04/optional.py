from typing import Optional
import random

'''Optional se usa cuando la función puede devolver, o no, algo
Lo bueno es que, en este caso, el entorno o mypy nos avisa de que a lo mejor
los métodos que queremos aplicar no son aplicables en el caso None
Con lo que hemos de revisar....'''


class Frank:
    def __init__(self, frankfurt: str):
        self.frankfurt = frankfurt


def dispense_frank_v0() -> Frank:
    ''' Esto está mal, me advierte tanto mypy como Pycharm....
    mypy me dice: Incompatible return value type(got"None", expected"Frank")'''
    if random.random() <= 0.8:
        return Frank('frankfourt')
    else:
        return None

def dispense_frank_v1() -> Frank | None:
    ''' Ahora ya está bien, pq le decimos que podemos devolver un objeto
    tipo Frank o None'''
    if random.random() <= 0.8:
        return Frank('frankfourt')
    else:
        return None

def dispense_frank_v2() -> Optional[Frank]:
    ''' Pero es mejor así (aunque realmente es lo mismo)'''
    if random.random() <= 0.8:
        return Frank('frankfourt')
    else:
        return None


class Bun:
    def __init__(self, cereal: str):
        self.cereal = cereal
        self.condiments = []

    def add_frank(self, frank: Frank) -> Optional:
        self.frank = frank
        if random.random() <= 0.8:
            return self
        else:
            return None


    def add_condiments(self, *condimentos):
        for condimento in condimentos:
            self.condiments.append(condimento)


def dispense_bun() -> Optional[Bun]:
    if random.random() <= 0.8:
        return Bun('trigo')
    else:
        return None

def dispense_ketchup() -> Optional[str]:
    if random.random() <= 0.8:
        return 'ketchup'
    else:
        return None

def dispense_mustard() -> Optional[str]:
    if random.random() <= 0.8:
        return 'mustard'
    else:
        return None


def create_hot_dog():
    bun = dispense_bun()
    frank = dispense_frank_v2()
    hot_dog = bun.add_frank(frank)
    ketchup = dispense_ketchup()
    mustard = dispense_mustard()
    '''
    me advierte pycharm ahora.... no encuentro referencia a add_condiments in None!!!
    '''
    hot_dog.add_condiments(ketchup, mustard)

     # dispense_hot_dog_to_customer(hot_dog)