import requests
import threading
from flask import Flask
from modules.sekret import PARTNER_ID,\
    SERVER_TOKEN, URL_ORDER_STATUS


app = Flask(__name__)


@app.route('/v1/requests/{id}/', methods=['POST'])
def get_order_status(order_id):
    threading.Timer(20.0, get_order_status, [order_id]).start()
    url = URL_ORDER_STATUS.format(order_id)
    print(url)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,

    }
    headers = {'accept': 'application/json',
               'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(url, data=body, headers=headers).json()
    print(responce)
    driver_data = responce['driver']
    print(driver_data)
    order_status = responce['status']
    print(order_status)
    trip_cost = responce['trip_cost']
    print(trip_cost)
    return order_status
