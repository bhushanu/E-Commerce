from django.shortcuts import render
from .models import Order, Product
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class OrderView(APIView):

    def get(self, request, pk):

        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response({
            'suceess': True,
            'message': 'Success',
            'data': serializer.data
        })

    def post(self, request):

        product = Product.objects.get(request.data.get('product.id'))
