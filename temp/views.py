from django.shortcuts import render

# Create your views here.
from order.models import Order


def index(request):
    context = {}
    context['title'] = 'home'
    context['orders'] = Order.objects.all()
    return render(request, 'temp/index.html', context)


def details(request, id=None):
    context = {}
    context['title'] = 'details'
    context['order'] = Order.objects.get(id=id)
    return render(request, 'temp/details.html', context)
