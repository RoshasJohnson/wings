from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from users.utils import get_tokens_for_user
from rest_framework.decorators import api_view, permission_classes
from questions.models import Question

@api_view(['POST'])
def Admin_login_view (request):
    data = request.data
    email =data['email']
    password = data['password']
    auth = authenticate(email=email, password=password)
    if auth is not None:
        user = User.objects.get(email=email)
        if user.is_superuser:
            serialized_user = UserSerializer(user).data
            jwt_token = get_tokens_for_user(user)
            response = ({"user": serialized_user,
                        "jwt": jwt_token
                        })
        return Response(response)

    return Response(status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_admin(self,user):
        if user.is_superuser:
            return True
        return False



    def get(self, request):
        user = User.objects.get(id = request.user.id)
        if self.get_admin(user):
        
            users  = User.objects.all()
            serialized_users = UserSerializer(users, many=True).data
            return Response(serialized_users)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,pk):
        user = User.objects.get(id = request.user.id)
        if self.get_admin(user):
            user = User.objects.get(id=pk)
            user.status = not user.status
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    

    def delete(self,request,pk):
        user = User.objects.get(id = request.user.id)
        if self.get_admin(user):
            user = User.objects.get(id=pk)
            user.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


 
@api_view(['GET'])
def get_statistics(request):
    users = User.objects.all()
    users_count = users.count()
    users_active = users.filter(status=True).count()
    users_inactive = users.filter(status=False).count()
    question = Question.objects.all()
    question_count = question.count()
    # question_active = question.filter(status=True).count()
    # question_inactive = question.filter(status=False).count()
    response = {
        "users_count": users_count,
        "users_active": users_active,
        "users_inactive": users_inactive,
        "question_count": question_count,
        # "question_active": question_active,
        # "question_inactive": question_inactive
    }
    return Response(response)



    


