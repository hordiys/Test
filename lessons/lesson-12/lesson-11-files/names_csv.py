import csv

def check_city(city_name, row):
    return row['city'] == city_name


city = 'Odesa'
source_file = 'd:\courses\GoITeens\python\!my\lesson-12\code\pupils.csv'

with open(source_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if check_city(city, row):
            print(row['name'])
