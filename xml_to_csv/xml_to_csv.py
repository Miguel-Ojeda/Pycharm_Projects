from pathlib import Path
import time
from xml_csv_funciones import hlc_data_to_csv, extract_hlc_from_xml



# xml_path = 'C:/Users/Angel Ojeda/Documents/Miguel/xml/sl.xml'
xml_file = 'D:/Documentos/XML noviembre/Santa Lucia de Tirajana.xml'
csv_file = 'D:/Documentos/XML noviembre/Santa Lucia de Tirajana.csv'


datos_hlc = extract_hlc_from_xml(xml_file)
for item in datos_hlc:
    print(item)

hlc_data_to_csv(datos_hlc, csv_file)

'''
path_xml_dir = Path('D:/Documentos/HLC prueba')
# Creamos el subdirectorio para los ficheros CSV, basándonos en la fecha y hora actual
str_time = time.strftime('%y%m%d-%H%M%S')
path_csv_dir = path_xml_dir / str_time
path_csv_dir.mkdir(exist_ok=True)

# Vamos a almacenar los datos de cada centro en una lista
# Cada fila será un diccionario que representa una fila en el resultado del CSV
lista_datos_centros = []

# --------------------
for _, xml_file in enumerate(path_xml_dir.glob('*.[xX][mM][lL]')):
   
    # Extraemos los datos de cada centro... va a ser una lista de diccioanrios... cada diccionario
    # representa una fila con los datos de un profesor...
    datos_centro = extract_hlc_from_xml(xml_file)
    csv_file = path_csv_dir / f'{xml_file.stem}.csv'
    hlc_data_to_csv(datos_centro, csv_file)


    # Añadimos los datos de cada centro al listado
    # lista_datos_centros.append(datos_centro)

'''

'''
# Ahora nos queda combinar los datos de todos los centros y crear el csv...
datos_todos_centros = pd.concat(lista_datos_centros)
datos_todos_centros.to_csv(path_csv / 'todos_los_centros.csv', header=False, index=False)
# Para pasar a excel hace falta tener instalado también el módulo openpyxl
datos_todos_centros.to_excel(path_csv / 'todos_los_centros.xlsx', sheet_name='HLC', header=False, index=False)
'''

