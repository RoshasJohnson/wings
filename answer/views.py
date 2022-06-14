from django.db.models import Case, Value, When
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



@api_view(['POST'])
def vote_answer(request, fk):
    user =User.objects.get(username = request.user)
    ans_id = Answer.objects.get(id=fk)
    if  Vote.objects.filter(voter=user, answer=ans_id).exists():
        vote_obj =  Vote.objects.get(voter=user, answer=ans_id)
        vote_obj.vote = not vote_obj.vote
        vote_obj.save()    

    else:
        Vote.objects.create(voter=user, answer=ans_id, vote=True,vote_count =+1)
    vote_data = Vote.objects.filter(voter  = user ,answer = ans_id)
    # serialzers = VoteSerializer(vote_data,many = True)

    # return Response({'data':serialzers.data})
    return Response("ok")

@api_view(['GET'])
def vote_answer_status(request,fk):

    # try:
        answer   = Answer.objects.filter(question  =fk)
        totalVots = Vote.objects.filter(answer__id__in = answer,vote = True)
        vote_count = totalVots.count()
        print(vote_count,'------------------')
        serializers = VoteSerializer(totalVots,many = True)
        return Response({
        "TotalVotes":serializers.data })
    # except:
        # return Response(status=status.HTTP_404_NOT_FOUND)  # 404