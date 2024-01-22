from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


class ProductView(APIView):

    def get(self, request, pk):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Success',
                'data': serializer.data
            })
        return Response({
            'success': False,
            'message': 'Failed',
            'data': ''
        })

    def put(self, request, pk, *args, **kwargs):
        if pk is not None:
            product = Product.objects.get(pk=pk)
            if product:
                serializer = ProductSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'Success',
                        'data': serializer.data
                    })
        return Response({
            'success': False,
            'message': 'Failed',
            'data': ''
        })

    def delete(self, request, pk, *args, **kwargs):
        if pk is not None:
            product = Product.objects.get(pk=pk)

            if product:
                product.delete()
                return Response({
                    'success': True,
                    'message': 'Success'
                })
        return Response({
            'success': False,
            'Message': 'Failed',
        })
