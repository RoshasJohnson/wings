
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from questions.models import Question
from users.models import User
from rest_framework import status
from.serializers import AnswerSerializer , VoteSerializer
from.models import Answer , Vote
# Create your views here.


@api_view(['GET'])
def get_answers_of_eachQustions(request, id):
    answers = Answer.objects.filter(question=id,is_report = False ).select_related("respondent")
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

class AnswerListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        pass

    def post(self,request):
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
    
    def put(self,request):
        user  = User.objects.get(id=request.user.id)
        answer_id = request.data['answer']

        answer = Answer.objects.get(id=answer_id)
        if user in answer.vote.all():
            answer.vote.remove(user)
        else:
            answer.vote.add(user)
        answer.save()
        vote_count = answer.vote.count()
        print(vote_count,'===================================')
        return Response(vote_count)

        # return Response(status=status.HTTP_200_OK)


