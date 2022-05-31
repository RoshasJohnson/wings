
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from.utils import get_tokens_for_user


@api_view(['POST'])
def login_view(request):
    User = get_user_model()
    email = request.data.get('email')
    password = request.data.get('password')
    auth = authenticate(email=email, password=password)
    if auth is not None:
        user = User.objects.filter(email=email).first()
        serialized_user = UserSerializer(user).data
        jwt_token = get_tokens_for_user(user)
        response = ({"user": serialized_user,
                    "jwt": jwt_token
                     })
        return Response(response)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListCreate(APIView):
    def get(self, request):
        users = User.objects.filter(is_superuser=False)
        serializer = UserSerializer(users, many=True)
        print(request.user, "-------------------------------------------")
        return Response(serializer.data)

    def post(self, request):
        email = request.data.get("email")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(email = email).first()
            jwt_token = get_tokens_for_user(user)
            response = ({"user": serializer.data,
                         "jwt": jwt_token
                         })

            return Response(response)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class biew(TokenObtainPairView):
