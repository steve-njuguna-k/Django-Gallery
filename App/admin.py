from django.contrib import admin
from .models import Image, County, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Image) 

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    
admin.site.register(Category, CategoryImportExportModelAdmin)

class CountyResource(resources.ModelResource):
    class Meta:
        model = County

class CountyImportExportModelAdmin(ImportExportModelAdmin):
    resource_class = CountyResource
    
admin.site.register(County, CountyImportExportModelAdmin)