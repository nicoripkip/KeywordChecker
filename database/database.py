from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.schema import Column


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
        self.query = Null
        self.table_name = ""

    
    #
    # Methode voor het maken van de verbinding
    #
    def connect_database(self):
        return create_engine("mysql+pymysql://niko:henkdepotvis@127.0.0.1/keywordchecker?charset=utf8mb4")


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
        self.query = select(self.table_name)
        
        if params != []:
            self.query.replace("*", ", ".join(params), 1)


    def where(self, param1, param2):
        self.query.where(param1 == param2)

        print(self.query)


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
        connection = self.connect_database()
        return connection.execute(self.query).fetchall()