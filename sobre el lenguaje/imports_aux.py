class Test_2:
    def __init__(self):
        self.x = 14
        self.y = 24
        self._z = 25

    def externo(self):
        print('Externo')
        print(self.x, self.y, self._z)

    def _interno(self):
        print('Interno')
        print(self.x, self.y, self._z)

