from django.contrib import admin
from .models import Image, Location, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class ImageImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = ImageResource
    
admin.site.register(Image, ImageImportExportModelAdmin)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    
admin.site.register(Category, CategoryImportExportModelAdmin)

class LocationResource(resources.ModelResource):
    class Meta:
        model = Location

class LocationImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = LocationResource
    
admin.site.register(Location, LocationImportExportModelAdmin)