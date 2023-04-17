from api.models import PhoneNumber
from api._serializers.phonenumber_serializers import PhoneNumberSerializer
from core.mixins import view_mixins
from core.utilities.rest_exceptions import (PermissionDenied)


class CreatePhoneNumberViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewPhoneNumbersListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    permission_classes = []
    serializer_class = PhoneNumberSerializer
    lookup_field = 'id'
    # #filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request):
        if 'PhoneNumbers' in cache:
            # get results from cache
            PhoneNumbers = cache.get('PhoneNumbers')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [PhoneNumber.to_json() for PhoneNumber in queryset]
            # store data in cache
            cache.set('PhoneNumbers', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrievePhoneNumberViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdatePhoneNumberViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeletePhoneNumberViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception
