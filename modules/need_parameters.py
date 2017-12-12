from api.handlers_order import create_order
from chat.keyboard import get_order_keyboard
from chat.keyboard import save_phone
from chat.keyboard import send_button_message
from chat.messages import BOT_PHONE_START_996, BOT_ORDER_CREATED, \
    BOT_ERROR_MESSAGE, BOT_ORDER_DONE, BOT_DRIVER_IN_PLACE, \
    BOT_CLIENT_BORT, BOT_DRIVER_LOCATION, BOT_ORDER_ACCEPTED
from .db import insert_address, insert_phone_numbers
from .sekret import PAGE_ACCESS_TOKEN


def need_phone(sender_id, data, order_status):
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
            insert_phone_numbers(data)
        else:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_ERROR_MESSAGE)
    except ValueError:
        need_address(sender_id, data, order_status)


def need_address(sender_id, data, order_status):
    message_id = data['entry'][0]['messaging'][0]['message']['text']
    if message_id == " ":
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ERROR_MESSAGE)
    elif message_id == len(message_id) < 3 or len(message_id) > 150:
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ERROR_MESSAGE)
    else:
        insert_address(data)
        create_order()
        send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                            BOT_ORDER_CREATED)
        get_order_keyboard(sender_id)
        if order_status == 'Принят':
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_ORDER_ACCEPTED)
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_DRIVER_LOCATION)
        elif order_status == 'Машина на месте':
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_DRIVER_IN_PLACE)
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_DRIVER_LOCATION)
        elif order_status == 'Клиент на борту':
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_CLIENT_BORT)
        else:
            send_button_message(sender_id, PAGE_ACCESS_TOKEN,
                                BOT_ORDER_DONE)
