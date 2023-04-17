"""car_booking_api URL Configuration
"""
from django.conf.urls import url, re_path, include
from django.contrib import admin
from rest_framework import routers, permissions
import authentication.urls as auth_urls
import api.urls as api_urls
from django.urls import path


# DRF - YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://ntwaalako.co.ug/pages.php?page=vehicles",
        contact=openapi.Contact(email="info@ntwaalako.co.ug"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Default route
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    # Admin route
    url(r'^admin/', admin.site.urls),

    # accounts
    path('account/', include('authentication.urls')),

    # User Routes
    path('drivers/', include(auth_urls.driver_urls)),
    path('passengers/', include(auth_urls.passenger_urls)),
    path('users/', include(auth_urls.user_urls)),
    # TD: to add a route for user

    # api routes
    path('vehicles/', include(api_urls.vehicle_urls)),
    path('passengerblacklists/', include(api_urls.passenger_blacklist_urls)),


    path('trips/', include(api_urls.trip_urls)),
    path('passengertrips/', include(api_urls.passenger_trip_urls)),

    path('notification/', include(api_urls.notification_urls)),

    path('sendnotification/', include(api_urls.send_notification_urls)),
    path('sendDesktopnotification/',
         include(api_urls.send_desktop_notification_urls)),

    path('rating/', include(api_urls.rating_urls)),
    path('driver-rating/', include(api_urls.driver_rating_urls)),


    path('phonenumber/', include(api_urls.phonenumber_urls)),
    path('reports/', include(api_urls.reports_urls)),
    path('get-driver-time/', include(api_urls.driver_available_urls)),

    # drf-yasg Routes
    path('docs/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),


]
