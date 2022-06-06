from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from urllib import response
from django.shortcuts import render
from questions.models import Question
from users.models import User
from rest_framework import status
from.serializers import AnswerSerializer
from.models import Answer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.




@api_view(['GET'])
def get_answers_of_eachQustions(request, id):
    answers = Answer.objects.filter(question=id).select_related("respondent")
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_new_answer(request):
    user = request.user
    data = request.data
    que_id = data['question']
    answer = data['answer']
    image = data['image']
    username = User.objects.get(username=user)
    question = Question.objects.get(id=que_id)
    Answer.objects.create(respondent=username, question=question,
                          answer=answer, attached_file=image)

    return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def vote_answer(ruquest):
    pass