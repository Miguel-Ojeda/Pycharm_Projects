# https://pushkarasharma.github.io/2020/05/05/ASCII.html
# https://www.geeksforgeeks.org/converting-image-ascii-image-python/
# https://bitesofcode.wordpress.com/2017/01/19/converting-images-to-ascii-art-part-1/
# https://bitesofcode.wordpress.com/2017/05/27/converting-images-to-ascii-art-part-2/
'''
# Veo que lo del contraste no sirve, pq, al perder al canal alfa (pq transoformo con el método
convert('L') la mínima luminancia siempre va a ser 0 (para los píxeles transparente)
con lo que no optimmizao... por ello, no utilizaré el método convert... para pasar a Grises
sino lo haré manualmente.... como cuando empecé
'''

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
from pathlib import Path

#67 levels of gray
# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,\"^`. "
gscale_1_fondo_blanco = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale_1_fondo_negro = gscale_1_fondo_blanco[::-1]
# 10 niveles
# gscale2 = "@%#*+=-:. "
gscale_2_fondo_blanco = "@%#*+=-:.  "
gscale_2_fondo_negro = gscale_2_fondo_blanco[::-1]
gscale_3_fondo_blanco = "Ñ@#W$9876543210?!abc;:+=-,._ "
gscale_3_fondo_negro = gscale_3_fondo_blanco[::-1]
# print(len(gscale1))
# sys.exit()
ascii_grey_chars = gscale_2_fondo_blanco

ASCII_WIDTH = 400
CARACTER_RATIO = 2.4  # es la proporción de un carácter... el alto / ancho...

# picture = Image.open('images/dog_1920.png')
# picture = Image.open('images/ciudad.png')
picture_path = Path.home() / 'Documents/files/aray_2.jfif'
picture = Image.open(picture_path)
ascii_path = Path.home() / f'Documents/files/{picture_path.stem}.txt'

reduction = picture.width // ASCII_WIDTH
ASCII_HEIGHT = int(picture.height / reduction / CARACTER_RATIO)

picture_peque_bn = picture.resize((ASCII_WIDTH, ASCII_HEIGHT))
# picture_peque_bn = picture.resize((ASCII_WIDTH, ASCII_HEIGHT)).convert('L')


# Si la imagen no tuviera alpha, pues se lo pongo, pq en los cálculo supongo que existe el canal

if picture_peque_bn.mode not in ('RGBA', 'LA'):
    picture_peque_bn.putalpha(1)

# Calculo la luminancia
for row in range(ASCII_HEIGHT):
    alpha = 1
    for col in range(ASCII_WIDTH):
        red, green, blue, alpha = picture_peque_bn.getpixel((col, row))
        # red, green, blue = picture_peque_bn.getpixel((col, row))
        if alpha == 0:
            continue
        # luminancia = int(0.30 * red + 0.59 * green + 0.11 * blue)
        luminancia = int(0.33 * red + 0.33 * green + 0.33 * blue)

        picture_peque_bn.putpixel((col, row), (luminancia, luminancia, luminancia))

# perro_peque_bn.save('images/ppbn.sinoptimizar.png')


# Optimización...
# Análisis previo de la imagen, para mejorar el contraste...
min_luminancia = 255
max_luminancia = 0
for row in range(ASCII_HEIGHT):
    for col in range(ASCII_WIDTH):

        luminancia, _, _, alpha = picture_peque_bn.getpixel((col, row))
        if alpha == 0:
            continue
        elif luminancia < min_luminancia:
            min_luminancia = luminancia
            continue
        elif luminancia > max_luminancia:
            max_luminancia = luminancia

amplificacion = 1
if max_luminancia != min_luminancia:
    amplificacion = 255 / (max_luminancia - min_luminancia)
print(min_luminancia, max_luminancia, amplificacion)
# sys.exit()

rows: list[str] = []
output = open(ascii_path, 'w', encoding='utf-8')
for row in range(ASCII_HEIGHT):
    len_gray = len(ascii_grey_chars)
    row_string = []
    for col in range(ASCII_WIDTH):
        # luminancia, *resto = amplificacion * (perro_peque_bn.getpixel((col, row)) - min_luminancia)
        luminancia, *resto = picture_peque_bn.getpixel((col, row))
        luminancia = amplificacion * (luminancia - min_luminancia)
        # print(luminancia)
        char_luminancia = ascii_grey_chars[int(luminancia * (len_gray - 1) / 255)]
        row_string.append(char_luminancia)
    row_string.append('\n')
    row_string = ''.join(row_string)
    output.write(row_string)
    print(row_string[:-1])

output.close()



# Otra opción simplemente es el método convert... que es lo que dejo...
# perro_peque.convert('L')  # convertimos a imagene de grises, sólo con canal luminancia!!!
# perro_peque.save('images/perro_peque.png')
# perro_peque_bn.save('images/perro_peque_bn.png')




'''
# open a new text file
>>> f = open(outFile, 'w')
# write each string in the list to the new file
>>> for row in aimg:
...    f.write(row + '\n')
# clean up
>>> f.close()
'''
