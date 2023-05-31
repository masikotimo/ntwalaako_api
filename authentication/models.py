from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from api.mixins.base_model_mixin import BaseModel
import uuid
from django.core.mail import send_mail
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from core.mixins.model_mixins import Registrable
from django.contrib.auth.validators import UnicodeUsernameValidator
from core.utilities.unique_code_generators import UniqueMonotonicCodeGenerator
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.signals import post_save, post_delete
from api.models import Vehicle


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given  email, and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)

         # Check if 'vehicle' key exists in extra_fields for the case of drivers with cars
        # if 'vehicle' in extra_fields:
        #     extra_fields.pop('vehicle')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        null=True,
        blank=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=gender_choices, blank=True)


    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    Id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    is_passenger = models.BooleanField(
        _('user is a passenger'),
        default=False,
    )
    is_driver = models.BooleanField(
        _('user is a driver'),
        default=False,
    )
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(User, self).save()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }



class Passenger(Registrable):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.OneToOneField(
        User, related_name="Passenger", on_delete=models.CASCADE)

    is_available = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Passenger, self).save()

    def __str__(self):
        _str = '%s' % self.user.email
        return _str


class Driver(Registrable):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    permit_number = models.CharField(max_length=50,
                                     default='UAX')
    permit_class = models.CharField(max_length=50,
                                    default='UAX')

    permit_expiry_date = models.CharField(max_length=50,
                                          default='UAX')
    permit_issuance_date = models.CharField(max_length=50,
                                            default='UAX')

    is_available = models.BooleanField(default=True)

    user = models.OneToOneField(
        User, related_name="Driver", on_delete=models.CASCADE)

    vehicle = models.OneToOneField(
        Vehicle, related_name="Vehicle", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Driver, self).save()

    def __str__(self):
        _str = '%s' % self.user.email
        return _str


class PasswordResetInfo(models.Model):
    """
    The PasswordResetInfo Model:
        Lays specifications of how the PasswordResetInfo Entity / Table Should be Created in the Database.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, default='000000', unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(
        default=(timezone.now() + timezone.timedelta(hours=24)))

    def __str__(self):
        _str = ''
        if(self.user.first_name or self.user.last_name):
            if self.user.first_name:
                _str += self.user.first_name
            if self.user.last_name:
                _str += ' ' + self.user.last_name
        if self.user.email:
            _str += ' ' + self.user.email + ''
        if self.reset_code:
            _str += ' (' + str(self.reset_code) + ')'
        return _str

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self._state.adding:
            CodeGenerator = UniqueMonotonicCodeGenerator()
            self.reset_code = CodeGenerator.generate()
            self.expires_at = (timezone.now() + timezone.timedelta(hours=24))
            print(self.reset_code)
            print(self.expires_at)
        super(PasswordResetInfo, self).save()


    class Meta:
        verbose_name_plural = 'Password Reset Info'
        ordering = ['user']
    # End class Meta