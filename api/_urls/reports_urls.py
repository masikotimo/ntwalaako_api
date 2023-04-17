from django.urls import path
from api._views.Reports_views import ReportsView

urlpatterns = [
    path('', ReportsView.as_view(),
         name='reports_views'),

]
