"""
Write a function that writes a dict to a CSV file.
Each line in the CSV file should contain three fields:
(1) the key, which we’ll assume to be a string,
(2) the value, and
(3) the type of the value (e.g., str or int).
"""
import csv


def dict_to_csv(dict, csv_name='files/diccionario.csv'):
    with open(csv_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        for key, value in dict.items():
            csv_writer.writerow([key, value, type(value)])


def dict_to_csv_2(dict, csv_name='files/diccionario_2.csv'):
    with open(csv_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, delimiter='\t', fieldnames=['key', 'value', 'type'])
        for key, value in dict.items():
            csv_writer.writerow({'key': key, 'value': value, 'type': type(value)})


diccionario = {'nombre': 'Juan', 0: {14}, 'edad': 42,
               'teléfono': 609856432, 5: [1, 2, '54'], 'profesión': 'fontanero'}
dict_to_csv(diccionario)
dict_to_csv_2(diccionario)