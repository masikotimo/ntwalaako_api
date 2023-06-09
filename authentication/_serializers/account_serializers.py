from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.forms import SetPasswordForm  # , PasswordResetForm

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from authentication.models import (
    User, Passenger, Driver,  PasswordResetInfo)
from core.mixins.serializer_mixins import (BaseSerializer, ModelSerializer)


class UserLoginSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)
    password = serializers.CharField(
        max_length=254,
        min_length=6,
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        # login_data = attrs
        # return UserFacade().login(login_data)

        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials, Please Try again')
        if not user.is_active:
            raise AuthenticationFailed(
                'Your Account is Disabled. Contact Passenger')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified!')

        passenger = Passenger.objects.filter(user=user)
        driver = Driver.objects.filter(user=user)
        fleetmanager = FleetManager.objects.filter(user=user)
        return_object = {
            'email': user.email,
            'user_id': user.Id,
            'tokens': user.tokens()
        }

        if(passenger.exists()):
            return_object['passenger_id'] = passenger[0].id
        if(driver.exists()):
            return_object['driver_id'] = driver[0].id
        if(fleetmanager.exists()):
            return_object['fleetmanager_id'] = fleetmanager[0].id

        return return_object


class SendVerificationLinkSerializer(BaseSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)

    def validate(self, attrs):
        return attrs


class PasswordResetSerializer(BaseSerializer):
    email = serializers.EmailField(max_length=254, min_length=5)

    class Meta:
        pass

    def validate(self, attrs):
        return attrs


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    email = serializers.EmailField(max_length=254, min_length=5)
    code = serializers.CharField(max_length=6, required=True)
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)

    set_password_form_class = SetPasswordForm
    set_password_form = None
    user = None
    _errors = {}

    class Meta:
        pass

    def validate(self, attrs):
        self._errors = {}

        # Validate Password reset code Code
        try:
            user_data = attrs
            user = User.objects.filter(email=user_data['email'])
            if not user.exists():
                raise ValidationError({'detail': 'Invalid email!'})
            self.user = user[0]

            reset_instance = PasswordResetInfo.objects.filter(user=self.user)

            if not reset_instance.exists():
                raise ValidationError(
                    {'email': 'No password reset-code is set for User with this email (%s).' % user_data['email']})

            if not (reset_instance[0].reset_code == user_data['code']):
                raise ValueError

            if (timezone.now() > reset_instance[0].expires_at):
                raise ValidationError({'code': 'Reset code expired'})

        except (TypeError, ValueError, OverflowError):
            raise ValidationError({'code': ['Invalid value']})

        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        return self.set_password_form.save()
