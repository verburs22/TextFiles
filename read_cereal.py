#sarah verburg 06-02

import csv

filename = 'cereal_grains.csv'

with open(filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)


