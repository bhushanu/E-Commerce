from django.urls import path, include
from rest_framework import routers
from .views import UserView

urlpatterns = [
    path('', UserView.as_view())
]
