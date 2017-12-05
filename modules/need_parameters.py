from .messages import *
from .sekret import *
from .db import insert_address, insert_phone_numbers
from api.requests import create_order
from .keyboard import get_order_keyboard
from .keyboard import save_phone
from .keyboard import send_button_message
from .messages import BOT_ERROR_MESSAGE


def need_phone(sender_id, data):
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    try:
        integer = int(message_id)
        a = message_id.rfind('')
        if message_id[0:4] != "+996":
            send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_PHONE_START_996)
        elif message_id[0:4] == "+996" and a == 13:
            save_phone(sender_id)
            insert_phone_numbers(data)
        else:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ERROR_MESSAGE)
    except ValueError:
        need_address(sender_id, data)


def need_address(sender_id, data):
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    if message_id == " ":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ERROR_MESSAGE)
    elif message_id == len(message_id) < 3 or len(message_id) > 150:
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ERROR_MESSAGE)
    else:
        insert_address(data)
        create_order()
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ORDER_CREATED)
        get_order_keyboard(sender_id)




















