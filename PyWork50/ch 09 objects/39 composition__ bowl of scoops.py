"""
In this exercise, we’re going to see a small-scale version of COMPOSITION.

In the previous exercise, we created a Scoop class that represents one scoop of ice cream.

If we’re really going to model the real world, though, we should have another object into
which we can put the scoops. I thus want you to create a Bowl class, representing a
bowl into which we can put our ice cream (figure 9.7); for example
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)
The result of running print(b) should be to display the three ice cream flavors in our
bowl (figure 9.8). Note that it should be possible to add any number of scoops to the
bowl using Bowl.add_scoops.
"""

from  e38_scoop_class import Scoop

class Bowl:
    def __init__(self):
        self.list_scoops = []

    def add_scoops(self, *scoops):
        # for scoop in scoops:
        #     self.list_scoops.append(scoop)

        # Otra opción podría ser...
        self.list_scoops.extend(scoops)

    def __repr__(self):
        # También se podría poner esto en __str__ realmente
        # Revuen opta por ponerlo en __repr__ pq así mata dos pájaros de un tiro...
        return '\n'.join(scoop.flavor
                         for scoop in self.list_scoops)


if __name__ == '__main__':
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    print(b)
