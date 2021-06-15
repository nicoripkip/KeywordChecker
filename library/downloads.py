import csv
import os
import pandas as pd
import flask_excel as excel


#
# Object voor het downloaden van stuff
#
class Downloads(object):
    #
    # Constructor
    #
    def __init__(self, type):
        self.data = None
        self.download_type = type


    #
    # Toevoeging van de dataset
    #
    def dataset(self, dataset):
        self.data = dataset


    #
    # Methode om te laten downloaden
    #
    def download(self):
        if self.download_type == "text":
            pass

        elif self.download_type == "csv":
            pass

        elif self.download_type == "excel":
            return self.convert_to_excel()

        else:
            raise Exception("Er is geen download optie gevonden!")
        


    #
    # Methode om de dataset om te zetten naar textbestand
    #
    def convert_to_text(self, head, body):
        with open('dataset.txt', 'w') as file:
            pass


    #
    # Methode om de dataset om te zetten naar excel bestand
    #
    def convert_to_excel(self):
        return excel.make_response_from_array([], "csv", file_name="dataset")


    #
    # Methode om de dataset om te zetten naar csv bestand
    #
    def convert_to_csv(self, head, body):
        with open('dataset.csv', 'w') as file:
            write = csv.writer(file)
            write.writerow(head)
            write.writerows(body)


    #
    # Methode om de dataset op te schonen
    #
    def dispose(self):
        del self.dataset