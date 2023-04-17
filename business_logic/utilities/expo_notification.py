import requests
import json


def send_push_message(notification_details, extra=None):

    url = 'https://exp.host/--/api/v2/push/send'
    data_passenger = [
        {
            "to": notification_details['passenger_token'],
            "title": "Request Approved",
            "body": "Hello " + notification_details['passenger_name'] + ", your request to "+notification_details['destination'] + " has been approved",
            'sound': 'default',
            # 'data': {'someData': 'goes here'},
        },

    ]
    data_driver = [

        {
            "to": notification_details['driver_token'],
            "title": "Request Approved",
            "body": "Hello " + notification_details['driver_name'] + ", you have been assigned a trip going to "+notification_details['destination'],
            'sound': 'default',
            # 'data': {'someData': 'goes here'},
        }
    ]

    try:
        res = []
        res_passenger = requests.post(url, json=data_passenger)
        res_driver = requests.post(url, json=data_driver)
        res.append(res_passenger.json())
        res.append(res_driver.json())

        return res
    except Exception as exception:
        raise exception


# send_push_message('ExponentPushToken[J0YkqmGwt6jwk2SzhgRrN1]', 'sds', 'hfj')
