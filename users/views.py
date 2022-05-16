
from email.policy import HTTP
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated,AllowAny
from rest_framework.response import  Response
from rest_framework import status



class UsersList(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context 




class UserList(APIView):
    """
    List all users, or create a new users.
    """
    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    permission_classes= [AllowAny]

    def post(self,request):
        data = request.data
        seriliazer = UserSerializer(data=request.data)
        if seriliazer.is_valid():
            new_user = seriliazer.save()
            if new_user:
                return Response (status=status.HTTP_201_CREATED)
        return Response(seriliazer.errors,status=status.HTTP_400_BAD_REQUEST) 
