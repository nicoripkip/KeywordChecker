from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import BLOB
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import Text



#
# Subscriptie model
# 
class Subscription(object):
    #
    # Constructor
    #
    def __init__(self, table):
        self.table_name = table
        self.metadata = MetaData()


    #
    # Construct table
    #
    def table(self):
        return Table(
            self.table_name,
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(255)),
            Column('description', Text, nullable=True),
            Column('image', BLOB, nullable=True),
            Column('value', Float),
            Column('startdate', Date),
            Column('enddate', Date),
            Column('payment', Integer, nullable=False)
        )