import os
from database.database import DatabaseConnection
from flask import Flask, render_template, render_template_string, request, Blueprint
from config import DevelopmentConfig


app = Flask(__name__, template_folder="templates")
app.secret_key = DevelopmentConfig.SECRET_KEY


#
# Methode voor het ophalen van de index pagina
#
@app.route("/", methods=["GET"])
def index():
    return render_template("home.html")


#
# Methode om de 
#
@app.route("/noun", methods=["POST", "GET"])
def noun_results():
    return render_template("noun.html")


#
# Methode vraagwoorden toe te voegen
#
@app.route('/question', methods=['GET'])
def question_results():
    return render_template("question.html");


#
# Methode om de voegwoorden pagina op te halen
#
@app.route('/conjuction', methods=['GET'])
def conjuction_results():
    return render_template("conjuction.html")


#
# Methode
#
if __name__ == '__main__':
    app.run()