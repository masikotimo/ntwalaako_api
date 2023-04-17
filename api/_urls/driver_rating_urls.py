import api._views.driver_rating_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewDriverRatingsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateDriverRatingViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveDriverRatingViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateDriverRatingViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverRatingViewSet.as_view({'delete': 'destroy'})),
]
