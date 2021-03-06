import json
import requests
from chat.messages import BOT_ORDER_BUTTON_MESSAGE, BOT_WELCOME_MESSAGE
from modules.sekret import PAGE_ACCESS_TOKEN, URL


def send_button_message(sender_id, page_token, btn_message):
    params = {
        "access_token": page_token
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": btn_message

        }
    })
    response = requests.post(URL, params=params, headers=headers, data=data)
    return response


def get_basic_keyboard_message(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
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
                        }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    response = requests.post(URL, data=data,
                             params=params,
                             headers=headers)
    return response


def get_order_keyboard(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": BOT_ORDER_BUTTON_MESSAGE,
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Узнать статус заказа",
                            "payload": "order-status"
                        },
                        {
                            "type": "postback",
                            "title": "Машины рядом",
                            "payload": "nearest-drivers"
                        },
                        {
                            "type": "postback",
                            "title": "Отменить заказ",
                            "payload": "order-cancel"
                        }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    response = requests.post(URL, data=data,
                             params=params,
                             headers=headers)
    return response


def create_keyboard_fares(sender_id):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Проведите >/< для получения доп.тарифов",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Стандарт",
                                    "payload": "1"
                                },
                                {
                                    "type": "postback",
                                    "title": "Минивэн",
                                    "payload": "2"
                                },
                                {
                                    "type": "postback",
                                    "title": "Комфорт",
                                    "payload": "3"
                                }
                                ]
                        },
                        {
                            "title": "Проведите >/< для получения доп.тарифов",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Байк+",
                                    "payload": "4"
                                },
                                {
                                    "type": "postback",
                                    "title": "Портер",
                                    "payload": "5"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    response = requests.post(URL,
                             data=data,
                             params=params,
                             headers=headers)
    return response


def save_phone(sender_id):
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Нажмите на кнопку для сохранения вашего номера",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Сохранить номер телефона",
                            "payload": "save-phone"
                        },
                    ]
                }
            }
        }
    })
    headers = {'Content-type': 'application/json'}
    responce = requests.post(URL,
                             data=data,
                             params=params,
                             headers=headers)
    return responce
