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

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.cat.id)
        category.update_category('Travel')
        category = Category.get_category_id(self.cat.id)
        self.assertTrue(category.name == 'Travel')