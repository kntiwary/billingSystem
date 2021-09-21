from django.contrib import admin
from django.urls import path, include
from temp.views import index

urlpatterns = [
    path('', index, name='index_list')
]