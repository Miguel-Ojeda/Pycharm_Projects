"""The FlatList class inherits from list and overrides the append method.
If append is passed an iterable, then it should add each element of the iterable separately.
This means that fl.append([10, 20, 30]) would not add the list
[10, 20, 30] to fl, but would rather add the individual integers 10, 20, and 30.
"""
'''list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
'''


class FlatList(list):
    def append(self, elemento):
        try:
            for item in elemento:
                list.append(self, item)
        except:
            list.append(self, elemento)



mi_fl = FlatList()
mi_fl.append(12)
mi_fl.append(13)
mi_fl.append([1,2, 5, 4])
print(mi_fl)