import json
import requests
from .sekret import *


# def sendFares(sender_id):
#     params = {
#         "access_token": PAGE_ACCESS_TOKEN
#     }
#     data = json.dumps({
#         "recipient": {
#             "id": sender_id
#         },
#         "message": {
#             "attachment": {
#                 "type": "template",
#                 "payload": {
#                     "template_type": "button",
#                     "text": "Нажмите на кнопку для сохранения вашего номера",
#                     "buttons": [
#                         {
#                             "type": "postback",
#                             "title": "Стандарт",
#                             "payload": "standard-fare"
#                         },
#                         {
#                             "type": "postback",
#                             "title": "Минивэн",
#                             "payload": "minivan-fare"
#                         },
#                         {
#                             "type": "postback",
#                             "title": "Комфорт",
#                             "payload": "comfort-fare"
#                         },
#                         {
#                             "type": "postback",
#                             "title": "Байк+",
#                             "payload": "bike-fare"
#                         },
#                         {
#                             "type": "postback",
#                             "title": "Портер",
#                             "payload": "porter-fare"
#                         }
#                     ]
#                 }
#             }
#         }
#     })
#     headers = {'Content-type': 'application/json'}
#     r = requests.post(URL, data=data, params=params, headers=headers)
#
