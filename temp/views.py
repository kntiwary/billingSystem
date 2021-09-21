from django.shortcuts import render

# Create your views here.
from order.models import Order


def index(request):
    context = {}
    context['title'] = 'temptesting'
    context['orders'] = Order.objects.all()
    return render(request, 'temp/index.html', context)
