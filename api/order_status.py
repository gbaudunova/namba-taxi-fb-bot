import requests
from flask import Flask
from modules.sekret import *

app = Flask(__name__)


@app.route('/v1/requests/{id}/', methods=['POST'])
def get_order_status(order_id):
    url = "https://partners.staging.swift.kg/api/v1/requests/{0}/".format(order_id)
    print(url)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(url, data=body, headers=headers).json()
    print(responce)