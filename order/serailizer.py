from django.db import transaction
from rest_framework import serializers

from order.models import Item, Order, Customer, OrderShip, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        # exclude = ('created_at',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = '__all__'
        exclude = ('created_at',)


class OrderShipSerializer(serializers.ModelSerializer):
    item = serializers.IntegerField(source='OrderItem.item_id', write_only=True)
    price = serializers.DecimalField(source='OrderItem.price', decimal_places=2, max_digits=5, write_only=True)
    discount = serializers.DecimalField(source='OrderItem.price', decimal_places=2, max_digits=5, write_only=True)

    class Meta:
        model = OrderShip
        fields = (
            'item',
            'discount',
            'price',
            'quantity'
        )
        # exclude = ('paid',)


class OrderSerializer(serializers.ModelSerializer):
    orders = OrderShipSerializer(source='ordership_set', many=True, required=False, write_only=True)

    class Meta:
        model = Order
        # fields = ('total', 'id', 'paid', 'payment_mode', 'orders')
        exclude = ('paid', 'created_at')

    @transaction.atomic
    def create(self, validated_data):
        try:
            order_items = validated_data.pop('ordership_set')
        except Exception as e:
            print(e)
        order = Order.objects.create(**validated_data)
        for _ in order_items:
            cur_item = _['OrderItem']
            order_item = OrderItem.objects.create(**cur_item)
            OrderShip.objects.create(item=order_item, order=order)

        return order

    def to_representation(self, instance):
        data = super(OrderSerializer, self).to_representation(instance)
        return data


class OrderShipDetailSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OrderShip
        fields = (
            'item',
            'quantity',
            'item_name',
            'subtotal_price'
        )
        depth = 1

    def get_item_name(self, queryset):
        return queryset.item.item.name


class OrderDetailSerializer(serializers.ModelSerializer):
    orders = OrderShipDetailSerializer(source='ordership_set', many=True, )

    class Meta:
        model = Order
        fields = ('id', 'paid', 'payment_mode', 'orders', 'total', 'gst', 'nettotal')

        depth = 1


# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'
#
#
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#
#
