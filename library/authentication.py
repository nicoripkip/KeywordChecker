from flask import session


#
# Object authenticatie
#
class Authentication(object):
    #
    # Constructor
    #
    def __init__(self):
        pass


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


Authentication.register = staticmethod(Authentication.register)
# Authentication.middleware = staticmethod(Authentication.middleware)
