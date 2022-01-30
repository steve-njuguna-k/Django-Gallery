from django.test import TestCase
from .models import Image, Category, County

# Create your tests here.
class LocationTestCLass(TestCase):
    #Set up Method
    def setUp(self):
        self.loc = County(name="Kenya")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,County))

    def test_save_method(self):
        self.loc.save_location()
        locations = County.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.delete_location()
        location = County.objects.all()
        self.assertTrue(len(location) == 0)

    def test_update(self):
        location = County.get_location_id(self.loc.id)
        location.update_location('Tanzania')
        location = County.get_location_id(self.loc.id)
        self.assertTrue(location.name == 'Tanzania')