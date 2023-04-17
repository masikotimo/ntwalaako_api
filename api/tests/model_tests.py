from django.test import TestCase
import api.models as api_models
import authentication.models as auth_models
import uuid
# Create your tests here.


class TestVehicleModal(TestCase):
    def setUp(self):
        vehicle = api_models.Vehicle.objects.create(
            type_of_vehicle='range-rover', carrying_capacity=5)

    def test_existence_of_vehicle_created(self):

        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='range-rover').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_vehicle_record(self):

        vehicle_store = api_models.Vehicle.objects.get(
            type_of_vehicle='range-rover')
        vehicle_store.type_of_vehicle = 'bmw'
        vehicle_store.save()
        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='bmw').exists()
        self.assertTrue(check_existence)

    def test_delete_of_vehicle_record(self):

        vehicle_store = api_models.Vehicle.objects.get(
            type_of_vehicle='range-rover')
        vehicle_store.delete()
        check_existence = api_models.Vehicle.objects.filter(
            type_of_vehicle='range-rover').exists()
        self.assertFalse(check_existence)


class TestOrganisationModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra', id=1)

    def test_existence_of_organisation_created(self):

        check_existence = api_models.Organisation.objects.filter(
            name='Unra').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_organisation_record(self):

        organisation_store = api_models.Organisation.objects.get(
            name='Unra')
        organisation_store.name = 'kakira'
        organisation_store.save()
        check_existence = api_models.Organisation.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_organisation_record(self):

        organisation_store = api_models.Organisation.objects.get(
            name='Unra')
        organisation_store.delete()
        check_existence = api_models.Organisation.objects.filter(
            name='Unra').exists()
        self.assertFalse(check_existence)


