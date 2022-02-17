"""
Define a list of five dicts. Each dict will have two key-value pairs, name and age,
containing a person’s name and age (in years).

Use a list comprehension to produce a list of dicts in which each dict contains three key-value pairs:
* the original name, the original age,and a third age_in_months key, containing the person’s age in months.

However, the output should exclude any of the input dicts representing people over 20 years of age.
"""
import pprint


def generate_new_dicc(personas):
    return [{'name': persona['name'], 'age': persona['age'], 'months': persona['age'] * 12}
            for persona in personas
            if persona['age'] <= 20]



def generate_new_dicc_v2(personas):
    """
    Reuven usa el operador ** para crear más rápido el diccionario!!
    ¡Además, al utilizar dict ya las claves no van entre llaves y se utiliza el = como en los keyword arguments!!
    Mucho mejor que mi opción, más compacto y claro!!
    Es innecesario volver a especificar todo_ el dictionary si vamos a partir del existente!!
    """

    return [dict(**persona,  months=persona['age'] * 12)
            for persona in personas
            if persona['age'] <= 20]


name_age_people = [{'name': 'Juan', 'age': 10},
                   {'name': 'Ernesto', 'age': 22},
                   {'name': 'Pancracio', 'age': 13},
                   {'name': 'Bernadette', 'age': 23},
                   {'name': 'Lucía', 'age': 19},
                   ]

name_age_months_lt20 = generate_new_dicc(name_age_people)

pprint.pprint(name_age_months_lt20)