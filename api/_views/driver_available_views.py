
from authentication.models import Driver
from api.models import Trip
from rest_framework.response import Response
from rest_framework import status, generics
from api._serializers.driver_availability_serializers import DriverAvailableSerializer
from core.utilities.rest_exceptions import (ValidationError)


class DriverAvailableView(generics.GenericAPIView):
    serializer_class = DriverAvailableSerializer

    def post(self, request, format=None):

        driver = request.data.pop('driver', None)

        driver_instances = Driver.objects.all().filter(id=driver)

        if not driver_instances.exists():
            raise ValidationError(
                {'driver': 'driver doesnt exist contact Maintainer!'})

        driver_instance = driver_instances[0]

        trips = Trip.objects.all().filter(
            driver=driver_instance).filter(
            status='Approved')

        driver_booked_times = []
        for trip in trips:
            driver_booked_times.append(trip.date)

        res = driver_booked_times

        return Response(res,
                        status=status.HTTP_201_CREATED)
