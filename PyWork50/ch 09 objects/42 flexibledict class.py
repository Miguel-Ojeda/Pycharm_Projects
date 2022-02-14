"""In this exercise, we’ll also implement a subclass of dict, which I call FlexibleDict.
Dict keys are Python objects, and as such are identified with a type. So if you use key 1
(an integer) to store a value, then you can’t use key '1' (a string) to retrieve that
value. But FlexibleDict will allow for this. If it does not find the user’s key, it will try to
convert the key to both str and int before giving up; for example
fd = FlexibleDict()
fd['a'] = 100
print(fd['a'])
fd[5] = 500
print(fd[5])
fd[1] = 100
print(fd['1'])
fd['1'] = 100
print(fd[1])
"""

class FlexibleDict(dict):
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        elif type(key) == int:
            return self.get(str(key))
        elif type(key) == str and key.isdigit():
            return self.get(int(key))

# Versión de Reuven es mejor, pq no reporta None como la mía si no existe, sino que da error
class FlexibleDict_2(dict):
    def __getitem__(self, key):
        # El try realmente es por el error que puede dar en el último elif
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            # esta es la condición que puede dar un ValueError!!!
            # por eso la dejamos para el final!!!!
            # si la pusiéramos antes, dejaríamos de intentar otras cosas!!!
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self, key)


if __name__ == '__main__':
    d = FlexibleDict()
    d['a'] = 5
    print(d['a'])
    d[1] = 'abcd'
    print(d[1])
    print(d['1'])
    d['2'] = 'dfdf'
    print(d[2])
    print(d[3])
    # >>> me da None,

    d2 = FlexibleDict_2()
    d2['a'] = 5
    print(d2['a'])
    d2[1] = 'abcd'
    print(d2[1])
    print(d2['1'])
    d2['2'] = 'dfdf'
    print(d2[2])
    print(d2[3])
    # >>> KeyError: 3 que es lo correcto pq la clave falla!!