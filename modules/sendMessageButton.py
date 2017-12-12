from api.handlers_order import cancel_order, delete_order_id
from api.nearest_drivers import get_nearest_drivers
from api.order_status import get_order_status
from chat.keyboard import create_keyboard_fares
from chat.keyboard import get_basic_keyboard_message
from chat.keyboard import send_button_message
from chat.messages import BOT_ASK_FARE, BOT_ASK_PHONE, BOT_FARES_LINK, BOT_MESSAGE_NEAREST_CARS, BOT_FARE_INFO, \
    BOT_MESSAGE_MY_ORDER_STATUS, BOT_ORDER_CANCEL, BOT_ASK_ADDRESS
from modules.get_data import get_order_id
from .db import insert_fares
from .sekret import PAGE_ACCESS_TOKEN


def decide_button(sender_id, message, data):
    data_order_id = get_order_id()
    order_id = data_order_id[1]

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
        get_order_status(order_id)
    elif message == 'nearest-drivers':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_MESSAGE_NEAREST_CARS)
        get_nearest_drivers()

    elif message == 'order-cancel':
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ORDER_CANCEL)
        cancel_order(order_id)
        delete_order_id()

    else:
        callback = data['entry'][0]['messaging'][0]['postback']['payload']
        print(callback)
        insert_fares(data)
        send_button_message(sender_id, PAGE_ACCESS_TOKEN, BOT_ASK_ADDRESS)





