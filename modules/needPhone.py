from .messages import BOT_PHONE_START_996, BOT_ASK_FARE
from .sendMesaageButton import send_button_message
from .sekret import *


def needPhone(sender_id, message_text, data):
    message_id = data['entry'][0]['messaging'][0]['message']['text'][0]
    if message_id != "+":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_PHONE_START_996)
    elif message_id == "+":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_FARE)
    else:
        print("Error")