# -*- coding: utf-8 -*-
import sys
import requests
from flask import Flask, request
from pymessenger.bot import Bot
from modules.need_parameters import need_phone
from modules.sekret import VERIFY_TOKEN, PAGE_ACCESS_TOKEN, \
    URL_MESSENGER_PROFILE
from modules.sendMessageButton import decide_button

app = Flask(__name__)
bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get("hub.mode") == "subscribe" and\
            request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook_test():
    data = request.get_json()
    log(data)
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]
                if messaging_event.get("message"):
                    message_text = messaging_event["message"]["text"]
                    print(message_text)
                    need_phone(sender_id, data)

                if messaging_event.get("postback"):
                    message = messaging_event["postback"]["payload"]
                    decide_button(sender_id, message, data)

                if messaging_event.get("delivery"):
                    pass
    setup_all()

    return "ok", 200


def setup_get_started():
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = {
        "get_started": {
            "payload": "get_started"
        }
    }
    r = requests.post(URL_MESSENGER_PROFILE,
                      params=params, json=data)
    print(r)


def setup_greeting():
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = {
            "greeting": [
                {
                    "locale": "default",
                    "text": "Вас приветствует Facebook-бот\
                                для вызова NambaTaxi!\n"
                            "Вызовите команду Get Started"
                }
            ]
    }
    r = requests.post(URL_MESSENGER_PROFILE,
                      params=params, json=data)
    print(r)


def setup_all():
    setup_get_started()
    setup_greeting()


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
