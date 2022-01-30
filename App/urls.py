from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    path('images/all', views.AllImages, name="AllImages"),
    path('image/<str:title>', views.SingleImage, name="SingleImage"),
    path('search', views.Search, name="Search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)