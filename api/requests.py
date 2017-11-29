import requests
from flask import Flask
from modules.sekret import *

app = Flask(__name__)


@app.route('/v1/requests/', methods=['POST'])
def create_order(phone_number, fare, address):
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "phone_number": phone_number,
        "fare": fare,
        "address": address

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post("https://partners.staging.swift.kg/api/v1/requests/", data=body, headers=headers)
    print(responce.content)


