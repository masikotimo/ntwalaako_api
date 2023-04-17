from rest_framework.permissions import BasePermission, IsAuthenticated
from authentication.models import *


class HasUserGroup(BasePermission):
    """
    Gives access to Grouped Users.
    """

    message = 'Operation not allowed. Either the user-group field was not specified in the request Header or the current user does not belong to the specified user-group.'

    def has_permission(self, request):
        permit = False
        group = request.META.get('HTTP_USER_GROUP')
        permit = bool(group is not None and ((group == 'SystemAdmin') or (
            group == 'passenger') or (group == 'driver') or (group == 'fleet manager')))
        if group == 'SystemAdmin':
            permit = bool(SystemAdmin.objects.all().filter(
                user=request.user).exists())
        if group == 'passenger':
            permit = bool(Passenger.objects.all().filter(
                user=request.user).exists())
        if group == 'driver':
            permit = bool(Driver.objects.all().filter(
                user=request.user).exists())
        if group == 'fleet manager':
            permit = bool(FleetManager.objects.all().filter(
                user=request.user).exists())

        return permit


class IsSystemAdmin(BasePermission):
    """
    Gives access to SystemAdmins.
    """

    def has_permission(self, request):
        admin = bool(SystemAdmin.objects.filter(user=request.user).exists())
        return bool(IsAuthenticated and admin)


class IsPassenger(BasePermission):
    """
    Gives access to Passenger Members.
    """

    def has_permission(self, request):
        passenger = bool(Passenger.objects.filter(user=request.user).exists())
        return bool(IsAuthenticated and passenger)


class IsDriver(BasePermission):
    """
    Gives access to Drivers.
    """

    def has_permission(self, request):
        driver = bool(Driver.objects.filter(user=request.user).exists())
        return bool(IsAuthenticated and driver)


class IsFleetManager(BasePermission):
    """
    Gives access to FleetManager Members.
    """

    def has_permission(self, request):
        fleet_manager = bool(FleetManager.objects.filter(
            user=request.user).exists())
        return bool(IsAuthenticated and fleet_manager)


def is_systemAdmin(request):
    group = request.META.get('HTTP_USER_GROUP')
    admin = bool(SystemAdmin.objects.filter(user=request.user).exists())
    return bool(IsAuthenticated and admin and (group == 'SystemAdmin'))


def is_passenger(request):
    group = request.META.get('HTTP_USER_GROUP')
    passenger = bool(Passenger.objects.filter(user=request.user).exists())
    return bool(IsAuthenticated and passenger and (group == 'passenger'))


def is_driver(request):
    group = request.META.get('HTTP_USER_GROUP')
    driver = bool(Driver.objects.filter(user=request.user).exists())
    return bool(IsAuthenticated and driver and (group == 'driver'))


def is_fleet_manager(request):
    group = request.META.get('HTTP_USER_GROUP')
    fleet_manager = bool(FleetManager.objects.filter(
        user=request.user).exists())
    return bool(IsAuthenticated and fleet_manager and (group == 'fleet manager'))
