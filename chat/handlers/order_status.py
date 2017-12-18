import requests
import threading
from flask import Flask
from modules.sekret import PARTNER_ID,\
    SERVER_TOKEN, URL_ORDER_STATUS, PAGE_ACCESS_TOKEN
from chat.messages import BOT_ORDER_ACCEPTED, BOT_DRIVER_LOCATION, \
    BOT_CLIENT_BORT, BOT_DRIVER_IN_PLACE, BOT_ORDER_DONE, \
    BOT_MESSAGE_MY_ORDER_STATUS, BOT_ORDER_CANCEL, BOT_NO_ORDER
from chat.keyboard import send_button_message


app = Flask(__name__)


@app.route('/v1/requests/{id}/', methods=['POST'])
def get_order_status(sender_id, order_id):
    timer = threading.Timer(30.0, get_order_status, [sender_id, order_id])
    timer.start()
    url = URL_ORDER_STATUS.format(order_id)
    print(url)
    body = {
        "server_token": SERVER_TOKEN,
        "partner_id": PARTNER_ID,

    }
    headers = {'accept': 'application/json',
               'content-type': 'application/x-www-form-urlencoded'}
    responce = requests.post(url, data=body, headers=headers).json()
    driver_data = responce['driver']
    order_status = responce['status']
    trip_cost = responce['trip_cost']
    order_status_reaction(sender_id, order_status, trip_cost, driver_data)
    return trip_cost, order_status, driver_data


def order_status_reaction(sender_id, order_status, trip_cost, driver_data):
    driver_phone_number = driver_data['phone_number']
    cab_number = driver_data['cab_number']
    name_driver = driver_data['name']
    car = driver_data['make']
    license_plate = driver_data['license_plate']
    lon = driver_data['lon']
    lat = driver_data['lat']
    print(lat, lon)
    if order_status == 'Новый заказ':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_MESSAGE_MY_ORDER_STATUS)
    elif order_status == 'Отклонен':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ORDER_CANCEL)
    elif order_status == 'Принят':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ORDER_ACCEPTED.format(cab_number,
                                                      name_driver,
                                                      driver_phone_number,
                                                      license_plate,
                                                      car))
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_DRIVER_LOCATION)

    elif order_status == 'Машина на месте':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_DRIVER_IN_PLACE)
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_DRIVER_LOCATION)
    elif order_status == 'Клиент на борту':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_CLIENT_BORT)
    elif order_status == 'Выполнен':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ORDER_DONE.format(trip_cost))
    else:
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_NO_ORDER)
