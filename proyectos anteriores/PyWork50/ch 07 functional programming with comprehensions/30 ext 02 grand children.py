"""
Define a dict that represents the children and grandchildren in a family.
(See figure 7.1 for a graphic representation.)

Each key will be a child’s name, and each value will be a list of strings representing their children
(i.e., the family’s grandchildren). En esta estructura, no aparecen los abuelos, que serían el origen..

Thus the dict {'A':['B', 'C', 'D'], 'E':['F', 'G']} means that A and E are siblings;
A’s children are B, C, and D; and E’s children are F and G.
Use a list comprehension to create a list of the grandchildren’s names.

O sea, con el diccionario anterior se crearía la lista ['B', 'C', 'D', 'F', 'G']
Observar que parece sencillo, simplemente crear una lista con todos los ítemes de los valúes
"""
import pprint


def get_grand_children(family):
    return [nieto
            for hijo in family
            for nieto in family[hijo]
            ]

def get_grand_children_v2(family):
    """Aunque mi vesión funciona, conceptualmente es más sencillo la versiónd de Reuven
    simplemente utilizar los valores, que representan los nietos!!
    Y ya está, nos olvidamos totalmente de los hijos y ya está!!!"""
    return [nieto
            for nietos in family.values()
            for nieto in nietos
            ]


familia = {'A':['B', 'C', 'D'], 'E':['F', 'G']}

resultado = get_grand_children(familia)
pprint.pprint(resultado)

resultado_2 = get_grand_children_v2(familia)
pprint.pprint(resultado_2)
