from django.db import models

from authentication.models import User
from .mixins.base_model_mixin import BaseModel
import uuid
from authentication.models import (Driver, Passenger)
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Vehicle(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    type_of_vehicle = models.CharField(max_length=50, default='Double Cabin')
    brand = models.CharField(max_length=50, default='Toyota')
    carrying_capacity = models.CharField(max_length=50,
                                         default='4')
    is_available = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Vehicle, self).save()

    def __str__(self):
        _str = '%s' % self.type_of_vehicle
        return _str



class Trip(BaseModel):
    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    pick_up_location = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    destination = models.CharField(max_length=100)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10, null=False, choices=STATUS, default='Pending')
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    cost = models.DecimalField(max_digits=10, decimal_places=2,default=200.00)
    is_completed = models.BooleanField(default=False)
    preimage = models.BinaryField(default=b'')
    payment_request = models.CharField(default='',max_length=500)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Trip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str



class PassengerTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class Blacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    reason = models.CharField(max_length=100, default='not good')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Blacklist, self).save()

    def __str__(self):
        _str = '%s' % self.organisation.name
        return _str


class PassengerBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.passenger.user.first_name
        return _str


class DriverBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.driver.user.first_name
        return _str


class VehicleBlacklist(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    blacklist = models.ForeignKey(
        Blacklist, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE)
    # reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(VehicleBlacklist, self).save()

    def __str__(self):
        _str = '%s' % self.vehicle.type_of_vehicle
        return _str


class DriverTrip(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverTrip, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str



class Notification(BaseModel):
    STATUS = (
        ('Sent', 'Sent'),
        ('Not sent', 'Not sent'),
    )
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    expo_token = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10, null=False, choices=STATUS, default='Pending')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Notification, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class PassengerNotification(BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerNotification, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str


class DriverNotification(BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverNotification, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str



class PhoneNumber(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    number = PhoneNumberField(max_length=16, unique=True, blank=False)
    user = models.ForeignKey(
        User,  null=False, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.number
        return _str


class UserPhoneNumber (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.ForeignKey(
        User, related_name='phone_numbers', null=False, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(
        PhoneNumber, null=False, on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(UserPhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.phone_number.number
        return _str


class Rating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    rate_value = models.FloatField(default=0.0, null=False)
    reason = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Rating, self).save()

    def __str__(self):
        _str = '%s' % self.reason
        return _str


class PassengerRating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    passenger = models.ForeignKey(
        Passenger, on_delete=models.CASCADE)

    rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PassengerRating, self).save()

    def __str__(self):
        _str = '%s' % self.rating.reason
        return _str


class DriverRating (BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))

    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE)

    rating = models.ForeignKey(
        Rating, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(DriverRating, self).save()

    def __str__(self):
        _str = '%s' % self.rating.reason
        return _str
