import requests
import sqlite3
from flask import Flask
from modules.sekret import *
from modules.get_data import get_data
from .order_status import get_order_status


app = Flask(__name__)


@app.route('/v1/drivers/nearest', methods=['POST'])
def get_nearest_drivers():
    data = get_data()
    address = data[2][1]
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "address": address

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    resp = requests.post("https://partners.staging.swift.kg/api/v1/drivers/nearest", data=body, headers=headers).json()
    print(resp)


@app.route('/v1/requests/{id}/cancel/')
def cancel_order(order_id):
    url = "https://partners.staging.swift.kg/api/v1/requests/{0}/cancel/".format(order_id)
    print(url)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(url, data=body, headers=headers).json()
    print(responce)


@app.route('/v1/requests/', methods=['POST'])
def create_order():
    data = get_data()
    phone_number = data[0][1]
    fare = data[1][1]
    address = data[2][1]
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,
        "phone_number": phone_number,
        "fare": fare,
        "address": address

    }
    headers = {'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post("https://partners.staging.swift.kg/api/v1/requests/", data=body, headers=headers).json()
    order_id = responce['order_id']
    print(order_id)
    insert_order_id(order_id)
    get_order_status(order_id)
    cancel_order(order_id)
    get_nearest_drivers()
    return order_id


def insert_order_id(order_id):
    db3 = sqlite3.connect('NambaTaxiBot.db')
    conn2 = db3.cursor()
    conn2.execute("INSERT INTO order_id VALUES (NULL , ?)", (order_id,))
    db3.commit()















