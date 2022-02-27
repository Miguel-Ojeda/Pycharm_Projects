# https://pushkarasharma.github.io/2020/05/05/ASCII.html
# Aquí lo explica...
from PIL import Image, ImageFont, ImageDraw
import sys
from pathlib import Path
import random


gscale_1_fondo_blanco = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale_1_fondo_negro = gscale_1_fondo_blanco[::-1]
gscale_2_fondo_blanco = "@%#*+=-:.   "
gscale_2_fondo_negro = gscale_2_fondo_blanco[::-1]
gscale_3_fondo_blanco = "Ñ@#W$9876543210?!abc;:+=-,._ "
gscale_3_fondo_negro = gscale_3_fondo_blanco[::-1]
ascii_grey_chars = gscale_2_fondo_negro

ASCII_WIDTH = 200
CARACTER_RATIO = 1.8  # es la proporción de un carácter... el alto / ancho...

# picture = Image.open('images/dog_1920.png')
# picture = Image.open('images/ciudad.png')
picture_path = Path.home() / 'Documents/files/aray_perro.jfif'
picture = Image.open(picture_path)
ascii_png_path = Path.home() / f'Documents/files/{picture_path.stem}_ascii.png'

reduction = picture.width // ASCII_WIDTH
ASCII_HEIGHT = int(picture.height / reduction / CARACTER_RATIO)

picture_peque = picture.resize((ASCII_WIDTH, ASCII_HEIGHT))
picture_peque_bn = picture_peque.copy()
# picture_peque_bn = picture.resize((ASCII_WIDTH, ASCII_HEIGHT)).convert('L')


# Si la imagen no tuviera alpha, pues se lo pongo, pq en los cálculos supongo que existe el canal

if picture_peque.mode not in ('RGBA', 'LA'):
    picture_peque.putalpha(1)
    picture_peque_bn.putalpha(1)


# Calculo la luminancia
for row in range(ASCII_HEIGHT):
    alpha = 1
    for col in range(ASCII_WIDTH):
        red, green, blue, alpha = picture_peque_bn.getpixel((col, row))
        # red, green, blue = picture_peque_bn.getpixel((col, row))
        if alpha == 0:
            continue
        luminancia = int(0.30 * red + 0.59 * green + 0.11 * blue)
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


font = ImageFont.truetype('C:/Windows/Fonts/lucon.ttf', 15)
if font is None:
    sys.exit()
char_width = 10
char_height = 18
w, h = picture_peque_bn.size
outputImage = Image.new('RGB', (char_width * w, char_height * h), color=(0, 0, 0))
draw = ImageDraw.Draw(outputImage)


for row in range(ASCII_HEIGHT):
    len_gray = len(ascii_grey_chars)
    for col in range(ASCII_WIDTH):
        luminancia, *resto = picture_peque_bn.getpixel((col, row))
        luminancia = amplificacion * (luminancia - min_luminancia)
        char_luminancia = random.choice(['Ñ', '@', '$'])
        # char_luminancia = ascii_grey_chars[int(luminancia * (len_gray - 1) / 255)]
        # char_luminancia = ascii_grey_chars[-1]
        red, green, blue, alpha = picture_peque.getpixel((col, row))
        draw.text((col * char_width, row * char_height), char_luminancia,
                  font=font, fill=(red, green, blue))

outputImage.save(ascii_png_path)

