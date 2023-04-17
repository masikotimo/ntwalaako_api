
from authentication.models import Passenger
from api.models import Trip
from rest_framework.response import Response
from business_logic.utilities.expo_notification import send_push_message
from rest_framework import serializers, status, generics
from api._serializers.send_notification_serializers import SendNotificationSerializer
from django.utils.timezone import utc
import datetime
from django.http import HttpResponse
from core.utilities.rest_exceptions import (ValidationError)


class SendNotificationView(generics.GenericAPIView):
    serializer_class = SendNotificationSerializer

    def post(self, request, format=None):

        serializer = SendNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            notification_details = (serializer.create(request.data))

            res = send_push_message(notification_details)

            return Response(res,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
