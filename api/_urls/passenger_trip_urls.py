import api._views.passenger_trip_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    path(r'create/',
         views.CreatePassengerTripViewSet.as_view({'post': 'create'})),

    path(r'', views.ViewAllPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    
    path('pay-trip', views.PayPassengerTripView.as_view(),
         name='pay for trip'),

    path('settle-trip', views.SettlePassengerTripView.as_view(),
         name='settle-trip'),

    path(r'<str:passenger_id>/', views.ViewPassengerTripsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),

    path(r'<str:passenger_id>/<str:id>/', views.RetrievePassengerTripViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),

    path(r'<str:passenger_id>/<str:id>/update/',
         views.UpdatePassengerTripViewSet.as_view({'put': 'update'})),

    path(r'<str:passenger_id>/<str:id>/delete/',
         views.DeletePassengerTripViewSet.as_view({'delete': 'destroy'})),
]
