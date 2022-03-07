"""
Find a solution to the missionaries-and-cannibals problem for a different number of starting
missionaries and cannibals. Hint: you may need to add overrides
of the __eq__() and __hash__() methods to MCState.
"""

'''Ya está hecho... lo hice tanto en:
03 misioneros y caníbales: aquí utilicé dataclasses y no tuve ningún problema ni hace nada especial

Cuando fui a hacerlo de nuevo, en 03 misioneros y caníbales v2, simplemente para simplificar
lo hice como clases, y me di cuenta de que no servía!! (excepto el dfs)

Parece que para comprobar si algo está en un conjunto se necesita primero un hash
(que sea constante si el contenido es constante, para saber donde buscar) y luego una igualdad
también basada en contenidos... con los dataclasses Python sabe hacer esto automáticamente
si le digo que es de tipo frozen....
Pero para clases tuve que hacerlo yo...
Ver el código en 03 misioneros y caníbales v2

En sets lo primero que se hace es saber donde buscarlos, para ello utiliza el hash..ç
pero si no definimos hash... Python lo hace por defecto, basado en TODO EL OBJETO, no solo en sus datos
y por ello, a veces piensa que el objeto no está en el set, pq el lugar asociado al hash que ha calculado
está vacío, pero sí que esta´....
Además, después cuando sabe donde buscar, basado en el hash, hay que saber comparar... de nuevo basado en el 
contenido del objeto....
'''
