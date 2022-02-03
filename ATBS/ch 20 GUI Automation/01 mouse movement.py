import pyautogui
import time

window_size = pyautogui.size()
print(window_size)

# o simplemente
width, height = pyautogui.size()

# realmente no es necesario, porque size() nos devuelve una named-tuple
print(f'El ancho de la pantalla es {window_size.width} y el alto {window_size.height}')
# --> El ancho de la pantalla es 1920 y el alto 1080

# las coordenadas son (0, 0) para let, top y abajo del todo_ según la resolución ... en este caso (1919, 1079)

'''
# Para mover el ratón podemos usar métodos moveTo(x, y, duration=??)
# Nos mueve el ratón a esas coordenadas, tardando en el movimiento el tiempo especificado
# por defecto el tiempo es 0, instantáneo...
La función move es similar, pero el movimiento es relativo a la posición actual del cursor
'''

# time.sleep(5)
for i in range(6):    # describamos un cuadrado con el ratón... 6 veces...
    pyautogui.moveTo(500, 500, duration=0.25)
    pyautogui.moveTo(800, 500, duration=0.25)
    pyautogui.moveTo(800, 800, duration=0.25)
    pyautogui.moveTo(500, 800, duration=0.25)

# Lo mismo, pero relativo a la posición inicial del cursor...
time.sleep(3)  # dormirmos un poco el programa para colocar el ratón en otro sitio...
for i in range(6):    # describamos un cuadrado con el ratón... 10 veces...
    pyautogui.move(200, 0, duration=0.25)  # 200 a la derecha
    pyautogui.move(0, 200, duration=0.25)   # 200 abajo
    pyautogui.move(-200, 0, duration=0.25)  # 200 a la iz
    pyautogui.move(0, -200, duration=0.25)  # 200 arriba

# Si queremos obtener la posición del ratón
posicion = pyautogui.position()
# Retorna una named-tupla, podemos acceder por [] o con .x .y

'''
Haciendo click --> .click()... por defecto hace click izquierdo en la posición actual
pero podemos tb. especificar posición, y decir que sea otro botón
Por ejemplo  --> pyautogui.click(200, 250, button='right')
Otras opciones...
pyautogui.doubleClick(), pyautogui.rightClick(), pyautogui.middleClick()
'''

# Arrastre del ratón.... dragging
'''
pyautogui.dragTo(x, y) and pyautogui.drag(): son iguales, pero la segunda la posición es relativa a la actual
'''

'''
Ejemplo, abrir el mspaint
Dibujemos automáticamente una espiral... para ello simplemetne elegir un pincel en
MSPAINT y luego este código hará todo
'''
time.sleep(5)  # Para que nos dé tiempo de ir a la app del mspaint
pyautogui.click()   # para convertirla en activa... (tb. podríamos hacer clic nosotros, claro)
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)  # Move right.
    distance -= change
    pyautogui.drag(0, distance, duration=0.2)  # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance -= change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.


# Scrolling the Mouse --> pyautogui.scroll(200)

# Planning Your Mouse Movements  --> pyautogui.mouseInfo()
'''Podemos automatizar el movimiento del ratón, pero cómo saber a dónde tenemos que ir...
Pues mouseInfo nos ayuda a conseguir la información necesaria...
nos ayuda a averiguar la posición x, y a la que tenemos que ir...
The pyautogui.mouseInfo() function is meant to be called from the interactive shell,
rather than as part of your program.
It launches a small application named MouseInfo that’s included with PyAutoGUI.
The window for the application looks like Figure 20-3
Básicamente es un app que nos ayuda a averiguar a obtener los datos del x, y apropiado
para luego poder meter esas posiciones en nuestros scripts '''


