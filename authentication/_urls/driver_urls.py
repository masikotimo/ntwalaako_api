import authentication._views.driver_views as views
from django.urls import path

urlpatterns = [
    path(r'create/',
         views.CreateDriverViewSet.as_view({'post': 'create'})),
    path('', views.ViewDriversListViewSet.as_view(
        {'get': 'list'}), name="view_driver"),
    
    path(r'available/', views.ViewDriversAvailableListViewSet.as_view(
    {'get': 'list'}), name="view_available_driver"),
        
    path(r'<str:id>/', views.RetrieveDriverViewSet.as_view(
        {'get': 'retrieve'}), name="retrieve_driver"),
    path(r'<str:id>/update/',
         views.UpdateDriverViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/',
         views.DeleteDriverViewSet.as_view({'delete': 'destroy'})),
    path(r'account/login/', views.DriverLoginView.as_view()),

]
