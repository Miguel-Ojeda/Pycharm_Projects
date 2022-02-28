# https://www.unicode.org/versions/Unicode14.0.0/
# descargando de files el CodeCharts.pdf de 100 Megas

from typing import NamedTuple

class RangoUnicode(NamedTuple):
    start_id: int
    end_id: int
    description: str


unicode_bloques = RangoUnicode(start_id=0x2580, end_id=0x259F, description='Bloques')
unicode_geometric_shapes = RangoUnicode(start_id=0x25A0, end_id=0x25FF, description='Formas geométricas')
unicode_geometric_shapes_extended = RangoUnicode(start_id=0x01f780,
                                                 end_id=0x01f7eb, description='Formas geométricas Extendidas')
unicode_miscellaneous_symbols = RangoUnicode(start_id=0x2600, end_id=0x26ff, description='Símbolos misceláneos')
unicode_dingbats = RangoUnicode(start_id=0x2700, end_id=0x27bf, description='Dingbats')
unicode_braille = RangoUnicode(start_id=0x2800, end_id=0x28ff, description='Símbolos Braille')
unicode_symbols_for_legacy_computing = RangoUnicode(start_id=0x01fb00, end_id=0x01fbca, description='Legacy Computing')
unicode_yijing_hexagram_symbols = RangoUnicode(start_id=0x4dc0, end_id=0x4dff, description='Hexagramas')
unicode_cuneiforme = RangoUnicode(start_id=0x012000, end_id=0x0120ff, description='Cuneiforme')
unicode_egipcio = RangoUnicode(start_id=0x013000, end_id=0x0130DF, description='Jeroglífico Egipcio')
unicode_suplemento_bamum = RangoUnicode(start_id=0x016800, end_id=0x0168BF, description='Suplemento Bamum')
unicode_mayan_numerals = RangoUnicode(start_id=0x01D2E0, end_id=0x01D2FF, description='Numeración Maya')
unicode_Tai_Xuan_Jing_Symbols = RangoUnicode(start_id=0x1D300, end_id=0x1D356, description='Tai Xuan Jing Symbols')
unicode_misc_sym_and_pic = RangoUnicode(start_id=0x1F300, end_id=0x1F3FF, description='Miscellaneous Symbols and Pictographs')
unicode_emoticons = RangoUnicode(start_id=0x1F600, end_id=0x1F64F, description='Emoticonos')


'''
unicode_ = RangoUnicode(start_id=0x, end_id=0x, description='')
'''

def display_unicode(rango: RangoUnicode) -> None:
    ANCHO = 60
    separador = f' {chr(0x2502)} '  # │
    print('\n', rango.description.center(ANCHO), '\n')
    caracteres = separador.join([chr(i) for i in range(rango.start_id, rango.end_id + 1)])
    for i in range(0, len(caracteres), ANCHO):
        print(caracteres[i: i+ANCHO])


display_unicode(unicode_bloques)
display_unicode(unicode_geometric_shapes)
display_unicode(unicode_miscellaneous_symbols)
display_unicode(unicode_dingbats)
display_unicode(unicode_braille)
display_unicode(unicode_symbols_for_legacy_computing)
display_unicode(unicode_geometric_shapes_extended)
display_unicode(unicode_yijing_hexagram_symbols)
display_unicode(unicode_cuneiforme)
display_unicode(unicode_egipcio)
display_unicode(unicode_suplemento_bamum)
display_unicode(unicode_mayan_numerals)
display_unicode(unicode_Tai_Xuan_Jing_Symbols)
display_unicode(unicode_misc_sym_and_pic)
display_unicode(unicode_emoticons)





