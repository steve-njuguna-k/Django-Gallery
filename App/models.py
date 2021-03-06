from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locations'

class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100, verbose_name='Title', null=False)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Location')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, title, caption, author, category, location):
        update = cls.objects.filter(id = id).update(title = title , caption = caption, author = author, category = category, location = location)
        return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_category(cls,category):
        images = Image.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images_location = cls.objects.filter(location__id=location)
        return images_location

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Images'