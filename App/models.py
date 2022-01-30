from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class County(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locations'

class Image(models.Model):
    image = models.ImageField(upload_to='uploads', verbose_name='Image', null=False)
    title = models.CharField(max_length=100, verbose_name='Title', null=False)
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    location = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name='Location')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Images'

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls, id ,image, title , caption, author, category, location):
        update = cls.objects.filter(id = id).update(image = image, title = title ,caption = caption,author = author, category = category, location = location)
        return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls,category):
        images = Image.objects.filter(category=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images_location = cls.objects.filter(location=location)
        return images_location