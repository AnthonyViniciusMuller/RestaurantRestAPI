# RestaurantRestAPI 

> Disclaimer

This repository is just a challenge to create an REST API using python and the Clean Architecture 
It was quite the challenge as it's been 5 year since the last time I touched python, I've never created anything with the Uncle Bob's architecture and made it in my spare time in only three days .

> Dependencies

To run it you just need a MySQL server, the dump is located in 'src/persistent/MySQL/data_base/dump', and Python3, the dependencies are in the 'requirements.txt' file. 

> How to run

There are two services, one called 'app.py' to run the API, it will be visible in this url: http://127.0.0.1:6568/api/restaurant, and other to import the CSV file called 'csv_importer.py'.

To run then, just use your python interpreter and the file name: `/usr/bin/python app.py`

The json to be sent to POST and PUT methods needs to be with this orgazation, with the only fields that can't be null are 'name' and 'postal_code'

```
{
    "address": "800 N Canal Blvd",
    "categories": [
        "American Restaurant",
        "Fast Food Restaurant"
    ],
    "city": "Thibodaux",
    "country": "US",
    "id": 1,
    "latitude": 29.8147,
    "longitude": -90.8147,
    "name": "SONIC Drive In",
    "postal_code": "70301",
    "province": "LA",
    "websites": [
        "http://sonicdrivein.com",
        "http://www.sonicdrivein.com",
        "https://locations.sonicdrivein.com/la/thibodaux/800-north-canal-boulevard.html"
    ]
}
