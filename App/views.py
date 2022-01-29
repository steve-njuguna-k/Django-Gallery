from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Image

# Create your views here.
def Home(request):
    images = Image.objects.all()
    return render(request, 'Index.html', {'images':images})

def AllImages(request):
    images = Image.objects.all()
    return render(request, 'All Images.html', {'images':images})