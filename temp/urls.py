from django.contrib import admin
from django.urls import path, include
from temp.views import index, details

urlpatterns = [
    path('', index, name='index_list'),
    path('<int:id>/details/',details , name='index_details')
]