# https://pushkarasharma.github.io/2020/05/05/ASCII.html
# https://www.geeksforgeeks.org/converting-image-ascii-image-python/
# https://bitesofcode.wordpress.com/2017/01/19/converting-images-to-ascii-art-part-1/
# https://bitesofcode.wordpress.com/2017/05/27/converting-images-to-ascii-art-part-2/

"""
ASCII art is a graphic design technique that uses computers for presentation and consists
of pictures pieced together from the 95 printable (from a total of 128) characters defined
by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended
characters (beyond the 128 characters of standard 7-bit ASCII).
Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a
traditional typewriter) such as Courier for presentation.
"""
'''
Steps:
* Convert the input image to grayscale.
* Split the image into M×N tiles.
* Correct M (the number of rows) to match the image and font aspect ratio.
* Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
* Assemble rows of ASCII character strings and print them to a file to form the final image.
'''

from PIL import Image
import sys

#67 levels of gray
# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,\"^`. "
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# 10 niveles
# gscale2 = "@%#*+=-:. "
gscale2 = " %#*+=-:. "[::-1]
# print(len(gscale1))
# sys.exit()

ASCII_WIDTH = 140
CARACTER_RATIO = 2  # es la proporción de un carácter... el alto / ancho...

perro_pic = Image.open('images/dog_1920.png')
reduction = perro_pic.width // 80
ASCII_HEIGHT = int (perro_pic.height / reduction / CARACTER_RATIO)

# perro_peque = perro_pic.resize((ASCII_WIDTH, ASCII_HEIGHT))
perro_peque_bn = perro_pic.resize((ASCII_WIDTH, ASCII_HEIGHT)).convert('L')
'''
for row in range(ASCII_WIDTH):
    for col in range(ASCII_HEIGHT):
        red, green, blue, _ = perro_peque.getpixel((row, col))
        luminance = int(0.30 * red + 0.59 * green + 0.11 * blue)
        perro_peque_bn.putpixel((row, col), luminance)
'''
# Análisis previo de la imagen, para mejorar el contraste...
min_luminance = 255
max_luminance = 0
for row in range(ASCII_HEIGHT):
    for col in range(ASCII_WIDTH):
        perro_peque_bn.getpixel((col, row))
        luminancia = perro_peque_bn.getpixel((col, row))
        if luminancia < min_luminance:
            min_luminance = luminancia
            continue
        elif luminancia > max_luminance:
            max_luminance = luminancia

amplificacion = 1
if max_luminance != min_luminance:
    amplificacion = 255 / (max_luminance - min_luminance)
print(min_luminance, max_luminance, amplificacion)


rows: list[str] = []
for row in range(ASCII_HEIGHT):
    row_string = []
    for col in range(ASCII_WIDTH):
        luminancia = amplificacion * (perro_peque_bn.getpixel((col, row)) - min_luminance)
        # print(luminancia)
        char_luminancia = gscale1[int(luminancia * 69 /255)]
        row_string.append(char_luminancia)
    row_string = ''.join(row_string)
    print(row_string)



# Otra opción simplemente es el método convert... que es lo que dejo...
# perro_peque.convert('L')  # convertimos a imagene de grises, sólo con canal luminancia!!!
# perro_peque.save('images/perro_peque.png')
perro_peque_bn.save('images/perro_peque_bn.png')




'''
# open a new text file
>>> f = open(outFile, 'w')
# write each string in the list to the new file
>>> for row in aimg:
...    f.write(row + '\n')
# clean up
>>> f.close()
'''
