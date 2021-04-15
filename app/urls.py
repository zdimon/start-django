from django.contrib import admin
from django.urls import path
from main.views import index
from main.views import contact
from main.views import about
from main.views import cars
from main.views import food

urlpatterns = [
    path('', index),
    path('index', index),
    path('contact', contact),
    path('about', about),
    path('cars', cars),
    path('food', food),
    path('admin.html', admin.site.urls),
]
