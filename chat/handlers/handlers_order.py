import sqlite3
import requests
from flask import Flask
from modules.sekret import SERVER_TOKEN, \
    PARTNER_ID, URL_CANCEL_ORDER
from storage.get_data import get_data
from config.db_config import db_conf

app = Flask(__name__)


@app.route('/v1/requests/{id}/cancel/')
def cancel_order(order_id):
    url = URL_CANCEL_ORDER.format(order_id)
    print(url)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID

    }
    headers = {'accept': 'application/json',
               'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(url, data=body, headers=headers).json()
    print(responce)


@app.route('/v1/requests/', methods=['POST'])
def create_order():
    data = get_data(db_conf['name'])
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
    headers = {'accept': 'application/json',
               'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(
        "https://partners.staging.swift.kg/api/v1/requests/",
        data=body, headers=headers).json()
    order_id = responce['order_id']
    print(order_id)
    insert_order_id(order_id, db_conf['name'])
    return order_id


def insert_order_id(order_id, db_name):
    db3 = sqlite3.connect(db_name)
    conn2 = db3.cursor()
    conn2.execute('INSERT INTO order_id VALUES (NULL , ?)', (order_id,))
    db3.commit()
