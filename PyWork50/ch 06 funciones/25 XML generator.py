"""
Write a function, myxml, that allows you to create simple XML output.
The output from the function will always be a string.
The function can be invoked in a number of ways, as shown in table 6.3.

Call                                    Return Value
myxml('foo')                            <foo></foo>
myxml('foo', 'bar')                     <foo>bar</foo>
myxml('foo', 'bar', a=1, b=2, c=3)      <foo a="1" b="2" c="3">bar</foo>

* Notice that in all cases, the first argument is the name of the tag.
* In the latter two cases, the second argument is the content (text) placed between the opening and closing tags.
* And in the third case, the name-value pairs will be turned into attributes inside of the opening tag.
"""

def myxml(tag, content='', **attributes):
    output = f'<{tag}'
    # print(type(attributes), attributes)
    for key, value in attributes.items():
        output += f' {key}="{value}"'
    output += f'>{content}</{tag}>'
    return output


def myxml_2(tag, content='', **attributes):
    """¡La solución de Reuven es mucho más elegante
    Genera primero los atributos que vamos a poner...
    con un join en una lista con los pares...
    la lista se genera en un list comprehension!!
    Es lo mismo que hago yo en el for!! pero él lo hace automático!! en una sola línea!!
    Lo mío, en comparación, es supercutre!!!  :(
    """
    atributos = ''.join([f' {key}="{value}"' for key, value in attributes.items()])
    return f'<{tag}{atributos}>{content}</{tag}>'


resultado = myxml_2('foo')
print(resultado)

resultado = myxml_2('foo', 'bar')
print(resultado)

resultado = myxml_2('foo', 'bar', a=1, b=2, c=3)
print(resultado)
