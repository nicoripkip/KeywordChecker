from sqlalchemy import create_engine
from sqlalchemy.sql.expression import table

#
# Class Database
#
class DatabaseConnection(object):
    #
    # Constructor
    #
    def __init__(self, host, schema, username, password):
        self.host = host
        self.schema = schema
        self.username = username
        self.password = password
        self.engine = None
        self.query = ""
        self.table_name = ""

    
    #
    # Methode voor het maken van de verbinding
    #
    def connect_database(self):
        self.engine = create_engine("mysql://")


    #
    # Methode voor het sluiten van de database
    #
    def close_database(self):
        pass


    #
    # Methode voor het zetten van de tabelnaam
    #
    def table(self, tablename):
        self.table_name = tablename


    #
    # Methode voor het ophalen van gegevens
    #
    def get(self, params=[]):
        self.query = "SELECT * FROM " + self.table_name
        
        if params != []:
            self.query.replace("*", ", ".join(params), 1)


    #
    # Methode voor het toevoegen van de gegevens
    #
    def insert(self, params):
        self.query = "INSERT INTO " + self.table_name
        
        print(", ".join("{} : {}".format(key, value) for key, value in params.items()))

        if params != {}:
            self.query += ""
        else:
            raise Exception("Geen data gevonden")


    #
    # Methode voor het updaten van de data in de database
    #
    def update(self, params=[]):
        pass


    #
    # Methode voor het deleten van data uit de database
    #
    def delete(self):
        self.query = "DELETE * FROM " + self.table_name


    #
    # Methode voor het uitvoeren van de query
    #
    def execute(self):
        with self.engine.connect() as connection:
            connection.execute(self.query)


#
# Registratie van verschillende static functies
#
DatabaseConnection.execute = staticmethod(DatabaseConnection.execute)
DatabaseConnection.table = staticmethod(DatabaseConnection.table)
DatabaseConnection.get = staticmethod(DatabaseConnection.get)
DatabaseConnection.insert = staticmethod(DatabaseConnection.insert)
DatabaseConnection.update = staticmethod(DatabaseConnection.update)
DatabaseConnection.delete = staticmethod(DatabaseConnection.delete)