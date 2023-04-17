import api._views.vehicle_views as views
from api.views import vehicle_views as views
from django.urls import path

# from rest_framework import routers
# router = routers.DefaultRouter()

urlpatterns = [
   # path('', include(router.urls)),
    path(r'', views.ViewVehiclesListViewSet.as_view({'get': 'list'}),name="view_vehicles"),
    path(r'create/', views.CreateVehicleViewSet.as_view({'post': 'create'})),
    path(r'<str:id>/', views.RetrieveVehicleViewSet.as_view({'get': 'retrieve'}),name="retrieve_vehicle"),
    path(r'<str:id>/update/', views.UpdateVehicleViewSet.as_view({'put': 'update'})),
    path(r'<str:id>/delete/', views.DeleteVehicleViewSet.as_view({'delete': 'destroy'})),    
]
