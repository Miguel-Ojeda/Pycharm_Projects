"""
In this exercise, you’ll define a class, Scoop, that represents a single scoop of ice cream.
Each scoop should have a single attribute, flavor, a string that you can initialize
when you create the instance of Scoop.

Once your class is created, write a function (create_scoops) that creates three
instances of the Scoop class, each of which has a different flavor (figure 9.1).

Put these three instances into a list called scoops (figure 9.2). Finally, iterate over your
scoops list, printing the flavor of each scoop of ice cream you’ve created.
"""

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


def create_scoops(flavor_1, flavor_2, flavor_3):
    scoop_1 = Scoop(flavor_1)
    scoop_2 = Scoop(flavor_2)
    scoop_3 = Scoop(flavor_3)

    return [scoop_1, scoop_2, scoop_3]


def create_scoops_v2(flavor_1, flavor_2, flavor_3):
    return [Scoop(flavor) for flavor in (flavor_1, flavor_2, flavor_3)]


if __name__ == '__main__':
    scoop_list = create_scoops_v2('turrón', 'plátano', 'naranja')

    for scoop in scoop_list:
        print(scoop.flavor)