import requests
from flask import Flask
from modules.get_data import get_address
from modules.sekret import *

app = Flask(__name__)


@app.route('/v1/drivers/nearest/', methods=['POST'])
def get_nearest_drivers():
    data_address = get_address()
    address = data_address[1]
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "address": address
    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    resp = requests.post("https://partners.staging.swift.kg/api/v1/drivers/nearest/", data=body, headers=headers).json()
    nearest_cars = resp['drivers']
    return nearest_cars