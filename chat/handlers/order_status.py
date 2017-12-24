import requests
import time
from flask import Flask
from modules.sekret import PARTNER_ID,\
    SERVER_TOKEN, URL_ORDER_STATUS, PAGE_ACCESS_TOKEN
from chat.messages import BOT_ORDER_ACCEPTED, BOT_DRIVER_LOCATION, \
    BOT_CLIENT_BORT, BOT_DRIVER_IN_PLACE, BOT_ORDER_DONE, \
    BOT_MESSAGE_MY_ORDER_STATUS, BOT_ORDER_CANCEL, BOT_NO_ORDER
from chat.keyboard import send_button_message


app = Flask(__name__)


@app.route('/v1/requests/{id}/', methods=['POST'])
def get_order_status(order_id):
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
    return trip_cost, order_status, driver_data


def order_status_reaction(order_id, sender_id):
    order_status = 'Новый заказ'
    while True:
        status_func = get_order_status(order_id)
        time.sleep(5)
        print(status_func[1])
        trip_cost = status_func[0]
        current_status = status_func[1]
        driver_data = status_func[2]
        if current_status == order_status:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_MESSAGE_MY_ORDER_STATUS)
        else:
            if current_status == 'Отклонен':
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_ORDER_CANCEL)
            elif current_status == 'Принят':
                driver_number = driver_data['phone_number']
                cab_number = driver_data['cab_number']
                name_driver = driver_data['name']
                car = driver_data['make']
                license_plate = driver_data['license_plate']
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_ORDER_ACCEPTED.format(cab_number,
                                                              name_driver,
                                                              driver_number,
                                                              license_plate,
                                                              car))
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_DRIVER_LOCATION)

            elif current_status == 'Машина на месте':
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_DRIVER_IN_PLACE)
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_DRIVER_LOCATION)
            elif current_status == 'Клиент на борту':
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_CLIENT_BORT)
            elif current_status == 'Выполнен':
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_ORDER_DONE.format(trip_cost))
            else:
                send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                    BOT_NO_ORDER)
