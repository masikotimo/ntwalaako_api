
from authentication.models import  Passenger
from api.models import  Trip
from rest_framework.response import Response
from business_logic.utilities.desktop_notification import send_desktop_message
from rest_framework import serializers, status, generics, views
from api._serializers.send_desktop_notification_serializers import SendDesktopNotificationSerializer
from django.utils.timezone import utc
from django.http import HttpResponse
from core.utilities.rest_exceptions import (ValidationError)


class SendDesktopNotificationView(generics.GenericAPIView):
    serializer_class = SendDesktopNotificationSerializer

    def post(self, request, format=None):

        # fleet_manager = request.data.pop('fleet_manager', None)

        # fleet_manager_instances = FleetManager.objects.all().filter(id=fleet_manager)

        # if not fleet_manager_instances.exists():
        #     raise ValidationError({'fleet_manager': 'Invalid value!'})

        # fleet_manager_instance = fleet_manager_instances[0]

        # fleet_manager_notifications = FleetManagerNotification.objects.all().filter(
        #     fleet_manager=fleet_manager_instance)

        # token = fleet_manager_notifications[0].notification.expo_token
        # res = send_desktop_message(token)

        return Response("res",
                        status=status.HTTP_201_CREATED)
