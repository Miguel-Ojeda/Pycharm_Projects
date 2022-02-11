"""
Use a nested list comprehension to transform a list of dicts into a list of two element (name-value) tuples,
each of which represents one of the name-value pairs in one of the dicts.
If more than one dict has the same name-value pair, then the tuple should appear twice
"""
import pprint

list_dic = [dict(name='Carlos', edad=43, profesion='informático'),
            dict(name='Ana', edad=39, profesion='riesgos laborales'),
            dict(name='Aray', edad=2, profesion='estudiante', comida='churros'),
            dict(pais='España', ciudad='Las Palmas', deporte='motociclismo'),
            dict(color='naranja', codigo={1: 'ABC', 2: 'BCD', 3: 'DCA'}, cantidad=100, moneda='euro')]


def list_dic_to_tuples(list_dict):
    return [(name, value)
            for diccionario in list_dict
            for name, value in diccionario.items()]


# Después de ver Reuven veo que se puede hacer mejor!!!
# Puedo utilizar directamente la tuple que devuelve .items()
def list_dic_to_tuples_v2(list_dict):
    return [tupla
            for diccionario in list_dict
            for tupla in diccionario.items()]


resultado = list_dic_to_tuples_v2(list_dic)
pprint.pprint(resultado)

