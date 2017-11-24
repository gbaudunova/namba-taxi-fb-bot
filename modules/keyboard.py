import json
import requests
from .messages import *
from .sekret import *


def getBasicKeyboardMessage(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": BOT_WELCOME_MESSAGE,
                    "buttons": [
                    {
                        "type": "postback",
                        "title": "Быстрый вызов такси",
                        "payload": "call-taxi"
                    },
                    {
                        "type": "postback",
                        "title": "Тарифы",
                        "payload": "rates"
                    }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    r = requests.post(URL, data=data, params=params, headers=headers)
    # if r.status_code != 200:
    #     log(r.status_code)
    #     log(r.text)


def GetOrderKeyboard(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": BOT_ORDER_BUTTON_MESSAGE,
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Узнать статус заказа",
                            "payload": "order-status"
                        },
                        {
                            "type": "postback",
                            "title": "Машины рядом",
                            "payload": "nearest-drivers"
                        },
                        {
                            "type": "postback",
                            "title": "Отменить заказ",
                            "payload": "order-cancel"
                        }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    r = requests.post(URL, data=data, params=params, headers=headers)





