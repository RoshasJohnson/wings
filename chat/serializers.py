from rest_framework import serializers
from.models import Conversation

class ConversationSerializer(serializers.ModelSerializer): 

    # question_type   = QuestionTypeSerialzers(read_only = True)
    # answers_set     = AnswerSerializer(read_only = True,many =True)

    class Meta:
        depth = 1
        model = Conversation
        fields = "__all__"