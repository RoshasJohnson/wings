
from.models import Answer ,Vote
from rest_framework import serializers
from users.serializers import UserSerializer

class AnswerSerializer(serializers.ModelSerializer):
    respondent= UserSerializer(read_only = True)
    voteCount = serializers.SerializerMethodField(read_only = True)
   
    class Meta:
        model = Answer
        fields = "__all__"

    def get_voteCount(self,obj):
        return obj.vote.count()




class VoteSerializer(serializers.ModelSerializer):
    # votes =serializers.SerializerMethodField(read_only=True)
    votes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Vote
        fields = [
            'id',
            'voter',
            'answer',
            'vote',
            'votes'
        ]
    # def get_votes(self,obj):
    #     return obj.vote.count()
         
    def get_votes(self,obj):

        return obj.vote.count()