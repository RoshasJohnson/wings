from users.models import Profile, User
from topics.models import Topic
from rest_framework.permissions import IsAuthenticated
from answer.serializers import AnswerSerializer
from answer.models import Answer
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from.models import Question
from.serializers import QuestionSerializer
# Create your views here.


class QuestionView(APIView):
    """
    List all questions, or create a new question.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            if user:
                """
                If user is exist giving question based on user's favourite topics
                ,Or user is guest giving all latest questions 
                """
                user_topics = Profile.objects.filter(user=user)
                topics_id = []
                for i in user_topics:
                    for j in range(len(i.suggested_topic)):
                        id = Topic.objects.get(topics=i.suggested_topic[j])
                        topics_id.append(id.id)
                        
                    questions = Question.objects.filter(
                        question_topic__in=topics_id)
                    serializer = QuestionSerializer(questions, many=True)
                    return Response(serializer.data)
        except:
            questions = Question.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)

    def post(self, request):
        pass


class QuestionDetails(APIView):
    """
       Retrieve, update or delete a specific question  instance.

    """

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_answers(self, pk):
        try:
            return Answer.objects.filter(question=pk)

        except Answer.DoesNotExist:
            return Response("No answers founded")

    def get(self, request, pk):
        print("=================================================")
        question = self.get_object(pk)
        answers = self.get_answers(pk)
        ans_serializers = AnswerSerializer(answers, many=True)
        serializer = QuestionSerializer(question)
        print("answers", answers,
              "tttttttttsdddddfaaaaaaaaaaaaaaaaaaaaaaaaaatttttttttttttttttttttttttttttttttttttttttttttttttt")

        return Response({
            "question": serializer.data,
            "answers": ans_serializers.data
        })

    # def put(self,request ):
    #     serializer = QuestionSerializer(question, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
