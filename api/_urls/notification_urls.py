import api._views.notitification_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path(r'', views.ViewNotificationsListViewSet.as_view(
        {'get': 'list'}), name="view_vehicles"),
    path(r'create/',
         views.CreateNotificationViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveNotificationViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_vehicle"),
    path(r'<str:id>/update/',
         views.UpdateNotificationViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteNotificationViewSet.as_view({'delete': 'destroy'})),
]
