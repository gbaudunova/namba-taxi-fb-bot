import os
import requests
from modules.sekret import *


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
                "Вызовите команду Get Started b введите любое сообщение"
    }
        ]
    }
    r = requests.post("https://graph.facebook.com/v2.10/me/messenger_profile", params=params, json=data)


def setup_all():
    setup_getStarted()
    setup_greeting()