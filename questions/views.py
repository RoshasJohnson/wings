from django.shortcuts import render
from.models import Questions
from rest_framework import viewsets
from.serializers import  QuestionSerializer
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.



class QuestionViewSet(viewsets.ModelViewSet):
 
 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()   

    # def list(self,request):
    #     queryset = Questions.objects.all()
    #     print(queryset)
    #     serializer = QuestionSerializer(queryset, many=True)
    #     return Response(serializer.data)


