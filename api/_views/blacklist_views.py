from django.shortcuts import render
from api.models import Blacklist
from rest_framework import viewsets
from api._serializers.blacklist_serializer import CreateBlacklistSerializer, BlacklistSerializer
from car_booking_api.mixins import view_mixins
from car_booking_api import filters

# Create your views here.


class CreateBlacklistViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = CreateBlacklistSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewBlacklistsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['organisation']

    def get(self, request):
        if 'blacklists' in cache:
            # get results from cache
            blacklists = cache.get('blacklists')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [blacklist.to_json() for blacklist in queryset]
            # store data in cache
            cache.set('blacklists', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveBlacklistViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateBlacklistViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteBlacklistViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
