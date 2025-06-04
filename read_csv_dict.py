#sarah verburg 06-04

import csv

filename = 'cereal_grains.csv'

with open(filename, encoding='utf-8', newline='') as cereal_file:
    reader = csv.DictReader(cereal_file)
    for row in reader:
        print(row)