import requests
import json
from .messages import *
from .sendMessageButton import send_button_message
from .sekret import *
from .db import *
from .handlers import CreateOrder


def needPhone(sender_id, message_text, data):
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    try:
        integer = int(message_id)
        a = message_id.rfind('')
        if message_id[0:4] != "+996":
            send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_PHONE_START_996)
        elif message_id[0:4] == "+996" and a == 13:
            savePhone(sender_id)
            insertPhoneNumbers(data)

        else:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ERROR_JUST_NUMBER)

    except ValueError:
        address = data['entry'][0]['messaging'][0]['message']['text']
        insertAddress(data)
        CreateOrder()
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ORDER_CREATED)


def savePhone(sender_id):
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Нажмите на кнопку для сохранения вашего номера",
                    "buttons": [
                    {
                        "type": "postback",
                        "title": "Сохранить номер телефона",
                        "payload": "send-phone"
                    },
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    r = requests.post(URL, data=data, params=params, headers=headers)

