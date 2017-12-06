from .sekret import *
from .messages import *
from .keyboard import get_basic_keyboard_message
from .keyboard import create_keyboard_fares
from .db import insert_fares
from .keyboard import send_button_message


def decide_button(sender_id, message, data):
    if message == "call-taxi":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_PHONE)
    elif message == 'rates':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_FARE_INFO)
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_FARES_LINK)
    elif message == 'get_started':
        get_basic_keyboard_message(sender_id)
    elif message == 'save-phone':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_FARE)
        create_keyboard_fares(sender_id)
    elif message == 'order-status':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_MESSAGE_MY_ORDER_STATUS)
    elif message == 'nearest-drivers':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_MESSAGE_NEAREST_CARS)
    elif message == 'order-cancel':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ORDER_CANCEL)
    else:
        callback = data['entry'][0]['messaging'][0]['postback']['payload']
        insert_fares(data)
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_ADDRESS)





