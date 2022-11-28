
from flask import Flask, request, jsonify
from model import db, connect_db, EURData, GBPData, USDData
import requests
from datetime import datetime
from threading import Timer
import os
import psycopg2


app = Flask(__name__)

uri = os.environ.get('DATABASE_URL', 'postgresql:///bc_converter')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')


connect_db(app)
with app.app_context():
    db.create_all()

API_BASE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


"""Every 30 seconds, call API to get latest conversion data & add to DB"""
def getAndMapData():
    date = datetime.now()
    resp = requests.get(API_BASE_URL)

    latest_eur_rate = EURData(
        xValueRate = resp.json()["bpi"]["EUR"]["rate_float"],
        apiTimestamp = resp.json()["time"]["updated"],
        yValueTime = date)
        
    latest_usd_rate = USDData(
        xValueRate = resp.json()["bpi"]["USD"]["rate_float"],
        apiTimestamp = resp.json()["time"]["updated"],
        yValueTime = date)

    latest_gbp_rate = GBPData(
        xValueRate = resp.json()["bpi"]["GBP"]["rate_float"],
        apiTimestamp = resp.json()["time"]["updated"],
        yValueTime = date)

    with app.app_context():
        db.session.add(latest_eur_rate)
        db.session.add(latest_gbp_rate)
        db.session.add(latest_usd_rate)
        db.session.commit()

Timer(30.0, getAndMapData).start()



@app.route('/history/eur/<qty>', methods=["GET"])
def returnDataEUR(qty):
    eurDataArr = [EURData.serialize(obj) for obj in EURData.query.order_by(EURData.yValueTime.desc()).limit(qty).all()]

    return jsonify(eurDataArr)


@app.route('/history/usd/<qty>', methods=["GET"])
def returnDataUSD(qty):
    usdDataArr = [USDData.serialize(obj) for obj in USDData.query.order_by(USDData.yValueTime.desc()).limit(qty).all()]

    return jsonify(usdDataArr)


@app.route('/history/gbp/<qty>', methods=["GET"])
def returnDataGBP(qty):
    gbpDataArr = [GBPData.serialize(obj) for obj in GBPData.query.order_by(GBPData.yValueTime.desc()).limit(qty).all()]

    return jsonify(gbpDataArr)



