import api._views.rating_views as views
from django.urls import path


urlpatterns = [
    path(r'', views.ViewRatingsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateRatingViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveRatingViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateRatingViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteRatingViewSet.as_view({'delete': 'destroy'})),
]
