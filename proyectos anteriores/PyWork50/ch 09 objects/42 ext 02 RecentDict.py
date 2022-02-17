"""The RecentDict class works just like a dict, except that it contains a
userdefined number of key-value pairs, which are determined when the instance is
created.

In a RecentDict(5), only the five most recent key-value pairs are kept;
if there are more than five pairs, then the oldest key is removed, along with its
value.

Note: your implementation could take into account the fact that modern
dicts store their key-value pairs in chronological order"""

class RecentDict(dict):
    def __init__(self, max_entries, **kwargs):
        self.max_entries = max_entries
        super().__init__(self, **kwargs)

    def __setitem__(self, key, value):
        if len(self) == self.max_entries:
            iterador = iter(self)
            first_key = next(iterador)
            del self[first_key]

        dict.__setitem__(self, key, value)

    # Reuven utiliza el método pop de los diccionarios...
    # el método pop elimina del diccioanario la entrada con la key indicada
    # Es más natural... no tengo que crear primero un objeto iterador si tan sólo
    # me interesa eliminar el objeto con la primera clave....!!
    def __setitem__Reuven(self, key, value):
        if len(self) == self.max_entries:
            self.pop(list(self.keys())[0])
            # También serviría --> del self[list(self.keys())[0]]
        dict.__setitem__(self, key, value)


dct = RecentDict(5, hola='23', adios='24', juan=25, eustaquio=48)
dct['genaro'] = 23
dct['heriberto'] = 49
dct['carla'] = 53


for key, items in dct.items():
    print(key, items)
