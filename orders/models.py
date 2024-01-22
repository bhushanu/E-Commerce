from django.db import models
from products.models import Product
from users.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=(
        ('Placed', 'placed'),
        ('Confirmed', 'confirmed'),
        ('Shipped', 'shipped'),
        ('In Transit', 'in transit'),
        ('Out For Delivery', 'out for delivery'),
        ('Delivered', 'delivered')
    ))

    def __str__(self):
        return str(self.product)
