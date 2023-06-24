import requests
from core.utilities.rest_exceptions import (ValidationError)
from api.models import DriverNotification, PassengerNotification


def send_push_message(to , message,title, extra=None):

    user_expo_token =""
    passenger_notification_instances = PassengerNotification.objects.filter(
            passenger__id=to)

    driver_notification_instances = DriverNotification.objects.filter(
        driver__id=to)

    if not passenger_notification_instances.exists():
        if not driver_notification_instances.exists():
            raise ValidationError(
                {'detail': 'Driver/Passenger has not yet regisered his application to receive notifications !'})
        user_expo_token = driver_notification_instances[0].notification.expo_token
    
    else:
        user_expo_token = passenger_notification_instances[0].notification.expo_token

    url = 'https://exp.host/--/api/v2/push/send'
    detail = [
        {
            "to": user_expo_token,
            "title": title,
            "body": message,
            'sound': 'default',
            # 'data': {'someData': 'goes here'},
        },
    ]

    try:
        res = []
        res_details = requests.post(url, json=detail)
        res.append(res_details.json())
        print("notification dets",res)

        return res
    except Exception as exception:
        raise exception


# send_push_message('ExponentPushToken[J0YkqmGwt6jwk2SzhgRrN1]', 'sds', 'hfj')
