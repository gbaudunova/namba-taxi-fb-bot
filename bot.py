import sys
import json
import logging
import requests
from flask import Flask, request
from pymessenger.bot import Bot
# from modules.messages import *
from modules.sekret import *
from modules.needPhone import *
from modules.sendMessageButton import *
from modules.start import send_button_start_message




app = Flask(__name__)
bot = Bot(PAGE_ACCESS_TOKEN)
# logger = logging.getLogger(__name__)
# logger.addHandler(logging.NullHandler())


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
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
                recipient_id = messaging_event["recipient"]["id"]
                if messaging_event.get("message"):
                    message_text = messaging_event["message"]["text"]
                    needPhone(sender_id, message_text, data)


                if messaging_event.get("postback"):
                    # sender_id = messaging_event["sender"]["id"]
                    message = messaging_event["postback"]["payload"]
                    decide_message(sender_id, message, data)


    setup_all()

    return "ok", 200


def setup_getStarted():
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = {
        "get_started": {
            "payload": "getstarted"
        }
    }
    r = requests.post("https://graph.facebook.com/v2.10/me/messenger_profile", params=params, json=data)


def setup_greeting():
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = {
        "greeting": [
    {
        "locale": "default",
        "text": "Вас приветствует Facebook-бот для вызова NambaTaxi!\n"
                "Вызовите команду Get Started"
    }
        ]
    }
    r = requests.post("https://graph.facebook.com/v2.10/me/messenger_profile", params=params, json=data)


def setup_all():
    setup_getStarted()
    setup_greeting()


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=8000)

