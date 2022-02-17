"""
For this exercise, create a function, passwd_to_csv, that takes two filenames as
arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
https://docs.python.org/3/library/csv.html?module-csv
"""

import csv
from pathlib import Path


def pass_to_csv(passwd_file, csv_file=None):
    if not csv_file:
        base_dir = Path(passwd_file).parent
        csv_file = base_dir / f'{Path(passwd_file).stem}.csv'
    with open(passwd_file) as password, open(csv_file, 'w', newline='') as name_uid_csv:
        pass_reader = csv.reader(password, delimiter=':')
        name_uid_writer = csv.writer(name_uid_csv, delimiter='\t')
        for row in pass_reader:
            # if len(row) > 1:  # Creo que es mejor la opción que dejo...
            if not row[0].startswith('#'):
                name_uid_writer.writerow([row[0], row[2]])


pass_to_csv('files/passwd.txt')
