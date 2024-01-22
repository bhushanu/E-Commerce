from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=1000)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=50, choices=(
        ('Electronics', 'electronics'),
        ('Fashion', 'fashion'),
        ('Home', 'home'),
        ('Stationary', 'stationary'),
        ('Sports', 'sports')
    ))

    def __str__(self):
        return self.name
