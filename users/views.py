from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView




class UserListCreate(APIView):
        def get(self, request):
            users = User.objects.filter(is_superuser = False)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                print("=================================")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
