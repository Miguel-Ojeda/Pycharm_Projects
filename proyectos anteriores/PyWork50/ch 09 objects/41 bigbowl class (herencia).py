"""
Implement BigBowl for this exercise, such that the only difference between it and
the Bowl class we created earlier is that it can have five scoops, rather than three.

And yes, this means that you should use inheritance to achieve this goal.
You can modify Scoop and Bowl if you must, but such changes should be minimal
and justifiable.


IMPORTANTE!!!! para minimizar cambios, en la case Bowl,
modificamos el método add_scoops para no mirar el valor de Bowl.max_scoops
sino el valor de self.max_scoops... esto hace que primero se mire en el objeto
y (como no existe) luego en la clase del objeto!!!
Si utilizamos esto desde un bowl utilizará Bowl.max_scoops... pero si
lo utilizamos desde un BigBowl pues mirará BigBowl.max_scoops!!
Leer mejor la explicación del libro!! pg 180 y siguientes!!
"""


# Meto el código anterior aquí tb.....
# ___________________________________________________
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def create_scoops(flavor_1, flavor_2, flavor_3):
        return [Scoop(flavor) for flavor in (flavor_1, flavor_2, flavor_3)]


class Bowl:
    MAX_SCOOP = 3

    def __init__(self):
        self.list_scoops = []

    def add_scoops(self, *scoops):
        for scoop in scoops:
            # Como no existe el atributo MAX_SCOOP en self pues mirará para arriba
            # en su clase, o si no en la clase padre, etc
            # este cambio lo hacemos para no tener que definir un método distinto
            # en BigBowl para add_scoops...
            if len(self.list_scoops) < self.MAX_SCOOP:
                self.list_scoops.append(scoop)
            # O al revés, si es == len pues ya está lleno, hacer break...

    def __repr__(self):
        # También se podría poner esto en __str__ realmente
        # Revuen opta por ponerlo en __repr__ pq así mata dos pájaros de un tiro...
        return '\n'.join(scoop.flavor
                         for scoop in self.list_scoops) + '\n'


class BigBowl(Bowl):
    MAX_SCOOP = 5
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('Turrón')
    s5 = Scoop('Chocolate')
    s6 = Scoop('Naranja')
    s7 = Scoop('Yogur')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s4, s5, s6)

    bigb = BigBowl()
    bigb.add_scoops(s1, s2)
    bigb.add_scoops(s3)
    bigb.add_scoops(s4, s5, s6)
    print(b)
    print(bigb)