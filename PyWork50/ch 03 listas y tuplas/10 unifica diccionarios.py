# Write a function that takes a list of dicts and returns a single dict that combines
# all of the keys and values. If a key appears in more than one argument, the
# value should be a list containing all of the values from the arguments.

def unifica_diccionarios(*diccionarios: dict):
    union_dict = {}
    for diccionario in diccionarios:
        for key, value in diccionario.items():
            if key in union_dict.keys():  # si ya tenemos la clave...
                try:
                    union_dict[key].append(value)
                except AttributeError:
                    # SI estamos aquí es que no teníamos una lista!!
                    union_dict[key] = [union_dict[key], value]
            else:
                union_dict[key] = value
    return union_dict

dic_1 = {'nombre': ['Luis', 'Miguel'], 'apellidos': 'Pérez'}
dic_2 = {'profesión': 'doctor', 'equipo': 'Madrid', 'nombre': 'José'}
dic = unifica_diccionarios(dic_1, dic_2)
print(dic)