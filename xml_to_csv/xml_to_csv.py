import bs4  # Beautiful Soup para el análisis de xml, html, ...
# lxml tb tiene que estar instalado
from pathlib import Path
import pprint



def extract_hlc_from_xml(file_path):
    # datos_hlc = dict()
    datos_hlc = []
    # quizás mejor una nt para q esté ordenado como yo quiera'?



    with open(file_path, encoding='UTF-8') as file:
        soup = bs4.BeautifulSoup(file, 'xml')


    # file = open(file_path, 'r', encoding="UTF-8")
    # contenido = file.read()
    # file.close()
    # # print(contenido)


    # soup = bs4.BeautifulSoup(contenido, parser='lxml', features='lxml')

    # Extraemos el nombre del centro
    '''
    <NombreCentro>SANTA LUCÍA DE TIRAJANA</NombreCentro>
    '''
    '''
    seleccion = soup.select('NombreCentro')
    # datos_hlc['centro'] = seleccion[0].getText()
    datos_hlc.append(seleccion[0].getText())
    '''
    datos_hlc.append(soup.NombreCentro.string)


    # Extraemos el mes
    '''
    <NombreCertificacion>
    Certificación mensual de HLC para Educación de Personas Adultas - Noviembre 2021
    </NombreCertificacion>
    '''
    '''
    seleccion = soup.select('NombreCertificacion')
    texto = seleccion[0].getText().split('- ')[-1]
    # datos_hlc['mes'] = texto
    datos_hlc.append(texto)
    '''
    mes = soup.NombreCertificacion.string.split('- ')[-1]
    datos_hlc.append(mes)

    # Profesores (de momento DNI y totales)
    '''
    <Docente NIFNIE="54074889A" Apellido1="Alemán" Apellido2="Vega" Nombre="Nicolasa" TotalHLC="1440" TotalHLC10="1560">
    '''
    seleccion = soup.select('Docente')


    # profe = seleccion[-1]
    # horas_profe = dict()
    # print(type(profe))
    # # print(profe.name)
    # # print(profe.contents)
    # for i, child in enumerate(profe.DesgloseHLC):
    #     try:
    #         print(i, child, type(child), child.name, child.attrs)
    #         atributos = child.attrs
    #         horas_profe[atributos['Codigo']] = atributos['Minutos']
    #
    #     except:
    #         pass

    for profesor in seleccion:
        '''
        # Opción con get....
        NIFNIE = profesor.get('NIFNIE')
        apellido_1 = profesor.get('Apellido1')
        apellido_2 = profesor.get('Apellido2')
        nombre = profesor.get('Nombre')
        total_hlc = int(profesor.get('TotalHLC')) / float(60)           # Los datos están en minutos... pasar a horas
        total_hlc_10 = int(profesor.get('TotalHLC10')) / float(60)      # Los datos están en minutos... pasar a horas
        '''

        # Opción tipo diccionario... equivalente a la anterior
        NIFNIE = profesor['NIFNIE']
        apellido_1 = profesor['Apellido1']
        apellido_2 = profesor['Apellido2']
        nombre = profesor['Nombre']
        total_hlc = int(profesor['TotalHLC']) / float(60)  # Los datos están en minutos... pasar a horas
        total_hlc_10 = int(profesor['TotalHLC10']) / float(60)  # Los datos están en minutos... pasar a horas



        '''
            <DesgloseHLC>
            <Agrupacion Codigo="BPA" Denominacion="Bachillerato de Personas Adultas" Minutos="1440" />
          </DesgloseHLC>
        '''
        horas_profe = {}
        for child in profesor.DesgloseHLC:
            try:
                atributos = child.attrs
                horas_profe[atributos['Codigo']] = int(atributos['Minutos']) / float(60)
            except:
                pass

        tupla_profe = (NIFNIE, apellido_1, apellido_2, nombre, total_hlc, total_hlc_10, horas_profe)
        datos_hlc.append(tupla_profe)

    return datos_hlc


xml_path = 'C:/Users/Angel Ojeda/Documents/Miguel/xml/sl.xml'
datos_hlc = extract_hlc_from_xml(xml_path)

for item in datos_hlc:
    print(item)

