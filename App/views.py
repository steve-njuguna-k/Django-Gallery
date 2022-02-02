from unicodedata import category
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Category, Image
import random

# Create your views here.
def Home(request):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    items = list(Image.objects.all())
    images = random.sample(items, 9)
    return render(request, 'Index.html', {'images':images, 'trendingcategories':trendingcategories})

def AllImages(request):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    images = Image.objects.all()
    return render(request, 'All Images.html', {'images':images, 'trendingcategories':trendingcategories})

def AllCategories(request):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    categories = Category.objects.all()
    return render(request, 'Categories.html', {'categories':categories, 'trendingcategories':trendingcategories})

def SingleImage(request, title):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    items = list(Image.objects.all())
    images = random.sample(items, 3)
    image = Image.objects.get(title=title)
    return render(request, 'Single Image.html', {'image':image, 'images':images, 'trendingcategories':trendingcategories})

def Search(request):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    if request.method == 'POST':
        search = request.POST['imageSearch']
        images = Image.objects.filter(title__icontains = search).all()
        categories = Category.objects.filter(name__icontains = search).all()
        return render(request, 'Search Results.html', {'search':search, 'images':images, 'categories':categories, 'trendingcategories':trendingcategories})
    else:
        return render(request, 'Search Results.html', {'trendingcategories':trendingcategories})

def ImagesInCategory(request, id):
    trending = list(Category.objects.all())
    trendingcategories = random.sample(trending, 15)
    category = Category.objects.get(id=id)
    images = Image.objects.filter(category=id).all()
    return render(request, 'Category Images.html', {'images':images, 'category':category, 'trendingcategories':trendingcategories})