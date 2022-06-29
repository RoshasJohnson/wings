
from rest_framework import serializers
from.models import Question
from users.serializers import UserSerializer
from answer.models import Answer
from answer.serializers import AnswerSerializer





class QuestionSerializer(serializers.ModelSerializer):
    question  =  serializers.CharField(trim_whitespace=False) 

    # question_type   = QuestionTypeSerialzers(read_only = True)
    # answers_set     = AnswerSerializer(read_only = True,many =True)

    class Meta:
        depth = 1
        model = Question
        fields = ( 
                "id",
                "questioner",
                "question_title",
                "question_topic",
                "question",
                "attached_file",
                "created_at",
                'right_answer'
            
        )

    # def get_answers(self,obj):
    #     try:
    #         return Answer.objects.filter(question = obj)  