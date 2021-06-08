import os
from re import template

from werkzeug.utils import redirect
from database.database import DatabaseConnection
from flask import Flask, render_template, render_template_string, request, Blueprint, session
from config import DevelopmentConfig
from google.ads.googleads.client import GoogleAdsClient
# from google.ads.googleads.error import GoogleAdsException
from database.models.user_model import User
from google.api_core import protobuf_helpers
from flask import sessions
client = GoogleAdsClient.load_from_storage("./google-ads.yaml");



app = Flask(__name__, template_folder="templates")
app.secret_key = DevelopmentConfig.SECRET_KEY
GOOGLE_ADS_SERVICE = "GoogleAdsService"
_DEFAULT_PAGE_SIZE = 1000


#
# Methode voor het ophalen van de index pagina
#
@app.route("/", methods=["GET"])
def index():
    service = client.get_service("GoogleAdsService")
 
    print(service)

    username = ""

    if session['username'] != "":
        username = session['username']

    return render_template("home.html", username=username)


#
# Methode om de 
#
@app.route("/noun", methods=["POST", "GET"])
def noun_results():
    from flask import request

    # if request.method == "post":
    service = client.get_service(GOOGLE_ADS_SERVICE)

    if request.form.get("search") == "":
        raise Exception("Geen sleutelwoord ingevoerd!")

    api_query = """SELECT 
                        ad_group.id, 
                        ad_group_criterion.type, 
                        ad_group_criterion.criterion_id, 
                        ad_group_criterion.keyword.text, 
                        ad_group_criterion.keyword.match_type
                    FROM ad_group_criterion
                    WHERE ad_group_criterion.type = """ + request.form.get("search")
    
    request = client.get_type("SearchGoogleAdsRequest")
    request.query = api_query
    request.page_size = _DEFAULT_PAGE_SIZE

    results = service.search(request=request)

    username = ""

    if session['username'] != "":
        username = session['username']

    return render_template("noun.html", words=results, username=username)


#
# Methode vraagwoorden toe te voegen
#
@app.route('/question', methods=['GET', 'POST'])
def question_results():
    return render_template("question.html");


#
# Methode om de voegwoorden pagina op te halen
#
@app.route('/conjuction', methods=['GET', 'POST'])
def conjuction_results():
    if request.method == "POST":
        return render_template("conjuction.html")

    return render_template("conjuction.html")


#
# Methode om de zoek volume pagina op te halen
#
@app.route('/volumes', methods=['GET'])
def search_volume():
    pass


@app.route('/login', methods=["GET"])
def login():
    username = ""

    if session['username'] != "":
        username = session['username']
        return redirect("/")
    
    return render_template("login.html", username=username)


@app.route('/login_check', methods=["POST"])
def login_check():
    if request.form.get("username") != "" and request.form.get("password") != "":
        willem = User("users")
        user = willem.table()

        connection = DatabaseConnection("127.0.0.1", "keywordchecker", "nikoripkip", "henkdepotvis")
        connection.table(user)
        connection.where(user.c.password, request.form.get("password"))
        results = connection.execute()

        if len(results) > 0:
            session['username'] = results[0][1]
            session['password'] = results[0][2]

            return redirect("/")
        
    return redirect('/login')


@app.route('/logout', methods=["get"])
def logout():
    session['username'] = ""
    session['password'] = ""

    return redirect("/")


#
# Methode
#
if __name__ == '__main__':
    app.run(debug=DevelopmentConfig.DEBUG)