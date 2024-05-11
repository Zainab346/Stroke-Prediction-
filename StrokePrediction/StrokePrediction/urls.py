# StrokePrediction/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stroke/', include('stroke.urls')),
    path('', include('stroke.urls')),  # Add this line for the root path
]