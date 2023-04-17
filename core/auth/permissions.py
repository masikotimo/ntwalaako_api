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
        permit = bool(group is not None and ( (group == 'administrator') or (group == 'staff') or (group == 'client')))
        if group == 'administrator':
            permit = bool(Administrator.objects.all().filter(user=request.user).exists())
        if group == 'staff':
            permit = bool(Staff.objects.all().filter(user=request.user).exists())
        if group == 'vendor':
            permit = bool(Vendor.objects.all().filter(user=request.user).exists())
        if group == 'courier':
            permit = bool(Courier.objects.all().filter(user=request.user).exists())
        if group == 'client':
            permit = bool(Client.objects.all().filter(user=request.user).exists())

        return permit


class IsAdministrator(BasePermission):
    """
    Gives access to Administrators.
    """

    def has_permission(self, request):
        admin = bool(Administrator.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and admin)


class IsStaff(BasePermission):
    """
    Gives access to Staff Members.
    """

    def has_permission(self, request):
        staff = bool(Staff.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and staff)


class IsVendor(BasePermission):
    """
    Gives access to Vendors.
    """

    def has_permission(self, request):
        vendor = bool(Vendor.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and vendor)


class IsCourier(BasePermission):
    """
    Gives access to Courier Members.
    """

    def has_permission(self, request):
        courier = bool(Courier.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and courier)


class IsClient(BasePermission):
    """
    Gives access to Clients.
    """

    def has_permission(self, request):
        client = bool(Client.objects.filter(user = request.user).exists())
        return bool(IsAuthenticated and client)


def is_administrator(request):
    group = request.META.get('HTTP_USER_GROUP')
    admin = bool(Administrator.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and admin and (group == 'administrator'))

def is_staff(request):
    group = request.META.get('HTTP_USER_GROUP')
    staff = bool(Staff.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and staff and (group == 'staff'))

def is_vendor(request):
    group = request.META.get('HTTP_USER_GROUP')
    vendor = bool(Vendor.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and vendor and (group == 'vendor'))

def is_courier(request):
    group = request.META.get('HTTP_USER_GROUP')
    courier = bool(Courier.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and courier and (group == 'courier'))

def is_client(request):
    group = request.META.get('HTTP_USER_GROUP')
    client = bool(Client.objects.filter(user = request.user).exists())
    return bool(IsAuthenticated and client and (group == 'client'))
