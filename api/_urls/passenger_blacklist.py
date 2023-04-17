import api._views.passenger_blacklist as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    # path(r'create/',
    #      views.CreatePassengerBlacklistViewSet.as_view({'post': 'create'})),
    # path('', views.ViewPassengerBlacklistsListViewSet.as_view(
    #     {'get': 'list'}), name="view_vehicles"),
    # path(r'<str:id>/', views.RetrievePassengerBlacklistViewSet.as_view(
    #     {'get': 'retrieve'}), name="retrieve_vehicle"),
    # # path(r'<str:id>/update/',
    # #      views.UpdatePassengerBlacklistViewSet.as_view({'put': 'update'})),
    # path(r'<str:id>/delete/',
    #      views.DeletePassengerBlacklistViewSet.as_view({'delete': 'destroy'})),
]
