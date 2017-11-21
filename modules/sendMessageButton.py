import json
import requests
from bot import log
from .messages import *
from .sekret import *
from .start import send_button_start_message
from .needPhone import *


def decide_message(sender_id, message):
    if(message == "call-taxi"):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_PHONE)
    elif(message == 'rates'):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_BUTTON_MESSAGE2)
    elif(message == 'getstarted'):
        send_button_start_message(sender_id)
    elif(message == 'send-phone'):
        #send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_FARE)
        sendFares(sender_id)
    else:
        print('Get Started')


def send_button_message(sender_id, page_token, btn_message):
    # log("sending message to {recipient}: {text}".format(recipient=sender_id, text=""))
    params = {
        "access_token": page_token
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": btn_message

        }
    })
    r = requests.post(URL, params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def sendFares(sender_id):
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
                    "text": "Выберите тариф",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Стандарт",
                            "payload": "standard-fare"
                        },
                        {
                            "type": "postback",
                            "title": "Минивэн",
                            "payload": "minivan-fare"
                        },
                        {
                            "type": "postback",
                            "title": "Комфорт",
                            "payload": "comfort-fare"
                        },
                        {
                            "type": "postback",
                            "title": "Байк+",
                            "payload": "bike-fare"
                        },
                        {
                            "type": "postback",
                            "title": "Портер",
                            "payload": "porter-fare"
                        }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    r = requests.post(URL, data=data, params=params, headers=headers)

