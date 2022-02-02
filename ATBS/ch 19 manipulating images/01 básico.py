from PIL import Image


# Lo primero, es obtener un objeto tipo imagen, para luego hacerle transformaciones...
cat_image = Image.open('files/zophie.png')
print(type(cat_image))  # --> <class 'PIL.PngImagePlugin.PngImageFile'>

# Podemos obtener fácilmente un montón de atributos de la imagen...
print(f'Las dimensiones de la imagen son: {cat_image.size}')
print(f'El alto es {cat_image.height} y el ancho {cat_image.width}')
print(f'El formato de la imagen es {cat_image.format}, o sea, "{cat_image.format_description}"')

# Podemos fácilmente grabar la imagen en cualquier otro formato
cat_image.save('files/gato.jpg')

'''
Podemos crear nuevos objeto imagen... por ejemplo, damos 
el espacio de color, las dimensiones, y el color (de varias formas se puede pasar todo esto)
Veamos un ejemplo para crear una imagen nueva, fondo naranja, que la grabamos luego como png
'''

fondo_naranja = Image.new('RGBA', (400, 400), 'orange')
# Otra opción fondo_verde = Image.new('RGBA', (400, 400), (0, 255, 0, 255))
fondo_naranja.save('files/fondo_naranja.png')

# Podemos trabajar con los siguientes espacios de color...
# "1", "CMYK", "F", "HSV", "I", "L", "LAB", "P", "RGB", "RGBA", "RGBX", "YCbCr"

# Podemos cropear una imagen dando el bounding  box (left, top, right, bottom)
# recordar que el right, bottom no se incluye

cropped_cat = cat_image.crop((355, 345, 565, 560))
cropped_cat.save('files/cropped_cat.png')

# El método copy nos sirve para crear un duplicado de la imagen...
duplicated_cat = cat_image.copy()
# Ahora, ambos objetos son independientes, podemos transformarlos por separado...

# Vamos a pegar a esta nueva imagen copias del crop con la cara...
duplicated_cat.paste(cropped_cat, (0, 0))
duplicated_cat.paste(cropped_cat, (600, 800))

# el paste modifica el objeto 'inplace'

# y grabamos el montaje con las 2 caras pegadas...
duplicated_cat.save('files/gato_con_varias_caras.png')


# Hagamos una nueva imagen mosaico con 25 caras 5 x 5
ancho_imagen = cropped_cat.width * 5
alto_imagen = cropped_cat.height * 5

nueva_imagen = Image.new('RGBA', (ancho_imagen, alto_imagen))

for y in range(0, alto_imagen, cropped_cat.height):
    for x in range(0, ancho_imagen, cropped_cat.width):
        nueva_imagen.paste(cropped_cat, (x, y))

nueva_imagen.save('files/mosaico.png')


# Resizing...
# 1 creamos una copia que sea 1/4 del original...
ancho_original, alto_original = cat_image.size
gato_reducido_un_cuarto = cat_image.resize((ancho_original // 2, alto_original // 2))
gato_reducido_un_cuarto.save('files/gato_a_un_cuarto.png')

gato_flaco = cat_image.resize((ancho_original // 2, alto_original))
gato_flaco.save('files/gato_flaco.png')


# Rotating and flipping
cat_image.rotate(90).save('files/gato_rotado_90.png')
cat_image.rotate(180).save('files/gato_boca_abajo.png')
'''
Podemos rotar cualquier ángulo...
Si rotamos 15 grados, por ejemplo, tendremos que decir también si queremos que la imagen
resultante mantenga las dimensiones originales (en cuyo caso las esquinas van a desaparecer)
o si queremos expandir para que se muestre todo
'''
cat_image.rotate(6).save('files/rotated6.png')
cat_image.rotate(6, expand=True).save('files/rotated6_expanded.png')

# Para hacer el flipping, utilizar el método transpose...
cat_image.transpose(Image.FLIP_LEFT_RIGHT).save('files/horizontal_flip.png')
cat_image.transpose(Image.FLIP_TOP_BOTTOM).save('files/vertical_flip.png')

# También podemos hacer muchísimas cosas más, claro...
# Coger el valor de un pixel.... im.getpixel(tupla_coordenadas) --> nos devuelve la tupla con el color
# cambiar color im.putpixel(tupla_coordenadas, tupla_color)




