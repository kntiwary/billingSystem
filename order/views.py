from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from order.models import Item, Order, Customer
from order.serailizer import ItemSerializer, OrderSerializer, CustomerSerializer, OrderDetailSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    @action(detail=True, methods=['GET'])
    def details(self, request, id=None):
        order = self.get_object()
        orders = Order.objects.filter(id=id)
        serializer = OrderDetailSerializer(orders, many=True)
        return Response(serializer.data, status=200)
