from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response


class UserView(APIView):

    def get(self, request, pk):
        if pk is not None:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response({
                'success': True,
                'message': 'Success',
                'data': serializer.data
            })

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'message': 'Success'
            })

        return Response({
            'success': False,
            'message': 'Failed',
        })

    def put(self, request, pk, *args, **kwargs):
        if pk is not None:
            user = User.objects.get(pk=pk)
            if user:
                serializer = UserSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success': True,
                        'message': 'Success',
                        'data': serializer.data
                    })

        return Response({
            'success': False,
            'message': 'Failed'
        })

    def delete(self, request, pk, *args, **kwargs):
        if pk is not None:
            user = User.objects.get(pk=pk)
            if user:
                user.delete()
                return Response({
                    'success': True,
                    'message': 'Success'
                })

        return Response({
            'Success': False,
            'message': 'Failed'
        })
