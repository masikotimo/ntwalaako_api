from django.shortcuts import render
from authentication.models import Passenger
from rest_framework import viewsets, generics, status
from authentication._serializers.passenger_serializers import PassengerSerializer, CreatePassengerSerializer, PassengerLoginSerializer, UpdatePassengerSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters
from rest_framework.response import Response


# Create your views here.


class CreatePassengerViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = CreatePassengerSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewPassengersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['user']

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


class RetrievePassengerViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdatePassengerViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = UpdatePassengerSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeletePassengerViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception


class PassengerLoginView(generics.GenericAPIView):
    serializer_class = PassengerLoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            data = serializer.validated_data
            # print(data)
            return Response(data=data, status=status.HTTP_200_OK)
