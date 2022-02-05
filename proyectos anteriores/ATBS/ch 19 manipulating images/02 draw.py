from PIL import Image, ImageDraw


nueva_imagen = Image.new('RGBA', (200, 200), 'white')
# Obtenemos un ImageDraw Object, que nos va a permitir dibujar en la imagen asociada!!!
draw_object = ImageDraw.Draw(nueva_imagen)

'''
ALgunos métodos que podemos utilizar con este objeto ImageDraw....
Dibujo de puntos... point([lista de puntos], fill)
Lines  line(xy, fill, width)   xy es una lista de tuplas o de enteros...
Rectángulos ... rectangle(xy, fill, outline)
Ellipses ellipse(xy, fill, outline)
Polygons polygon(xy, fill, outline) 
'''


nueva_imagen = Image.new('RGBA', (200, 200), 'white')
draw_object = ImageDraw.Draw(nueva_imagen)
draw_object.line([(10, 150), (190, 150), (190, 190), (10, 190), (10, 150)], fill='black', width=6)
draw_object.rectangle((20, 30, 60, 60), fill='blue')
draw_object.ellipse((120, 30, 160, 60), fill='red')
draw_object.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')

for i in range(100, 200, 10):
    draw_object.line([(i, 0), (200, i - 100)], fill='green')

nueva_imagen.save('files/drawing.png')


# También hay un método para colocar texto, etc.!!!!
