from authentication.models import User
from authentication._serializers.user_serializers import (
    UpdateUserSerializer,
    UserProfileSerializer,
    UserSerializer)
from core.mixins import view_mixins
from rest_framework import generics, status
from rest_framework.response import Response


class ViewUsersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'Id'
    #filter_backends = [filters.SearchFilter]
    search_fields = ['user']

    def get(self, request):
        if 'user' in cache:
            # get results from cache
            user = cache.get('user')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('user', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveUserViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'Id'

    def get(self, request, Id=None):
        try:
            return self.retrieve(request, Id)
        except Exception as exception:
            raise exception


class UpdateUserViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = 'Id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception
