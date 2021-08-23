from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(User):
    pass


class Item(models.Model):
    name = models.CharField(max_length=511, blank=False)
    category = models.CharField(max_length=511)
    created_at = models.DateTimeField(auto_created=True, default=datetime.now())
    active = models.BooleanField(default=False)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_query_name='orderitems')
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    discount = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)


class Order(models.Model):
    paid = models.BooleanField(default=False)
    payment_mode = models.CharField(choices=[('C', 'Cash'), ('U', 'UPI'), ('Crd', 'Card'),
                                             ('I', 'Instamojo')], default='I',
                                    max_length=3)
    payment_part = models.CharField(choices=[('Part', 'Part'), ('Full', 'Full'), ], default='Part',
                                    max_length=4)

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def nettotal(self):
        sum = 0

        sum += self.total+self.gst
        s = round(sum, 2)
        return s

    @property
    def total(self):
        sum = 0
        items = self.ordership_set.all()
        for item in items:
            sum += item.subtotal_price
        s = round(sum, 2)
        return s

    @property
    def gst(self):
        gst_percentage = 25
        gst_value = round((self.total * gst_percentage) / 100, 2)
        return gst_value

    def __str__(self):
        return str(self.id) + ' | ' + str(self.name)


class OrderShip(models.Model):
    item = models.ForeignKey(OrderItem, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)

    @property
    def subtotal_price(self):
        sum = (self.item.price - self.item.discount) * self.quantity
        s = round(sum, 2)
        return s


class Tax(models.Model):
    pass


class Payment(models.Model):
    pass


class Transaction(models.Model):
    pass
