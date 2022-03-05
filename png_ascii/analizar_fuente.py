'''
ImageDraw.textbbox(xy, text, font=None, anchor=None, spacing=4, align='left',
direction=None, features=None, language=None, stroke_width=0, embedded_color=False)[source]¶
Returns bounding box (in pixels) of given text relative to given anchor when rendered in font with provided direction,
features, and language. Only supported for TrueType fonts.

Use textlength() to get the offset of following text with 1/64 pixel precision.
The bounding box includes extra margins for some fonts, e.g. italics or accents.

Parameters
xy – The anchor coordinates of the text.
text – Text to be measured. If it contains any newline characters, the text is passed on to multiline_textbbox().
font – A FreeTypeFont instance.
anchor – The text anchor alignment. Determines the relative location of the anchor to the text.
The default alignment is top left. See Text anchors for valid values. This parameter is ignored for non-TrueType fonts.
spacing – If the text is passed on to multiline_textbbox(), the number of pixels between lines.
align – If the text is passed on to multiline_textbbox(), "left", "center" or "right".
Determines the relative alignment of lines. Use the anchor parameter to specify the alignment to xy.

direction – Direction of the text. It can be "rtl" (right to left), "ltr" (left to right) or "ttb" (top to bottom).
Requires libraqm.

features – A list of OpenType font features to be used during text layout.
This is usually used to turn on optional font features that are not enabled by default, for example "dlig" or "ss01", but can be also used to turn off default font features, for example "-liga" to disable ligatures or "-kern" to disable kerning. To get all supported features, see OpenType docs. Requires libraqm.

language – Language of the text. Different languages may use different glyph shapes or ligatures.
This parameter tells the font which language the text is in, and to apply the correct substitutions as appropriate, if available. It should be a BCP 47 language code. Requires libraqm.

stroke_width – The width of the text stroke.

embedded_color – Whether to use font embedded color glyphs (COLR, CBDT, SBIX).
'''
import pprint

from PIL import Image, ImageFont, ImageDraw
from unicode_auxiliar import RangoUnicode, unicode_bloques
from collections import defaultdict
import sys



def analiza_rango_unicode(rango: RangoUnicode, font_type: str = 'C:/Windows/Fonts/arial.ttf', font_size=40)\
        -> dict[str, list]:
    font = ImageFont.truetype(font_type, font_size)
    if font is None:
        font = ImageFont.load_default()

    # Crearemos nuestros test en una imagen... tamaño proporcional al size
    # test_image = Image.new(mode='L', size=(5 * font_size, 5 * font_size), color=0)
    # black_image = test_image.copy()
    # draw = ImageDraw.Draw(test_image)
    luminosidad: dict[str, float] = {}

    # for unicode in range(rango.start_id, rango.end_id + 1):
    for unicode in range(rango.start_id, rango.end_id + 1):

        test_image = Image.new(mode='L', size=(5 * font_size, 5 * font_size), color=0)
        draw = ImageDraw.Draw(test_image)
        draw.text((0, 0), chr(unicode), font=font, fill=255)
        # x0, y0, x1, y1 = draw.textbbox((0, 0), chr(unicode), font=font)
        lum_acumulada = 0
        for x in range(0, 100):
            for y in range(0, 100):
                lum_acumulada += test_image.getpixel((x, y))
        luminosidad[chr(unicode)] = lum_acumulada
        # test_image.paste(black_image)

    # Ahora buscamos el valor con más luminosidad...
    max_lum = max(luminosidad.values())
    return {key: (255 * val / max_lum) for key, val in luminosidad.items()}

if __name__ == '__main__':
    resultado = analiza_rango_unicode(unicode_bloques)
    pprint.pprint(resultado)






