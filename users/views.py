
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
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
    print(auth, "------------------------------------------")

    if auth is not None:
        user = User.objects.get(email=email)
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
        return Response(serializer.data)

    def post(self, request):
        email = request.data.get("email")
        username  = request.data.get("username")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(email=email).first()
            jwt_token = get_tokens_for_user(user)
            response = ({"user": serializer.data,
                            "jwt": jwt_token
                            })
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    """
     creating userprofile with given user
    """
    user = request.user
    data = request.data
    f_name = data['Fname']
    l_name = data['Lname']
    profession = data['profession']
    print(data['avatar'],
          '=======================================================')

    bio = data['bio']
    full_name = str(f_name).capitalize() + " " + str(l_name.capitalize())
    topics = data['topics']
    Li_topics = topics.split(",")
    set_Topic = list(set(Li_topics))
    User.objects.filter(username=user).update(fullname=full_name, bio=str(bio), profession=profession.title(
    ), first_name=f_name, last_name=l_name, suggested_topic=[item for item in set_Topic], avatar=request.data["avatar"])
    user = User.objects.filter(username=user)
    serializer_user = UserSerializer(user, many=True)
    return Response(serializer_user.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_profile(request):
    """
    getting my profile
    """
    user = request.user
    user = User.objects.filter(username=user)
    serializer_user = UserSerializer(user, many=True)
    return Response(serializer_user.data)


@api_view(['GET'])
def get_connections(request):
    """c
    getting my onnections
    """
    user = request.user
    user = User.objects.all()
    serializer_user = UserSerializer(user, many=True)
    return Response(serializer_user.data)



