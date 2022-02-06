"""
Extend this exercise by asking the user to enter a space-separated list of integers,
indicating which fields should be written to the output CSV file.
Also ask the user which character should be used as a delimiter in the output file.
Then read from /etc/passwd, writing the user’s chosen fields, separated by the user’s
chosen delimiter.
"""
import csv
from pathlib import Path
import pprint


def pass_to_csv(passwd_file, csv_file=None, columnas_seleccionadas='0 2', delimiter='\t'):
    if not csv_file:
        base_dir = Path(passwd_file).parent
        csv_file = base_dir / f'{Path(passwd_file).stem}.csv'
    # Ahora hallamos los campos que queremos pillar...
    columnas_seleccionadas = [int(item) for item in columnas_seleccionadas.split()]
    with open(passwd_file) as password, open(csv_file, 'w', newline='') as name_uid_csv:
        pass_reader = csv.reader(password, delimiter=':')
        name_uid_writer = csv.writer(name_uid_csv, delimiter='\t')
        for row in pass_reader:
            # if len(row) > 1:  # Creo que es mejor la opción que dejo...
            if not row[0].startswith('#'):
                # pprint.pprint(row)
                name_uid_writer.writerow([row[i] for i in columnas_seleccionadas])


pass_to_csv('files/passwd.txt', columnas_seleccionadas='0 2 8 9')
