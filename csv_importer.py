import csv
from flask import jsonify
import requests

url = 'http://127.0.0.1:6568/api/restaurant'

a_csv_file = open('src/persistent/work_sheet/work_sheet_file.csv', "r")
dict_reader = csv.DictReader(a_csv_file)
ordered_dict_from_csv = list(dict_reader)

for restaurant in ordered_dict_from_csv:
    restaurant['categories'] = restaurant['categories'].split(' and ')
    restaurant['websites'] = restaurant['websites'].split(',')
    
    restaurant['name'] = restaurant['name'].replace("'", "\\'")
    restaurant['postal_code'] = restaurant['postalCode']
    del(restaurant['postalCode'])

    requests.post(url, json = (restaurant))
