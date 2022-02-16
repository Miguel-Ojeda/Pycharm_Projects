"""
Implement a MyRange class that returns an iterator that works the same as range, at least in for loops.

(Modern range objects have a host of other capabilities, such as being subscriptable. Don’t worry about that.)

The class, like range, should take one, two, or three integer arguments.
"""


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.bottom = 0
            self.top = first
            self.step = step

        else:
            self.bottom = first
            self.top = second
            self.step = step

        self._index = self.bottom


    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self.top:
            value = self._index
            self._index += self.step
            return value
        else:
            raise StopIteration


class MyRange_2:
    # Versión Reuven es más sencilla, elimina cosas innecesarias
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.current = 0
            self.top = first

        else:
            self.current = first
            self.top = second

        self.step = step



    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.top:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration


for i in MyRange_2(2, 10, 3):
    print(i)
