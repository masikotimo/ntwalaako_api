import authentication._views.driver_views as driver_views
import authentication._views.passenger_views as passenger_views
import authentication._views.account_views as account_views


# Create your views here.


# Account Views
SendVerificationLinkView = account_views.SendVerificationLinkView
VerifyEmailView = account_views.VerifyEmailView
UserLoginView = account_views.UserLoginView
PasswordResetView = account_views.PasswordResetView
PasswordResetConfirmView = account_views.PasswordResetConfirmView
