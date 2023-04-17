from django.shortcuts import render
from api.models import DriverBlacklist
from rest_framework import viewsets
from api._serializers.driver_blacklist_serializers import DriverBlacklistSerializer, CreateDriverBlacklistSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateDriverBlacklistViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverBlacklist.objects.all()
    serializer_class = CreateDriverBlacklistSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewDriverBlacklistsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverBlacklist.objects.all()
    serializer_class = DriverBlacklistSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['driver']

    def get(self, request):
        if 'driverblacklists' in cache:
            # get results from cache
            driverblacklists = cache.get('driverblacklists')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [driverblacklist.to_json()
                       for driverblacklist in queryset]
            # store data in cache
            cache.set('driverblacklists', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveDriverBlacklistViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverBlacklist.objects.all()
    serializer_class = DriverBlacklistSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateDriverBlacklistViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverBlacklist.objects.all()
    serializer_class = DriverBlacklistSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteDriverBlacklistViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverBlacklist.objects.all()
    serializer_class = DriverBlacklistSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
