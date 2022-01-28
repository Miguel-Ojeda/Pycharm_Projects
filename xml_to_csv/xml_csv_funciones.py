import csv
import bs4
# ---> Para usar el parser xml del beautiful soup tiene que estar instalado el módulo lxml

COLUMNAS = ['NIFNIE', 'Nombre', 'FBPA', 'BPA', 'ID', 'PPGES', 'PPAC2/PPAC3',
            'PPAU', 'CE2', 'MENTOR', 'INFB', 'FPS', 'TotalHLC', 'TotalHLC10']

def hlc_data_to_csv(datos, file_csv):

    with open(file_csv, 'w', newline='', encoding='utf-8') as csvfile:
        # Si el diccionario / fila, contiene alguna key que no está en columnas... malo....
        # por eso ponemos raise como extras action, para que si hay alguna key extra,
        # aparte de las de las columnas, que se arroje una excepción...
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNAS, restval=None, extrasaction='raise')
        writer.writeheader()
        writer.writerows(datos)


def extract_hlc_from_xml(file_path):
    datos_hlc = []
    # Almacenaremos los datos de cada centro en una lista cuyos ítems serán diccionarios
    # Cada diccionario va a ser una fila de datos (representando a un profesor con sus horas)
    # Puede haber otras filas que sean el nombre del centro, etc...
    # Las columnas de los datos resultantes son las siguiente...
    # COLUMNAS = ['NIFNIE', 'Nombre .... está arriba pq tb. se utiliza para hacer los csv

    # A veces pondremos filas vacías para separar mejor los datos, añadiendo {}

    # Abrimos el fichero para crear la sopa
    with open(file_path, encoding='UTF-8') as file:
        soup = bs4.BeautifulSoup(file, 'xml')

    # Como luego combinaremos varios centros, para separar un poco, añadimos al inicio una fila en blanco...
    datos_hlc.append({})   # Diccionario en blanco

    # Extraemos el nombre del centro, el código,  el mes, y
    # lo ponemos todo_ junto, en la columna 'Nombre' (simplemente por ser la más ancha)
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
    centro_codigo_mes = nombre_centro + ' (' + codigo_centro + ') ' + mes

    # grabamos ahora el nombre_mes en una fila (o sea, como un diccionario), eligiendo la columna (key) 'Nombre'
    datos_hlc.append({'Nombre': centro_codigo_mes})

    # dejamos una línea de separación, y luego colocamos las observaciones, (en la columna Nombre)
    # y colocamos dos líneas más de separación
    datos_hlc.append({})
    observaciones = soup.Observaciones.get_text().replace('\n', ' - ')  # Quitamos saltos de línea
    datos_hlc.append({'Nombre': observaciones})
    datos_hlc.append({})
    datos_hlc.append({})


    # Ahora toca seleccionar a los docentes...
    '''
    <Docente NIFNIE="54074889A" Apellido1="Alemán" Apellido2="Vega" Nombre="Nicolasa" TotalHLC="1440" TotalHLC10="1560">
    '''
    profesores = soup.select('Docente')

    for profesor in profesores:

        # Para extraer el valor de atributos lo podemos hacer de dos formas...
        # Como si fuera un diccionario: --> profesor['NIFNIE']
        # Con el método get: --> profesor.get('NIFNIE')
        # No sé si es mejor una u otra... el get no de errar si no existiera el valor, sino que retorna None

        # Para cada profesor habrá una línea, que será un diccionario con los campos apropiados
        # Iniciamos una fila vacía para el profesor...
        datos_profesor = {}
        # Y le vamos añadiendo cosas...
        datos_profesor['NIFNIE'] = profesor['NIFNIE']
        # Guardamos el nombre completo unido...
        apellido_1 = profesor['Apellido1']
        apellido_2 = profesor['Apellido2']
        nombre = profesor['Nombre']
        datos_profesor['Nombre'] = ' '.join([apellido_1, apellido_2 + ',', nombre])

        # Los datos de tiempo están en minutos... dividir entre 60
        # No aparece el 10 % suelto, sino ya sumado en Total HLC + 10 %
        datos_profesor['TotalHLC'] = int(profesor['TotalHLC']) / float(60)
        datos_profesor['TotalHLC10'] = int(profesor['TotalHLC10']) / float(60)

        '''
            <DesgloseHLC>
            <Agrupacion Codigo="BPA" Denominacion="Bachillerato de Personas Adultas" Minutos="1440" />
          </DesgloseHLC>
        '''
        # Ahora entramos dentro de cada profesor y buscamos sus hijos, en los que sean tags
        # Si no es tag (hay navigational strings tb) saltamos, pq las nav. strings no tienen atributos y da error
        for child in profesor.DesgloseHLC:
            # Si es un tag pues sacamos los datos (si es texto pues nada)
            if isinstance(child, bs4.element.Tag):
                atributos = child.attrs
                # El valor asociado al atributo 'Codigo' nos va a indica el tipo de hora (BPA, etc)
                datos_profesor[atributos['Codigo']] = int(atributos['Minutos']) / float(60)

        # Pues ya tenemos la fila con todos los datos del profe... la añadimos a la lista de datos...
        datos_hlc.append(datos_profesor)

    # Añadimos una fila en blanco y otra con asteriscos en la columna de DNI y Nombre... para separar centros
    datos_hlc.append({})
    datos_hlc.append({'NIFNIE': '********', 'Nombre': '********************'})
    datos_hlc.append({})


    '''
    Quitar esto de aquí!!! porque el csv lo guardaremos con otra función
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