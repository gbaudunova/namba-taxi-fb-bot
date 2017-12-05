import requests
from flask import Flask
from modules.sekret import *
from modules.get_data import get_data


app = Flask(__name__)


@app.route('/v1/requests/', methods=['POST'])
def create_order():
    a = get_data()
    phone_number = a[0][1]
    print(phone_number)
    fare = a[1][1]
    print(fare)
    address = a[2][1]
    print(address)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "phone_number": phone_number,
        "fare": fare,
        "address": address

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post("https://partners.staging.swift.kg/api/v1/requests/", data=body, headers=headers).json()
    print(responce['order_id'])












