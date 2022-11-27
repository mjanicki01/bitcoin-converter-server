
from flask import Flask, request, jsonify
from model import db, connect_db, EURData, GBPData, USDData
import requests


API_BASE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

app = Flask(__name__)

connect_db(app)
db.create_all()


"""Call API to get refreshed JSON object every 30 seconds"""
def importData():
    resp = requests.get(API_BASE_URL)
    print(resp)


@app.route('/update', methods=["POST"])
def updateData():
    resp = jsonify(requests.post(API_BASE_URL))
    return resp


@app.route('/history', methods=["GET"])
def returnData():
    resp = requests.get(API_BASE_URL)
    return resp



