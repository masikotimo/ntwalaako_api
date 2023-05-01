from django.shortcuts import render
from api.models import PassengerTrip, Trip
from authentication.models import Passenger, User
from rest_framework import viewsets,status, generics
from api._serializers.passenger_trip_serializer import PassengerTripSerializer, CreatePassengerTripSerializer, PayForPassengerTripSerializer, UpdatePassengerTripSerializer
from car_booking_api.mixins import view_mixins
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from car_booking_api import filters
from core.utilities.rest_exceptions import (ValidationError)
from lnd_grpc import Client
from rest_framework.response import Response
import time


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.


def _get_queryset(view_instance):
    try:
        passenger_id = view_instance.kwargs['passenger_id']

        # 03. Validate Vendor

        # ...
        _passengers = Passenger.objects.filter(id=passenger_id)
        if not _passengers.exists():
            raise ValidationError(
                {'passenger_id': 'passenger with the specified id does not exist!'})

        return PassengerTrip.objects.all().filter(passenger=_passengers[0])
    except Exception as exception:
        raise exception


class CreatePassengerTripViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = CreatePassengerTripSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewPassengerTripsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['type_of_vehicle', 'brand']

    def get(self, request):
        if 'vehicles' in cache:
            # get results from cache
            vehicles = cache.get('vehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('vehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

    def get_queryset(self):
        return _get_queryset(self)


class ViewAllPassengerTripsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializer
    lookup_field = 'id'
    filter_backends = []
    search_fields = ['type_of_vehicle', 'brand']

    def get(self, request):

        try:
            return self.list(request)
        except Exception as exception:
            raise exception


class RetrievePassengerTripViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class UpdatePassengerTripViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = UpdatePassengerTripSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)


class DeletePassengerTripViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PassengerTrip.objects.all()
    serializer_class = PassengerTripSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

    def get_queryset(self):
        return _get_queryset(self)




class PayPassengerTripView(generics.GenericAPIView):
    serializer_class = PayForPassengerTripSerializer

    def post(self, request, format=None):

        passenger_trip = request.data.pop('passenger_trip')

        passenger_trip_instances = PassengerTrip.objects.all().filter(id=passenger_trip)
        if not passenger_trip_instances.exists():
            raise ValidationError(
                {'passenger_trip': 'Passenger doesnt exist !'})

        passenger = passenger_trip_instances[0].passenger.user
        trip = passenger_trip_instances[0].trip

        passengerLnd = Client(lnd_dir = passenger.lnd_directory,macaroon_path= passenger.macaroon_path, tls_cert_path= passenger.tls_cert_path,network = passenger.network,grpc_host= passenger.grpc_host,grpc_port=passenger.grpc_port)

        resp = passengerLnd.send_payment(payment_request=trip.payment_request)
        
        # print("payment sent", resp)

        # if resp.payment_error is None:
        #     print("Payment successful!")
        # else:
        #     print("Payment failed:", resp.payment_error)

        trip_instances = Trip.objects.get(id=trip.id)
        trip_instances.status = "PAID"
        trip_instances.save()

        # return "sucess"

        return Response("success",
                        status=status.HTTP_201_CREATED)


class SettlePassengerTripView(generics.GenericAPIView):
    serializer_class = PayForPassengerTripSerializer

    def post(self, request, format=None):

        passenger_trip = request.data.pop('passenger_trip')

        passenger_trip_instances = PassengerTrip.objects.all().filter(id=passenger_trip)
        if not passenger_trip_instances.exists():
            raise ValidationError(
                {'passenger_trip': 'Passenger doesnt exist !'})

        
        trip = passenger_trip_instances[0].trip
        driver = trip.driver.user

        try:
            driverLnd = Client(lnd_dir = driver.lnd_directory,macaroon_path= driver.macaroon_path, tls_cert_path= driver.tls_cert_path,network = driver.network,grpc_host= driver.grpc_host,grpc_port=driver.grpc_port)

            # print('gotten-preimage',trip.preimage)            
            resp = driverLnd.settle_invoice(preimage=trip.preimage)
            driver_instances = User.objects.get(Id=driver.Id)
            driver_instances.wallet_balance = 500.00
            driver_instances.save()


            return Response("Invoice settled successfully, your wallet has been topped up!",
                        status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Failed to settle invoice:", str(e))
            return Response("Failed to settle invoice! Either it has expired or its been canceled already",)


        # return "sucess"

        
