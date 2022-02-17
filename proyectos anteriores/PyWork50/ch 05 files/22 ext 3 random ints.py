"""
Create a CSV file, in which each line contains 10 random integers between 10 and 100.
Now read the file back, and print the sum and mean of the numbers on each line.
"""
import random
import csv



def create_csv_10_random(filename='files/random.csv', num_rows=12, num_cols=10):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        for row_index in range(num_rows):
            row = [random.randint(10, 100) for i in range(num_cols)]
            csv_writer.writerow(row)

def calculate_mean_sum(filename):
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for index, row in enumerate(csv_reader):
            suma = sum([int(item) for item in row])
            media = suma / len(row)
            print(f'Fila {index}: suma --> {suma}  /  media --> {media}')


create_csv_10_random('files/random.csv')
calculate_mean_sum('files/random.csv')

