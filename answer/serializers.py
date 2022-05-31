
from.models import Answer,Replay_Answer
from rest_framework import serializers
from users.serializers import UserSerializer

class AnswerSerializer(serializers.ModelSerializer):
    respondent= UserSerializer(read_only = True)
   
    class Meta:
        model = Answer
        fields = "__all__"
        

class ReplayAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replay_Answer
        fields = "__all__"
  