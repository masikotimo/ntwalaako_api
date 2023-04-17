"""
    This module is an aggregate of all the auth urls / endpoints.
"""

import authentication._urls.driver_urls as driver_urls
import authentication._urls.passenger_urls as passenger_urls
import authentication._urls.user_urls as user_urls

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_auth.views import (LogoutView, PasswordChangeView)

from authentication.views import (
    # RegisterUserView,
    VerifyEmailView,
    SendVerificationLinkView,
    # UserLoginView,
    PasswordResetView, PasswordResetConfirmView
)


urlpatterns = [
    # jwt : Get Access token and its coresponding Refresh Token
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # jwt : User a Refresh Token to refresh the Access Token
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration and social media authentication
    # path(r'registration/register/', RegisterUserView.as_view(),
    #      name='account_signup_or_register'),
    # path(r'auth/registration/', include('rest_auth.registration.urls')),

    # Verifies email for successfull Registration
    path(
        r'verify-email/',
        VerifyEmailView.as_view(),
        name='verify-email'
    ),

    # Resends email verification link for successfull Registration
    path(
        r'verification-link/',
        SendVerificationLinkView.as_view(),
        name='email-verification-link'
    ),



    # URLs that do not require a session or valid token
    path(r'password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path(r'password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),

    # Login to the carbooking Platform
    # path(
    #     r'login/',
    #     UserLoginView.as_view(),
    #     name='login'
    # ),

    # URLs that require a user to be logged in with a valid session / token.
    path(r'logout/', LogoutView.as_view(), name='rest_logout'),
    path(r'password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),
]
