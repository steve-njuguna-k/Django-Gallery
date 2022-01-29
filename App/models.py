from sre_parse import CATEGORIES
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
        verbose_name_plural = 'Counties'

class Image(models.Model):
    caption = models.CharField(max_length=2200, verbose_name='Caption', null=False)
    image = models.ImageField(upload_to='Uploads', default='', verbose_name='Post Image', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    county = models.ForeignKey(County, on_delete=models.CASCADE, verbose_name='County')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date Updated')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'Images'