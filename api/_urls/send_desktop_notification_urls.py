from django.urls import path
from api._views.sendDesktopNotification_views import SendDesktopNotificationView

urlpatterns = [
    path('', SendDesktopNotificationView.as_view(),
         name='send_notification_views'),

]
