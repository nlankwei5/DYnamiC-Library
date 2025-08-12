from django.urls import path 
from .views import *
from django.conf import settings
from django.conf.urls.static import static


url_patterns=[
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')), 

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


