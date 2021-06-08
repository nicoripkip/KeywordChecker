from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BLOB
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey


#
# Gebruikers model
#
class User(object):
    def __init__(self, table):
        self.table_name = table
        self.metadata = MetaData();


    def table(self):
        return Table(
            self.table_name, 
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('username', String(255)),
            Column('password', String(255)),
            Column('email', String(255)),
            Column('email_verified_at', Boolean),
            Column('image', BLOB, nullable=True),
            Column('role_id', ForeignKey('roles.id'), nullable=False),
            Column('subscription_id', ForeignKey('subscription.id'), nullable=False)
        )