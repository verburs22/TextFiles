#sarah verburg 06-03

countries = {}

filename = 'country_info.txt'

with open(filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        #print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        #print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

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
