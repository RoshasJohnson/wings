
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from users.models import User
from topics.models import Topic
from rest_framework.permissions import IsAuthenticated, AllowAny
from answer.serializers import AnswerSerializer
from answer.models import Answer
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Question
from.serializers import QuestionSerializer
# Create your views here.
from django.core.paginator import Paginator


class QuestionView(APIView):
    """
    List all questions, or create a new question.
    """
    permission_classes = [AllowAny]

    def get(self, request):
       
        user = request.user
        # try:
        if user:
            """
            If user is exist giving question based on user's favourite topics
            ,Or user is guest giving all latest questions 
            """
            user_topics = User.objects.get(username=user)

            topics_id = []
            for i in user_topics.suggested_topic:
                id = Topic.objects.get(topics=i)
                topics_id.append(id.id)
            questions = Question.objects.filter(
                question_topic__in=  topics_id)
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        # except:
        questions = Question.objects.all()


        per_page = request.GET.get("per_page", 10)
        page = request.GET.get("page", 1)
        paginator = Paginator(questions, per_page)
        page_obj = paginator.get_page(page)

        serializer = QuestionSerializer(page_obj.object_list, many=True)
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
        question = self.get_object(pk)
        answers = self.get_answers(pk)
        ans_serializers = AnswerSerializer(answers, many=True)
        serializer = QuestionSerializer(question)
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


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_question(request):
    """
    creating new a new question
    """
    # try:
    req_user = request.user
    data = request.data
    title = data['question_title']
    question = data['question']
    q_topic = data['topic']
    image = data['image']
    print(image,"==========================")
    user = User.objects.get(username=req_user)
    topic = Topic.objects.get(topics=q_topic)
    print(title)
    print(user.id)
    Question.objects.create(questioner=user, question_title=title,
                            question_topic=topic, question=question, attached_file=image)
    return Response(status=status.HTTP_201_CREATED)
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def topic_wise(request,fk):
    questions_topic_wise = Question.objects.filter(question_topic = fk)
    serializers = QuestionSerializer(questions_topic_wise,many = True)
    return Response({
        "topicWise":serializers.data
    })


@api_view(['GET'])
def my_question(request):
    user = User.objects.get(username = request.user)
    get_myquestions  = Question.objects.filter(questioner = user).order_by("-id")
    serializers      = QuestionSerializer(get_myquestions,many = True)
    return Response({
        "MyQuestions":serializers.data
    })

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def got_answer(request):
    user  =request.user
    data= request.data
    print(request.data,"=================")
    queId = data['question']
    ansId = data['answer']
    question = Question.objects.get(questioner = user,id = queId)
    question.right_answer = ansId
    question.save()
    return Response(status=status.HTTP_200_OK)