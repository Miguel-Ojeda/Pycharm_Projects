"""
Bags. A bag is a collection where removing items is not supported—its purpose is to
provide clients with the ability to collect items and then to iterate through the collected
items (the client can also test if a bag is empty and find its number of items).
The order of iteration is unspecified and should be immaterial to the client.
With our Bag API, a client can add items to a bag and process them
all with a foreach statement whenever needed.
Such a client could use a stack or a queue, but one way to emphasize that the order in
which items are processed is immaterial is to use a Bag.
"""

class Bag:

    def __init(self):
        pass

    @property
    def is_empty(self):
        pass

    @property
    def size(self):
        pass

    def add(self):
        pass

    def itera(self):
        ...


