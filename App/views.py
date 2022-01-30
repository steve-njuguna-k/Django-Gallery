from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Category, Image
import random

# Create your views here.
def Home(request):
    items = list(Image.objects.all())
    images = random.sample(items, 9)
    return render(request, 'Index.html', {'images':images})

def AllImages(request):
    images = Image.objects.all()
    return render(request, 'All Images.html', {'images':images})

def SingleImage(request, title):
    items = list(Image.objects.all())
    images = random.sample(items, 3)
    image = Image.objects.get(title=title)
    return render(request, 'Single Image.html', {'image':image, 'images':images})

def Search(request):
    if request.method == 'POST':
        search = request.POST['imageSearch']
        images = Image.objects.filter(title__contains = search).all()
        categories = Category.objects.filter(name__contains = search).all()
        return render(request, 'Search Results.html', {'search':search, 'images':images, 'categories':categories})
    else:
        return render(request, 'Search Results.html')