import json
import requests
from bot import log
from .messages import *
from .sekret import *
from .start import send_button_start_message


def decide_message(sender_id, message):
    if(message == "call-taxi"):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_PHONE)
    elif(message == 'rates'):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_BUTTON_MESSAGE2)
    elif(message == 'getstarted'):
        send_button_start_message(sender_id)
    elif(message == 'send-phone'):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_FARE)
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
