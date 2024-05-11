# stroke/urls.py

from django.urls import path
from .views import bmi, counsel, cta, index, predict, predict_action

urlpatterns = [
    path('', index, name='default'),  # Redirect to index view by default
    path('bmi/', bmi, name='bmi'),
    path('counsel/', counsel, name='counsel'),
    path('cta/', cta, name='cta'),
    path('index/', index, name='index'),
    path('predict/', predict, name='predict'),
    path('predict_action/', predict_action, name='predict_action'),
    
]
