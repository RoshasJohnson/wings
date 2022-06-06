
from.models import Answer,Vote
from rest_framework import serializers
from users.serializers import UserSerializer

class AnswerSerializer(serializers.ModelSerializer):
    respondent= UserSerializer(read_only = True)
   
    class Meta:
        model = Answer
        fields = "__all__"
        

class VoteSerializer(serializers.ModelSerializer):
    votes_count =serializers.SerializerMethodField()
    

    class Meta:
        model = Vote
        fields = "__all__"
    def get_vote_count(self,obj):
        pass
         