class TestOrganisationFleetManagerModal(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')
        cls.fleetmanager = auth_models.FleetManager.objects.create(
            user=cls.user, id=1)
        cls.organisation = api_models.Organisation.objects.create(
            name='Unra', id=1)
        cls.organisation1 = api_models.Organisation.objects.create(
            name='Unrax', id=1)
        cls.organisationfleetmanager = api_models.OrganisationFleetManager.objects.create(
            organisation=cls.organisation, fleet_manager=cls.fleetmanager)

    def test_existence_of_OrganisationFleetManager_created(self):

        check_existence = api_models.OrganisationFleetManager.objects.filter(
            organisation=self.organisation).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_OrganisationFleetManager_record(self):

        organisationfleetmanager_store = api_models.OrganisationFleetManager.objects.get(
            organisation=self.organisation)
        organisationfleetmanager_store.organisation = self.organisation1
        organisationfleetmanager_store.save()
        check_existence = api_models.OrganisationFleetManager.objects.filter(
            organisation=self.organisation1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_OrganisationFleetManager(self):

        organisationfleetmanager = api_models.OrganisationFleetManager.objects.get(
            organisation=self.organisation)
        organisationfleetmanager.delete()
        check_existence = api_models.OrganisationFleetManager.objects.filter(
            organisation=self.organisation).exists()
        self.assertFalse(check_existence)


class TestOrganisationDriverModal(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')
        cls.driver = auth_models.Driver.objects.create(
            user=cls.user, id=1)
        cls.organisation = api_models.Organisation.objects.create(
            name='Unra', id=1)
        cls.organisation1 = api_models.Organisation.objects.create(
            name='Unrax', id=1)
        cls.organisationdriver = api_models.OrganisationDriver.objects.create(
            organisation=cls.organisation, driver=cls.driver)

    def test_existence_of_OrganisationDriver_created(self):

        check_existence = api_models.OrganisationDriver.objects.filter(
            organisation=self.organisation).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_OrganisationDriver_record(self):

        organisationdriver_store = api_models.OrganisationDriver.objects.get(
            organisation=self.organisation)
        organisationdriver_store.organisation = self.organisation1
        organisationdriver_store.save()
        check_existence = api_models.OrganisationDriver.objects.filter(
            organisation=self.organisation1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_OrganisationDriver(self):

        organisationdriver = api_models.OrganisationDriver.objects.get(
            organisation=self.organisation)
        organisationdriver.delete()
        check_existence = api_models.OrganisationDriver.objects.filter(
            organisation=self.organisation).exists()
        self.assertFalse(check_existence)


class TestOrganisationVehicleModal(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')
        cls.vehicle = api_models.Vehicle.objects.create(
            type_of_vehicle='range-rover')
        cls.organisation = api_models.Organisation.objects.create(
            name='Unra', id=1)
        cls.organisation1 = api_models.Organisation.objects.create(
            name='Unrax', id=1)
        cls.organisationvehicle = api_models.OrganisationVehicle.objects.create(
            organisation=cls.organisation, vehicle=cls.vehicle)

    def test_existence_of_OrganisationVehicle_created(self):

        check_existence = api_models.OrganisationVehicle.objects.filter(
            organisation=self.organisation).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_OrganisationVehicle_record(self):

        organisationvehicle_store = api_models.OrganisationVehicle.objects.get(
            organisation=self.organisation)
        organisationvehicle_store.organisation = self.organisation1
        organisationvehicle_store.save()
        check_existence = api_models.OrganisationVehicle.objects.filter(
            organisation=self.organisation1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_OrganisationVehicle(self):

        organisationvehicle = api_models.OrganisationVehicle.objects.get(
            organisation=self.organisation)
        organisationvehicle.delete()
        check_existence = api_models.OrganisationVehicle.objects.filter(
            organisation=self.organisation).exists()
        self.assertFalse(check_existence)


class TestProjectModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        project = api_models.Project.objects.create(
            name='projectx', organisation=organisation)

    def test_existence_of_project_created(self):

        check_existence = api_models.Project.objects.filter(
            name='projectx').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_project_record(self):

        project_store = api_models.Project.objects.get(
            name='projectx')
        project_store.name = 'kakira'
        project_store.save()
        check_existence = api_models.Project.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_project_record(self):

        project_store = api_models.Project.objects.get(
            name='projectx')
        project_store.delete()
        check_existence = api_models.Project.objects.filter(
            name='projectx').exists()
        self.assertFalse(check_existence)


class TestStationModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        station = api_models.Station.objects.create(
            name='Stationx', organisation=organisation)

    def test_existence_of_station_created(self):

        check_existence = api_models.Station.objects.filter(
            name='Stationx').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_station_record(self):

        station_store = api_models.Station.objects.get(
            name='Stationx')
        station_store.name = 'kakira'
        station_store.save()
        check_existence = api_models.Station.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_station_record(self):

        station_store = api_models.Station.objects.get(
            name='Stationx')
        station_store.delete()
        check_existence = api_models.Station.objects.filter(
            name='Stationx').exists()
        self.assertFalse(check_existence)


class TestBranchModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        branch = api_models.Branch.objects.create(
            name='Branchx', organisation=organisation)

    def test_existence_of_branch_created(self):

        check_existence = api_models.Branch.objects.filter(
            name='Branchx').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_branch_record(self):

        branch_store = api_models.Branch.objects.get(
            name='Branchx')
        branch_store.name = 'kakira'
        branch_store.save()
        check_existence = api_models.Branch.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_branch_record(self):

        branch_store = api_models.Branch.objects.get(
            name='Branchx')
        branch_store.delete()
        check_existence = api_models.Branch.objects.filter(
            name='Branchx').exists()
        self.assertFalse(check_existence)


class TestDepartmentModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        department = api_models.Department.objects.create(
            name='Departmentx', organisation=organisation)

    def test_existence_of_department_created(self):

        check_existence = api_models.Department.objects.filter(
            name='Departmentx').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_department_record(self):

        department_store = api_models.Department.objects.get(
            name='Departmentx')
        department_store.name = 'kakira'
        department_store.save()
        check_existence = api_models.Department.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_department_record(self):

        department_store = api_models.Department.objects.get(
            name='Departmentx')
        department_store.delete()
        check_existence = api_models.Department.objects.filter(
            name='Departmentx').exists()
        self.assertFalse(check_existence)


class TestDirectorateModal(TestCase):
    def setUp(self):
        organisation = api_models.Organisation.objects.create(
            name='Unra')

        directorate = api_models.Directorate.objects.create(
            name='Directoratex', organisation=organisation)

    def test_existence_of_directorate_created(self):

        check_existence = api_models.Directorate.objects.filter(
            name='Directoratex').exists()
        self.assertEqual(check_existence, True)

    def test_update_of_directorate_record(self):

        directorate_store = api_models.Directorate.objects.get(
            name='Directoratex')
        directorate_store.name = 'kakira'
        directorate_store.save()
        check_existence = api_models.Directorate.objects.filter(
            name='kakira').exists()
        self.assertTrue(check_existence)

    def test_delete_of_directorate_record(self):

        directorate_store = api_models.Directorate.objects.get(
            name='Directoratex')
        directorate_store.delete()
        check_existence = api_models.Directorate.objects.filter(
            name='Directoratex').exists()
        self.assertFalse(check_existence)


class TestBlacklistModal(TestCase):
    def setUp(cls):
        cls.organisation = api_models.Organisation.objects.create(
            name='Unra')

        cls.organisation1 = api_models.Organisation.objects.create(
            name='Unrax')

        cls.blacklist = api_models.Blacklist.objects.create(
            organisation=cls.organisation)

    def test_existence_of_blacklist_created(self):

        check_existence = api_models.Blacklist.objects.filter(
            organisation=self.organisation).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_blacklist_record(self):

        blacklist_store = api_models.Blacklist.objects.get(
            organisation=self.organisation)
        blacklist_store.organisation = self.organisation1
        blacklist_store.save()
        check_existence = api_models.Blacklist.objects.filter(
            organisation=self.organisation1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_blacklist_record(self):

        blacklist_store = api_models.Blacklist.objects.get(
            organisation=self.organisation)
        blacklist_store.delete()
        check_existence = api_models.Blacklist.objects.filter(
            organisation=self.organisation).exists()
        self.assertFalse(check_existence)


class TestPassengerBlacklistModal(TestCase):
    def setUp(cls):
        cls.organisation = api_models.Organisation.objects.create(
            name='Unrax')

        cls.blacklist = api_models.Blacklist.objects.create(
            organisation=cls.organisation)
        cls.blacklist1 = api_models.Blacklist.objects.create(
            organisation=cls.organisation)

        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        cls.passenger = auth_models.Passenger.objects.create(
            user=cls.user)

        cls.passengerblacklist = api_models.PassengerBlacklist.objects.create(
            blacklist=cls.blacklist, passenger=cls.passenger)

    def test_existence_of_passengerblacklist_created(self):

        check_existence = api_models.PassengerBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_passengerblacklist_record(self):

        passengerblacklist = api_models.PassengerBlacklist.objects.get(
            blacklist=self.blacklist)
        passengerblacklist.blacklist = self.blacklist1
        passengerblacklist.save()
        check_existence = api_models.PassengerBlacklist.objects.filter(
            blacklist=self.blacklist1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_passengerblacklist_record(self):

        passengerblacklist = api_models.PassengerBlacklist.objects.get(
            blacklist=self.blacklist)
        passengerblacklist.delete()
        check_existence = api_models.PassengerBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertFalse(check_existence)


class TestDriverBlacklistModal(TestCase):
    def setUp(cls):
        cls.organisation = api_models.Organisation.objects.create(
            name='Unrax')

        cls.blacklist = api_models.Blacklist.objects.create(
            organisation=cls.organisation)
        cls.blacklist1 = api_models.Blacklist.objects.create(
            organisation=cls.organisation)

        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        cls.driver = auth_models.Driver.objects.create(
            user=cls.user)

        cls.driverblacklist = api_models.DriverBlacklist.objects.create(
            blacklist=cls.blacklist, driver=cls.driver)

    def test_existence_of_driverblacklist_created(self):

        check_existence = api_models.DriverBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_driverblacklist_record(self):

        driverblacklist = api_models.DriverBlacklist.objects.get(
            blacklist=self.blacklist)
        driverblacklist.blacklist = self.blacklist1
        driverblacklist.save()
        check_existence = api_models.DriverBlacklist.objects.filter(
            blacklist=self.blacklist1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_driverblacklist_record(self):

        driverblacklist = api_models.DriverBlacklist.objects.get(
            blacklist=self.blacklist)
        driverblacklist.delete()
        check_existence = api_models.DriverBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertFalse(check_existence)


class TestVehicleBlacklistModal(TestCase):
    def setUp(cls):
        cls.organisation = api_models.Organisation.objects.create(
            name='Unrax')

        cls.blacklist = api_models.Blacklist.objects.create(
            organisation=cls.organisation)
        cls.blacklist1 = api_models.Blacklist.objects.create(
            organisation=cls.organisation)

        cls.user = auth_models.User.objects.create(
            first_name='timo', last_name='timo', password='xsxsee2323')

        cls.vehicle = api_models.Vehicle.objects.create(
            type_of_vehicle='range-rover')

        cls.vehicleblacklist = api_models.VehicleBlacklist.objects.create(
            blacklist=cls.blacklist, vehicle=cls.vehicle)

    def test_existence_of_vehicleblacklist_created(self):

        check_existence = api_models.VehicleBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertEqual(check_existence, True)

    def test_update_of_vehicleblacklist_record(self):

        vehicleblacklist = api_models.VehicleBlacklist.objects.get(
            blacklist=self.blacklist)
        vehicleblacklist.blacklist = self.blacklist1
        vehicleblacklist.save()
        check_existence = api_models.VehicleBlacklist.objects.filter(
            blacklist=self.blacklist1).exists()
        self.assertTrue(check_existence)

    def test_delete_of_vehicleblacklist_record(self):

        vehicleblacklist = api_models.VehicleBlacklist.objects.get(
            blacklist=self.blacklist)
        vehicleblacklist.delete()
        check_existence = api_models.VehicleBlacklist.objects.filter(
            blacklist=self.blacklist).exists()
        self.assertFalse(check_existence)
