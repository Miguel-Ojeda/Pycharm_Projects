from balloon import *
import random
import balloon_manager


class Prueba:
    def __init__(self):
        self.hola = 5
        self.mensaje = "Hola"
        # self.lista = [i for i in range(1, 10)]
        self.dict = {'uno': 1, 'dos': '222', self.mensaje: 'otro mensaje'}

    def __del__(self):
        print('borrando el objeto')



objeto = Prueba()
print(objeto.__dict__)

