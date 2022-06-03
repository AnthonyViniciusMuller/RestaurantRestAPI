# RestaurantRestAPI 

> Disclaimer

This repository is just a challenge to create an REST API using python and the Clean Architecture 
It was quite the challenge as it's been 5 year since the last time I touched python, I've never created anything with the Uncle Bob's architecture and made it in my spare time in only three days .

> Dependencies

To run it you just need a MySQL server, the dump is located in 'src/persistent/MySQL/data_base/dump', and Python3, the dependencies are in the 'requirements.txt' file. 

> How to run

There are two services, one called 'app.py' to run the API, it will be visible in this url: http://127.0.0.1:6568/api/restaurant, and other to import the CSV file called 'csv_importer.py'.

To run then, just use your python interpreter and the file name: `/usr/bin/python app.py`
