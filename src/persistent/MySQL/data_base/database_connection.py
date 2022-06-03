import mysql.connector
from mysql.connector import Error

class DataBaseConnectionHandler:

    def __init__(self):
        __host = 'localhost'
        __user_name = 'root'
        __password = ''
        __database = 'INDICO'

        try:
            self.connection = mysql.connector.connect(
                host     = __host, 
                database = __database, 
                user     = __user_name, 
                password = __password
            )
            
            
        except Error as error:
            if self.connection.is_connected():
                self.connection.close()
                
            print("Unable to connect to MySQL", error)
            print("Connection to MySQL closed")

    def __enter__(self):
        return self
            
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

