from rest_framework import generics, mixins, status
from rest_framework import viewsets


class BaseCreateAPIView(generics.GenericAPIView, mixins.CreateModelMixin, viewsets.ViewSet):
    pass


class BaseListAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.ViewSet):
    pass


class BaseRetrieveAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.ViewSet):
    pass


class BaseUpdateAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, viewsets.ViewSet):
    pass


class BaseDeleteAPIView(generics.GenericAPIView, mixins.DestroyModelMixin, viewsets.ViewSet):
    pass
