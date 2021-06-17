from flask import session
from sqlalchemy.sql.sqltypes import Numeric
from werkzeug.utils import redirect


#
# Object authenticatie
#
class Authentication(object):
    #
    # Constructor
    #
    def __init__(self):
        self.redirect = 0


    #
    # Register session vars
    #
    def register(self):
        if "username" not in session and "password" not in session and "login_key" not in session:
            session["username"] = ""
            session["password"] = ""
            session["login_key"] = ""


    #
    # Check voor login
    #
    @staticmethod
    def middleware(self) -> bool:
        if session["username"] and session["password"] and session["login_key"]:
            return True

        return False

    
    #
    # Methode om de redirect te zetten
    #
    def set_redirect(self, value):
        self.redirect = self.redirect + value


    #
    # Methode om de redirect count te stoppen
    #
    def reset_redirect(self):
        self.redirect = 0


    #
    # Methode om de redirect op te halen
    #
    # @staticmethod
    def get_redirect(self) -> int:
        return self.redirect


Authentication.register = staticmethod(Authentication.register)
# Authentication.middleware = staticmethod(Authentication.middleware)