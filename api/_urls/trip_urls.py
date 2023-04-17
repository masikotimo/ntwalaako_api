import api._views.trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/', views.CreateTripViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateTripViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteTripViewSet.as_view({'delete': 'destroy'})),
]
