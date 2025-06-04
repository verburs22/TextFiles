#sarah verburg 06-03

import csv

countries = {}

filename = 'country_info.txt'
dialect = csv.excel
dialect.delimiter ='|'

with open(filename, encoding='utf-8', newline='') as country_file:
    #get the colum heading from the first like of file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for i, head in enumerate(headings):
        headings[i] = head.casefold()
    reader = csv.DictReader(country_file, dialect= dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)

while True:
    choice  = input("Please enter a country to get its capital: ").casefold()
    if choice in countries:
        count = countries[choice]
        print("The capital of ", choice, " is", count['capital'])
    elif choice == 'quit':
        break
    else:
        print(choice, "is not in dictionary, please try again")
