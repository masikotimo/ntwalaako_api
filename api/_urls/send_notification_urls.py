from django.urls import path
from api.views import sendNotification_views

urlpatterns = [
    path('', sendNotification_views.SendNotificationView.as_view(),
         name='send_notification_views'),

]
