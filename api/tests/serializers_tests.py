from django.test import TestCase
import api.models as api_models
import api.serializers as serializers


class TestVehicleSerializers(TestCase):
    def setUp(self):
        self.vehicle = api_models.Vehicle.objects.create(
            type_of_vehicle='range-rover', carrying_capacity=5)

        self.serializer_data = {
            'type_of_vehicle': 'range-rover',
            'carrying_capacity': 5
        }

        self.serializer = serializers.VehicleSerializer(instance=self.vehicle)

    def test_contains_expected_fields(self):

        data = self.serializer_data

        self.assertEqual(set(data.keys()), set(
            ['type_of_vehicle', 'carrying_capacity']))
