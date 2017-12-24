import requests
from flask import Flask
from modules.sekret import SERVER_TOKEN, PARTNER_ID
from storage.get_data import get_address
from config.db_config import db_conf

app = Flask(__name__)


@app.route('/v1/drivers/nearest/', methods=['POST'])
def get_nearest_drivers():
    data_address = get_address(db_conf['name'])
    address = data_address[1]
    url = "https://partners.staging.swift.kg/api/v1/drivers/nearest/"
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "address": address
    }
    headers = {'accept': 'application/json',
               'content-type': 'application/x-www-form-urlencoded'}
    resp = requests.post(url,
                         data=body, headers=headers).json()
    print(resp)
    nearest_cars = resp['drivers']
    return nearest_cars
