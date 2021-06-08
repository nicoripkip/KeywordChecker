from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text


#
# Rechten model
#
class Roles(object):
    #
    # constructor
    #
    def __init__(self, table):
        self.table_name = table
        self.metadata = MetaData()


    #
    # Construct de table
    #
    def table(self):
        return Table(
            self.table_name,
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(255)),
            Column('description', Text)
        )