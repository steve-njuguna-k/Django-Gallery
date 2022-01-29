from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
def Home(request):
    return render(request, 'Index.html')