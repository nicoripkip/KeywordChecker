from http.client import responses
import os
from re import template
from sqlalchemy.sql.ddl import CreateColumn
from werkzeug.wrappers import response
from werkzeug.wrappers.response import Response
from library.client import RestClient
from werkzeug.utils import redirect
from database.database import DatabaseConnection
from flask import Flask, render_template, render_template_string, request, Blueprint, session
from config import DevelopmentConfig
from google.ads.googleads.client import GoogleAdsClient
from database.models.user_model import User
from google.api_core import protobuf_helpers
from library.authentication import Authentication
import uuid
client = GoogleAdsClient.load_from_storage("./google-ads.yaml");



app = Flask(__name__, template_folder="templates")
app.secret_key = DevelopmentConfig.SECRET_KEY
GOOGLE_ADS_SERVICE = "GoogleAdsService"
_DEFAULT_PAGE_SIZE = 1000


#
# Credentials api
#
CRED_USERNAME = "nikovanommen.nvo@gmail.com"
CRED_PASSWORD = "ac6b5942fae1ce72"


#
# Methode voor het ophalen van de index pagina
#
@app.route("/", methods=["GET"])
def index(): 
    Authentication.register

    languages = get_online_data(
        "/v3/keywords_data/google/languages",
        {
            0: CRED_USERNAME,
            1: CRED_PASSWORD
        }
    )

    languages = languages["tasks"][0]["result"]

    username = ""

    if "username" in session:
        username = session['username']

    return render_template("home.html", username=username, languages=languages)


#
# Methode om de 
#
@app.route("/noun", methods=["POST", "GET"])
def noun_results():
    from flask import request

    if request.method == "GET":
        post_online_data(
            "/v3/keywords_data/google/keywords_for_keywords/task_post",
            {
                0: CRED_USERNAME,
                1: CRED_PASSWORD
            },
            [
                dict(
                    language_code=request.form.get("language"),
                    location_code=2840,
                    keywords=[
                        request.form.get("search")
                    ],
                    pingback_url="http://127.0.0.1:5000/noun"
                ),
            ]
        )

        words = get_many_online_data(
            "/v3/keywords_data/google/keywords_for_keywords/tasks_ready",
            {
                0: CRED_USERNAME,
                1: CRED_PASSWORD
            }
        )

        words = words[0]["tasks"][0]["result"]
    else:
        words = []

    username = ""

    if "username" in session:
        username = session["username"]

    return render_template("noun.html", words=words, username=username)


#
# Methode vraagwoorden toe te voegen
#
@app.route('/question', methods=['GET', 'POST'])
def question_results():

    if request.method == "GET":
        words = get_many_online_data(
            "/v3/keywords_data/google/keywords_for_keywords/tasks_ready",
            {
                0: CRED_USERNAME,
                1: CRED_PASSWORD
            }
        )

        words = words[0]["tasks"][0]["result"]
    else:
        words = []

    if "username" in session:
        username = session["username"]

    return render_template("question.html", words=words, username=username);


#
# Methode om de voegwoorden pagina op te halen
#
@app.route('/conjuction', methods=['GET', 'POST'])
def conjuction_results():
    if request.method == "GET":
        words = get_many_online_data(
            "/v3/keywords_data/google/keywords_for_keywords/tasks_ready",
            {
                0: CRED_USERNAME,
                1: CRED_PASSWORD
            }
        )

        words = words[0]["tasks"][0]["result"]
    else:
        words = []
    
    if "username" in session:
        username = session["username"]

    return render_template("conjuction.html")


#
# Methode om de zoek volume pagina op te halen
#
@app.route('/volumes', methods=['GET'])
def search_volume():
    pass


#
#
#
@app.route('/login', methods=["GET"])
def login():
    username = ""

    if "username" in session:
        username = session['username']
        return redirect("/")
    
    return render_template("login.html", username=username)


#
#
#
@app.route('/login_check', methods=["POST"])
def login_check():
    if request.form.get("username") != "" and request.form.get("password") != "":
        willem = User("users")
        user = willem.table()

        connection = DatabaseConnection("127.0.0.1", "keywordchecker", "nikoripkip", "henkdepotvis")
        connection.table(user)
        connection.get()
        connection.where(user.c.username, request.form.get("username"))
        connection.where(user.c.password, request.form.get("password"))
        results = connection.execute()

        if len(results) > 0:
            session['username'] = results[0][1]
            session['password'] = results[0][2]
            session['login_key'] = uuid.uuid4()

            return redirect("/")
        
    return redirect('/login')


#
#
#
@app.route('/logout', methods=["get"])
def logout():
    del session['username']
    del session['password']
    del session['login_key']        

    return redirect("/")


#
# Methode voor het ophalen van online data
#
def get_online_data(url, credentials, payload=dict()):
    client = RestClient(credentials[0], credentials[1])
    response = client.get(url)

    if response["status_code"] == 20000:
        return response

    raise Exception("Er is geen data opgehaald")


#
# Methode wanneer er meerdere taken gedaan moeten worden
#
def get_many_online_data(url, credentials, payload=dict()):
    client = RestClient(credentials[0], credentials[1])
    response = client.get(url)

    if response["status_code"] == 20000:
        result = []

        for x in response["tasks"]:
            if x["result"] and len(x["result"]) > 0:
                for y in x["result"]:
                    print(y)

                    result.append(client.get(y["endpoint"]))            
    
        return result
    
    raise Exception("Er is geen data opgehaalt")


#
# Methode om data naar de api te werken
# 
def post_online_data(url, credentials, payload=dict()):
    client = RestClient(credentials[0], credentials[1])
    response = client.post(url, payload)

    if response["status_code"] == 20000:
        return response

    raise Exception("Data is niet naar de api verzonden: %s", (response["status_code"], response["status_message"]))


#
# Methode
#
if __name__ == '__main__':
    app.run(debug=DevelopmentConfig.DEBUG)
