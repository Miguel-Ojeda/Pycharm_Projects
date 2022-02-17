"""
Write a Beverage class whose instances will represent beverages.

Each beverage should have two attributes:  a name (describing the beverage) and a temperature.

Create several beverages and check that their names and temperatures are all handled correctly.
"""

class Beverage:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def display_info(self):
        print(f'El {self.name} se toma a {self.temperature}º C')

martini = Beverage('martini', 10)
tinto = Beverage('vino tinto', 14)
blanco = Beverage('vino blanco', 8)

for bebida in [martini, tinto, blanco]:
    bebida.display_info()


