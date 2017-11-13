import sys
import json
import logging
import sys
# from pymessenger import Button
import requests
from flask import Flask, request
from pymessenger.bot import Bot
from modules.messages import *
# from modules.sekret import *
from modules.setup import *
setup_all()

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
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_PHONE)
    elif(message_text == 'rates'):
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_BUTTON_MESSAGE2)
    else:
        print("Error")


def send_button_message(sender_id, page_token, btn_message):

    log("sending message to {recipient}: {text}".format(recipient=sender_id, text=""))

    params = {
        "access_token": page_token
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": btn_message

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




# def send_chat_message(sender_id, text):
#     buttons = [
#         {
#             'type': 'postback',
#             'title': 'New chat',
#             'payload': 'user1',
#         },
#         {
#             'type': 'postback',
#             'title': 'End chat',
#             'payload': 'user2',
#         },
#     ]
#
#     send_button_message(sender_id, text, buttons)
#
#
# def send_get_started_message(recipient_id):
#     text = 'Get started - chat with a rando'
#     buttons = [
#         {
#             'type': 'postback',
#             'title': 'Chat with a stranger',
#             'payload': 'nextuser',
#         },
#     ]
#
#     send_button_message(recipient_id, text, buttons)
#
# def send_button_message(sender_id, text, buttons):
#     message_data = {
#         'attachment': {
#             'type': 'template',
#             'payload': {
#                 'template_type': 'button',
#                 'text': text,
#                 'buttons': buttons,
#             }
#         }
#     }
#
#     send_text_message(sender_id, message_data)
# #
#
# def send_message(recipient_id, message_data):
#     params = {
#         'access_token': PAGE_ACCESS_TOKEN,
#     }
#
#     data = {
#         'recipient': {
#             'id': str(recipient_id)
#         },
#         'message': message_data,
#     }
#
#     print('message_data', message_data)
#
#     r = requests.post(GRAPH_URL, params=params, json=data)
#
#     if r.status_code != requests.codes.ok:
#         print(r, r.text)


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
