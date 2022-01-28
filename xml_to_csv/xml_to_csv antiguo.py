from pathlib import Path
import time
from xml_csv_funciones import hlc_data_to_csv, extract_hlc_from_xml


def extract_hlc_from_xml(file_path):
    # Los datos del centro se van a guardar en una lista
    # Cada ítem de la lista va a ser un diccionario, cuyas claves son las columnas, que tendrán los repectivos valores
    datos_hlc = []

    # Cada fila será un diccionario... cuyos keys representan las siguietnes columnas...
    COLUMNAS = ['NIFNIE', 'Nombre', 'FBPA', 'BPA', 'ID', 'PPGES', 'PPAC2/PPAC3',
                'PPAU', 'CE2', 'MENTOR', 'INFB', 'FPS', 'TotalHLC', 'TotalHLC10']
    fila_vacia = {}

    # Abrimos el fichero para crear la sopa
    with open(file_path, encoding='UTF-8') as file:
        soup = bs4.BeautifulSoup(file, 'xml')


    # Para separar a cada centro del resto, pues añadimos primero una fila en blanco a los datos...
    datos_hlc.append({})   # Diccionario en blanco

    # Extraemos el nombre del centro, el código,  el mes, y
    # lo ponemos todo_ junto, en la columna apellidos nombre (la más ancha)
    '''
    <NombreCentro>SANTA LUCÍA DE TIRAJANA</NombreCentro>
    '''
    nombre_centro = soup.NombreCentro.string

    '''
    <CodigoCentro>38011111</CodigoCentro>
    '''
    codigo_centro = soup.CodigoCentro.string

    '''
        <NombreCertificacion>
        Certificación mensual de HLC para Educación de Personas Adultas - Noviembre 2021
        </NombreCertificacion>
    '''
    mes = soup.NombreCertificacion.string.split('- ')[-1]
    nombre_centro_mes = nombre_centro + ' (' + codigo_centro + ') ' + mes

    # grabamos ahora el nombre_mes en una fila (o sea, como un diccionario), eligiendo la columna (key) 'Nombre'
    datos_hlc.append({'Nombre': nombre_centro_mes})

    # dejamos una línea de separación, y luego colocamos las observaciones, (en la columna Nombre)
    # y colocamos dos líneas más de separación
    datos_hlc.append({})
    observaciones = soup.Observaciones.get_text().replace('\n', ' - ')  # Quitamos saltos de línea
    datos_hlc.append({'Nombre': observaciones})
    datos_hlc.append({})
    datos_hlc.append({})


    '''
    <Docente NIFNIE="54074889A" Apellido1="Alemán" Apellido2="Vega" Nombre="Nicolasa" TotalHLC="1440" TotalHLC10="1560">
    '''
    # Seleccionamos todos los docentes...
    profesores = soup.select('Docente')

    for profesor in profesores:
        '''
        # Opción con get....
        NIFNIE = profesor.get('NIFNIE')
        apellido_1 = profesor.get('Apellido1')
        apellido_2 = profesor.get('Apellido2')
        nombre = profesor.get('Nombre')
        total_hlc = int(profesor.get('TotalHLC')) / float(60)           # Los datos están en minutos... pasar a horas
        total_hlc_10 = int(profesor.get('TotalHLC10')) / float(60)      # Los datos están en minutos... pasar a horas
        '''
        # Para cada profesor habrá una línea, que será un diccionario con los campos apropiados
        datos_profesor = {}  # Iniciamos una fila vacía para el profesor...
        # Extraemos DNI, NOmbre y apellidos, el total de hlc y con el 10 %
        datos_profesor['NIFNIE'] = profesor['NIFNIE']
        apellido_1 = profesor['Apellido1']
        apellido_2 = profesor['Apellido2']
        nombre = profesor['Nombre']
        datos_profesor['Nombre'] = ' '.join([apellido_1, apellido_2 + ',', nombre])
        # Los datos de tiempo están en minutos... dividir entre 60
        datos_profesor['TotalHLC'] = int(profesor['TotalHLC']) / float(60)
        datos_profesor['TotalHLC10'] = int(profesor['TotalHLC10']) / float(60)

        '''
            <DesgloseHLC>
            <Agrupacion Codigo="BPA" Denominacion="Bachillerato de Personas Adultas" Minutos="1440" />
          </DesgloseHLC>
        '''
        # horas_profe = {}
        for child in profesor.DesgloseHLC:
            # Si es un tag pues sacamos los datos (si es texto pues nada)
            if isinstance(child, bs4.element.Tag):
                atributos = child.attrs
                datos_profesor[atributos['Codigo']] = int(atributos['Minutos']) / float(60)

        # tupla_profe = (NIFNIE, apellido_1, apellido_2, nombre, total_hlc, total_hlc_10, horas_profe)
        datos_hlc.append(datos_profesor)

    # Añadimos una fila en blanco y otra con asteriscos en la columna de DNI y Nombre...
    datos_hlc.append({})
    datos_hlc.append({'NIFNIE': '********', 'Nombre': '********************'})
    datos_hlc.append({})
    '''
    Quitar esto de aquí!!!
    # Guardamos un csv!!!
    file_csv = file_path[:-3] + 'csv'
    # csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)¶
    with open(file_csv, 'w', newline='', encoding='utf-8') as csvfile:
        # Si el diccionario / fila, contiene alguna key que no está en columnas... malo....
        # por eso ponemos raise como extras action, para que si hay alguna key extra, aparte de las de las columnas
        # que se arroje una excepción...
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNAS, restval=None, extrasaction='raise')
        writer.writeheader()
        writer.writerows(datos_hlc)
    '''
    return datos_hlc



# ------------------------------------------



'''
# xml_path = 'C:/Users/Angel Ojeda/Documents/Miguel/xml/sl.xml'
xml_path = 'D:/Documentos/XML noviembre/Santa Lucia de Tirajana.xml'
datos_hlc = extract_hlc_from_xml(xml_path)
for item in datos_hlc:
    print(item)
# pprint.pprint(datos_hlc)

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
    '''
    sg.one_line_progress_meter(f'Procesando {numero_de_pdfs} PDFs...', _ + 1, numero_de_pdfs,
                               f'Procesando fichero {_ + 1} de {numero_de_pdfs} --> {nombre_del_fichero}',
                               key='HLC_METER', orientation='h', no_button=True)
    '''
    # Extraemos los datos de cada centro... va a ser una lista de diccioanrios... cada diccionario
    # representa una fila con los datos de un profesor...
    datos_centro = extract_hlc_from_xml(xml_file)
    csv_file = path_csv_dir / f'{xml_file.stem}.csv'
    hlc_data_to_csv(datos_centro, csv_file)


    # Añadimos los datos de cada centro al listado
    # lista_datos_centros.append(datos_centro)



'''
# Ahora nos queda combinar los datos de todos los centros y crear el csv...
datos_todos_centros = pd.concat(lista_datos_centros)
datos_todos_centros.to_csv(path_csv / 'todos_los_centros.csv', header=False, index=False)
# Para pasar a excel hace falta tener instalado también el módulo openpyxl
datos_todos_centros.to_excel(path_csv / 'todos_los_centros.xlsx', sheet_name='HLC', header=False, index=False)
'''

