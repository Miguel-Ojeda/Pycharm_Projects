"""
In this exercise, I want you to define a class attribute that will function like a constant,
ensuring that we don’t need to hardcode any values in our class.

What’s the task here? Well, you might have noticed a flaw in our Bowl class, one
that children undoubtedly love and their parents undoubtedly hate: you can put as
many Scoop objects in a bowl as you like.

Let’s make the children sad, and their parents happy, by capping the number of
scoops in a bowl at three. That is, you can add as many scoops in each call to
Bowl.add_scoops as you want, and you can call that method as many times as you
want—but only the first three scoops will actually be added.

Any additional scoops will be ignored.
"""

# Partimos de la clase Bowl que ya teníamos en 39 composition...

from e38_scoop_class import Scoop

class Bowl:
    MAX_SCOOP = 3

    def __init__(self):
        self.list_scoops = []

    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.list_scoops) < Bowl.MAX_SCOOP:
                self.list_scoops.append(scoop)
            # O al revés, si es == len pues ya está lleno, hacer break...

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
