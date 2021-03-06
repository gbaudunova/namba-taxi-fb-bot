from chat.handlers.handlers_order import create_order
from chat.keyboard import get_order_keyboard
from chat.keyboard import save_phone
from chat.keyboard import send_button_message
from chat.messages import BOT_PHONE_START_996, BOT_ORDER_CREATED, \
    BOT_ERROR_MESSAGE
from modules.sekret import PAGE_ACCESS_TOKEN
from storage.db import insert_address, insert_phone_numbers,\
    insert_data_creation_order
from storage.get_data import get_order_id
from config.db_config import db_conf


def need_phone(sender_id, data):
    data_order_id = get_order_id(db_conf['name'])
    order_id = data_order_id[1]
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    try:
        integer = int(message_id)
        print(integer)
        a = message_id.rfind('')
        if message_id[0:4] != "+996":
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_PHONE_START_996)
        elif message_id[0:4] == "+996" and a == 13:
            save_phone(sender_id)
            insert_phone_numbers(data, db_conf['name'])
        else:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_ERROR_MESSAGE)
    except ValueError:
        need_address(sender_id, data, order_id)


def need_address(sender_id, data, order_id):
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    if message_id == " ":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ERROR_MESSAGE)
    elif message_id == len(message_id) < 3 or len(message_id) > 150:
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ERROR_MESSAGE)
    else:
        insert_address(data, db_conf['name'])
        create_order()

        insert_data_creation_order(db_conf['name'])
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ORDER_CREATED.format(order_id))
        get_order_keyboard(sender_id)
