from django.contrib import admin
from django.urls import path
from main.views import index

urlpatterns = [
    path('',index),
    path('contact',index),
    path('about',index),
    path('cars',index),
    path('food',index),
    path('admin', admin.site.urls),
]
