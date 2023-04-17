import api._views.passenger_rating_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewPassengerRatingsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreatePassengerRatingViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrievePassengerRatingViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdatePassengerRatingViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeletePassengerRatingViewSet.as_view({'delete': 'destroy'})),
]
