from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
