from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Image
import random

# Create your views here.
def Home(request):
    images = Image.objects.all()
    return render(request, 'Index.html', {'images':images})

def AllImages(request):
    images = Image.objects.all()
    return render(request, 'All Images.html', {'images':images})

def SingleImage(request, title):
    items = list(Image.objects.all())
    images = random.sample(items, 3)
    image = Image.objects.get(title=title)
    return render(request, 'Single Image.html', {'image':image, 'images':images})