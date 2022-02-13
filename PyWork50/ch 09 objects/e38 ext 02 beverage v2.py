"""
Modify the Beverage class, such that you can create a new instance specifying the name, and not the temperature.

If you do this, then the temperature should have a default value of 75 degrees Celsius.
Create several beverages and double-check that the temperature has this default when not specified
"""

class Beverage:
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature

    def display_info(self):
        print(f'El {self.name} se toma a {self.temperature}º C')