from django.urls import path
from api._views.driver_available_views import DriverAvailableView

urlpatterns = [
    path('', DriverAvailableView.as_view(),
         name='get_driver_available_times_views'),

]
