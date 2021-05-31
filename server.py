import os
from re import template
from database.database import DatabaseConnection
from flask import Flask, render_template, render_template_string, request, Blueprint
from config import DevelopmentConfig
from google.ads.googleads.client import GoogleAdsClient
# from google.ads.googleads.error import GoogleAdsException
from google.api_core import protobuf_helpers
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
    return render_template("home.html")


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

    return render_template("noun.html", words=results)

    return render_template("noun.html")


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


#
# Methode
#
if __name__ == '__main__':
    app.run(debug=DevelopmentConfig.DEBUG)