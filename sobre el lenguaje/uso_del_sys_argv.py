# sys.argv se utilzia para saber los parámetros que pasamos a un programa
# es una variable del sistema cuyo contenido es una lista:
# primer ítem... el nombre del script invocado
# el segundo item... el primer argumento que pasamos el programa
# el tercer ítem.. el segundo argumento que pasamos al programa...

# Veamos como usarlo... (habrá que ejecutar este programa
# desde la línea de comandos y darle varios argumentos adicionales
import sys

# Cogemos el elemento 0, que va a ser el path completo al script invocado desde línea de comandos...
full_path = sys.argv[0]
# Lo partimos en cachitos pq nos interesa realmente el final....
elementos_path = full_path.split('/')
# print(elementos_path)
# Imprimimos simplemente el último elemento, con el nombre del script...
print(f'Este script se llama: {elementos_path[-1]}')
# Ahora, vamos a ver todos los argumentos utilizados (están a partir del índice 1...
for index, argumento in enumerate(sys.argv[1:]):
    print(f'El argumento {index} es: {argumento}')

# Cuando ejecutamos:
# $ py uso_del_sys_argv.py argumento1 argumento2 argumento3
# La salida es la siguiente:
# >>> Este script se llama: uso_del_sys_argv.py
# >>> El argumento 0 es: argumento1
# >>> El argumento 1 es: argumento2
# >>> El argumento 2 es: argumento3

