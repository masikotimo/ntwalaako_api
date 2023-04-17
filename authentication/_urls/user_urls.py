import authentication._views.user_views as views
from django.urls import path


urlpatterns = [
    path('', views.ViewUsersListViewSet.as_view(
        {'get': 'list'}), name="view_user"),
    path(r'<str:Id>/', views.RetrieveUserViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_user"),
    path(r'<str:Id>/update/',
         views.UpdateUserViewSet.as_view({'put': 'update'})),
]
