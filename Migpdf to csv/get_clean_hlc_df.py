import pandas as pd
import tabula
from pathlib import Path

# Opciones para ver mejor los df al imprimir....
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 15)


def get_clean_hlc_df(lista_df: list, centro=None, observaciones=None):
    """
    lista_df es la lista de dataframes que nos devuelve tabula al leer el pdf...
    Tiene errores y detecta mal los nombres de las columnas... haciendo que se extiendan
    varias filas verticalmente, con lo que hay filas sin datos que hay que borrar...

    centro: aquí debería estar el nombre del centro detectado en el pdf

    observaciones: aquí deberían estar las observaciones detectadas en el pdf

    La función...
    Quita las filas sin datos (por ejemplo, el nombre de la columna de redondeo se extiende
    verticalmente a 4 celdas... con lo que se crean 3 filas sin datos, innecesarias...

    También habrá que combinar todos los df existentes... se crea un df por tabla (en nuestro caso por página con datos)

    Añadimos algunas filas antes y después de los datos...
    En las filas de antes pondremos el nombre del centro y las observacioens detectadas en el pdf

    La función nos devuelve ya el dataframe corregido...
    """

    if not centro:
        centro = 'Centro...'
    if not observaciones:
        observaciones = 'Observaciones...'

    # El nombre que van a tener las columnas en el dataframe (tb en los datos en sí)
    columnas = ['DNI', 'Nombre', 'FBPA', 'BPA', 'ID', 'PPGES', 'PPAC2/PPAC3',
                'PPAU', 'CE2', 'MENTOR', 'INFB', 'FPS', 'Redondeo', 'Total HLC']

    for df in lista_df:
        df.columns = columnas
        df.dropna(subset=['DNI'], inplace=True)
        # Esto no debería hacer falta, pero...
        # Estamos eliminando filas que no tienen datos, pero que existen pq
        # los nombres de las columnas tabula detecta que ocupan varias celdas verticalmente!!!
        # Quizás utilizar otro detector???

    df_datos = pd.concat(lista_df, ignore_index=True)
    # CORRECCIÓN de los nombres de las columnas pq se graban mal en la tabla que detecta tabula...
    df_datos.loc[0]['PPAC2/PPAC3'] = 'PPAC2/PPAC3'
    df_datos.loc[0]['MENTOR'] = 'MENTOR'
    df_datos.loc[0]['Redondeo'] = 'Redondeo'

    # Creamos data frames para usar como prefijo y sufijo a los datos...
    fila_vacia = ['' for i in range(len(columnas))]
    fila_separadora = ['-------' for i in range(len(columnas))]

    df_entrada = pd.DataFrame(data=[fila_vacia, fila_vacia, fila_vacia, fila_vacia, fila_vacia, fila_vacia],
                              columns=columnas)

    # Añadimos el centro y las observaciones detectadas en el pdf que nos han pasado...
    df_entrada.at[1, 'Nombre'] = centro
    df_entrada.at[2, 'Nombre'] = observaciones

    df_salida = pd.DataFrame(data=[fila_vacia, fila_vacia, fila_separadora, fila_vacia, fila_vacia], columns=columnas)
    df_resultado = pd.concat([df_entrada, df_datos, df_salida], ignore_index=True)

    return (df_resultado)


if __name__ == '__main__':

    path_folder = Path.home() / 'Documents/Miguel/HLC'
    path_pdf = path_folder / 'ejemplo6.pdf'
    path_csv = path_folder / f'{path_pdf.stem}.csv'

    lista_df = tabula.read_pdf(input_path=path_pdf, pages='all')

    df = get_clean_hlc_df(lista_df, centro=path_pdf.stem)
    df.to_csv(path_csv, header=False, index=False)
    print(df)

