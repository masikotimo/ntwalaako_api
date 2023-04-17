import api.models as api_models
import authentication.models as auth_models
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from authentication.serializers import DriverSerializer
from api._serializers.trip_serializer import (
    TripSerializer, CreateTripSerializer)
from api._serializers.vehicle_serializer import VehicleSerializer

