from django.test import TestCase
import authentication.models as auth_models
import uuid


class TestUserModal(TestCase):
    def setUp(self):
        user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

    def test_existence_of_user_created(self):

        check_existence = auth_models.User.objects.filter(
            first_name='timo').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_user_record(self):

        user_store = auth_models.User.objects.get(first_name='timo')
        user_store.first_name = 'masiko'
        user_store.save()
        check_existence = auth_models.User.objects.filter(
            first_name='masiko').exists()
        self.assertTrue(check_existence)

    def test_delete_of_user_record(self):

        user_store = auth_models.User.objects.get(first_name='timo')
        user_store.delete()
        check_existence = auth_models.User.objects.filter(
            first_name='timo').exists()
        self.assertFalse(check_existence)


class TestSystemAdminModal(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timoxx', last_name='timoxx', email='masikotimo@gmail', password='xsxsee2323')

        cls.user1 = auth_models.User.objects.create(
            first_name='masiko', last_name='masiko', email='mmickey@gmail', password='xsxsee2323')

        cls.sysAdmin = auth_models.SystemAdmin.objects.create(
            user=cls.user)

    def test_existence_of_system_Admin_created(self):

        check_existence = auth_models.SystemAdmin.objects.filter(
            user=self.user).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_system_Admin_record(self):

        system_admin_store = auth_models.SystemAdmin.objects.get(
            user=self.user)
        system_admin_store.user = self.user1
        system_admin_store.save()
        check_existence = auth_models.SystemAdmin.objects.filter(
            user=self.user1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_system_Admin_record(self):

        system_admin_store = auth_models.SystemAdmin.objects.get(
            user=self.user)
        system_admin_store.delete()
        check_existence = auth_models.SystemAdmin.objects.filter(
            user=self.user).exists()
        self.assertFalse(check_existence)


class TestDriverModal(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timoxx', last_name='timoxx', email='masikotimo@gmail', password='xsxsee2323')

        cls.user1 = auth_models.User.objects.create(
            first_name='masiko', last_name='masiko', email='mmickey@gmail', password='xsxsee2323')

        cls.driver = auth_models.Driver.objects.create(
            user=cls.user)

    def test_existence_of_driver_created(self):

        check_existence = auth_models.Driver.objects.filter(
            user=self.user).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_driver_record(self):

        driver_store = auth_models.Driver.objects.get(
            user=self.user)
        driver_store.user = self.user1
        driver_store.save()
        check_existence = auth_models.Driver.objects.filter(
            user=self.user1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_driver_record(self):

        driver_store = auth_models.Driver.objects.get(
            user=self.user)
        driver_store.delete()
        check_existence = auth_models.Driver.objects.filter(
            user=self.user).exists()
        self.assertFalse(check_existence)


class TestPassengerModal(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timoxx', last_name='timoxx', email='masikotimo@gmail', password='xsxsee2323')

        cls.user1 = auth_models.User.objects.create(
            first_name='masiko', last_name='masiko', email='mmickey@gmail', password='xsxsee2323')

        cls.passenger = auth_models.Passenger.objects.create(
            user=cls.user)

    def test_existence_of_passenger_created(self):

        check_existence = auth_models.Passenger.objects.filter(
            user=self.user).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_passenger_record(self):

        passenger_store = auth_models.Passenger.objects.get(
            user=self.user)
        passenger_store.user = self.user1
        passenger_store.save()
        check_existence = auth_models.Passenger.objects.filter(
            user=self.user1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_passenger_record(self):

        passenger_store = auth_models.Passenger.objects.get(
            user=self.user)
        passenger_store.delete()
        check_existence = auth_models.Passenger.objects.filter(
            user=self.user).exists()
        self.assertFalse(check_existence)


class TestFleetManagerModal(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timoxx', last_name='timoxx', email='masikotimo@gmail', password='xsxsee2323')

        cls.user1 = auth_models.User.objects.create(
            first_name='masiko', last_name='masiko', email='mmickey@gmail', password='xsxsee2323')

        cls.fleetmanager = auth_models.FleetManager.objects.create(
            user=cls.user)

    def test_existence_of_fleetmanager_created(self):

        check_existence = auth_models.FleetManager.objects.filter(
            user=self.user).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_fleetmanager_record(self):

        fleetmanager_store = auth_models.FleetManager.objects.get(
            user=self.user)
        fleetmanager_store.user = self.user1
        fleetmanager_store.save()
        check_existence = auth_models.FleetManager.objects.filter(
            user=self.user1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_fleetmanager_record(self):

        fleetmanager_store = auth_models.FleetManager.objects.get(
            user=self.user)
        fleetmanager_store.delete()
        check_existence = auth_models.FleetManager.objects.filter(
            user=self.user).exists()
        self.assertFalse(check_existence)
