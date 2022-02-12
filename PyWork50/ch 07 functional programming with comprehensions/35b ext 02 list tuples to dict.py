"""Create a list of tuples in which each tuple contains three elements:
(1) the author’s first and last names,
(2) the book’s title, and
(3) the book’s price in U.S. dollars.

Use a dict comprehension to turn this into a dict whose keys are the book’s titles,
with the values being another (sub-) dict, with keys for
(a) the author’s first name,
(b) the author’s last name, and
(c) the book’s price in U.S. dollars.
"""
# Supondremos que el autor se guarda con dos palabras... Nombre Apellido  (ej Juan Ramírez)
import pprint

libros = [('Santiago Posteguillo', 'Africanus', 22),
          ('JK Rowling', 'El prisionero de Azkabán', 14),
          ('George Orwell', '1984', 9),
          ('Miguel de_Cervantes', 'El Quijote', 27),
          ('Ken Follett', 'Los Pilares de la Tierra', 17),
          ('Isaac Asimov', 'La fundación', 32),
          ]

def lista_to_dict(libros):
    return {item[1]: {'Autor (nombre)': item[0].split()[0],
                      'Autor (apellido)': item[0].split()[1],
                      'Precio': f'{item[2]} €'}
            for item in libros}


def lista_to_dict_v2(libros):
    """Después de ver la solución de Reuven.... desempaqueta la tupla!!!!"""
    return {titulo: {'Autor (nombre)': nombre.split()[0],
                      'Autor (apellido)': nombre.split()[1],
                      'Precio': f'{precio} €'}
            for nombre, titulo, precio in libros}

resultado = lista_to_dict_v2(libros)
pprint.pprint(resultado)