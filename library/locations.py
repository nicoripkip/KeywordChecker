import os


#
# Object locatie
#
class Locations(object):
    #
    # Constructor
    #
    def __init__(self):
        self.lang = ""


    #
    # Krijg aparaat land
    #
    def get_system_lang(self):
        self.lang = os.getenv('LANG')