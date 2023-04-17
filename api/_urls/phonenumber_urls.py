from django.urls import path
from api.views import phonenumber_views as views

urlpatterns = [
    path(r'create/',
         views.CreatePhoneNumberViewSet.as_view({'post': 'create'})),
    path('', views.ViewPhoneNumbersListViewSet.as_view(
        {'get': 'list'}), name="view_organizations"),
    path(r'<str:id>/', views.RetrievePhoneNumberViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_organization"),
    path(r'<str:id>/update/',
         views.UpdatePhoneNumberViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeletePhoneNumberViewSet.as_view({'delete': 'destroy'})),
]
