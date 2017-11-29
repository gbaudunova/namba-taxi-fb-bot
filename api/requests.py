import sys
import requests
import json
from flask import Flask, request
from modules.sekret import *
#from modules.get_data import get_data

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
    # data = json.loads(responce.json())
    # print(data)
    # value = request.get_json()
    # print(value)


@app.route('/v1/requests/{id}/', methods=['POST'])
def get_order_status():
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post("https://partners.staging.swift.kg/api/v1/requests/{id}/", data=body, headers=headers)
    print(responce.content)









