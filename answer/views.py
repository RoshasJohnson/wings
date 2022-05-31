from urllib import response
from django.shortcuts import render


from.serializers import AnswerSerializer ,ReplayAnswerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from.models import Answer,Replay_Answer
# Create your views here.


# class AnswerViewSet(viewsets.ModelViewSet):
 
 
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = AnswerSerializer
#     queryset = Answer.objects.all()     




# class  Replay_AnswerViewSet(viewsets.ModelViewSet):

    
#     serializer_class = ReplayAnswerSerializer
#     queryset = Replay_Answer.objects.all()   
@api_view(['GET'])
def get_answers_of_eachQustions(request,id):
    answers  = Answer.objects.filter(question =id ).select_related("respondent")
    serializer = AnswerSerializer(answers,many = True)


    return Response(serializer.data)
  
    



