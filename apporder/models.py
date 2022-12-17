from django.db import models
from django.contrib.auth.models import User

from appproduct.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    DELIVERED = 'delivered'

    STATUS_CHOICES = (
        (ORDERED, 'ordered'),
        (DELIVERED, 'delivered')
    )

    user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=268)
    last_name = models.CharField(max_length=268)
    email = models.CharField(max_length=268)
    address = models.CharField(max_length=268)
    zipcode = models.CharField(max_length=16)
    place = models.CharField(max_length=268)
    phone = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_intent = models.CharField(max_length=320)
    paid = models.BooleanField(default=False)
    paid_amount = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid_amount:
            return self.paid_amount / 100

        return 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.price / 100


# Create your models here.
