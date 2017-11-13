# import os
import sys
import logging
from flask import Flask, request
from pymessenger.bot import Bot
# from pymessenger import Button
import requests
import json


PAGE_ACCESS_TOKEN = ''
GRAPH_URL = ''
VERIFY_TOKEN = ''

app = Flask(__name__)
bot = Bot(PAGE_ACCESS_TOKEN)
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


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

    if data["object"] == "page":
        for entry in data["entry"]:

            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]

                    send_button_start_message(sender_id)
                if messaging_event.get("delivery"):
                    pass

                if messaging_event.get("optin"):
                    pass

                if messaging_event.get("postback"):
                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["postback"]["payload"]
                    decide_message(sender_id, message_text)

    return "ok", 200


def decide_message(sender_id, message_text):
    if(message_text == "call-taxi"):
        send_text_message(sender_id)
    elif(message_text == 'rates'):
        send_message(sender_id)
    else:
        print("Error")


def send_text_message(sender_id):

    log("sending message to {recipient}: {text}".format(recipient=sender_id, text="text1"))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": "Укажите ваш телефон. Например: +996555112233"

        }
    })
    r = requests.post("https://graph.facebook.com/v2.10/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def send_message(sender_id):
    log("sending message to {recipient}: {text}".format(recipient=sender_id,
                                                        text="Укажите ваш телефон. Например: +996555112233"))

    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": "Тариф: Стандарт. Стоимость посадки: 50.00. Стоимость за километр: 12.00.\n"
            
                    "Тариф: Минивэн. Стоимость посадки: 100.00. Стоимость за километр: 12.00.\n"
            
                    "Тариф: Комфорт. Стоимость посадки: 70.00. Стоимость за километр: 15.00.\n"
            
                    "Тариф: Байк+. Стоимость посадки: 100.00. Стоимость за километр: 10.00.\n"
            
                    "Тариф: Портер. Стоимость посадки: 500.00. Стоимость за километр: 0.00.\n"
            
                    "Для получения более подробной информации, перейдите по ссылке: https://nambataxi.kg/ru/tariffs/"

        }
    })
    r = requests.post("https://graph.facebook.com/v2.10/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def send_button_start_message(sender_id):
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params={"access_token": PAGE_ACCESS_TOKEN}, data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"attachment": {
                                    "type": "template",
                                    "payload": {
                                          "template_type": "button",
                                          "text": "Вас приветствует бот для вызова NambaTaxi!",
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
                                              },
                                          ]
                                      }
                                  }
                              }
                          }),
                    headers={'Content-type': 'application/json'})
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
