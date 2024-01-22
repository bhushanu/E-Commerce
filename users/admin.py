from django.contrib import admin
from .models import User

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth',
                    'area', 'city', 'pincode', 'phone', 'email')


admin.site.register(User, OrderAdmin)
