
from rest_framework import serializers

from users.serializers import UserSerializer
from.models import Feed,Comment

class FeedSerializer(serializers.ModelSerializer):
    author= UserSerializer(read_only = True)
    likeCount  = serializers.SerializerMethodField(read_only = True)
    commentCount = serializers.SerializerMethodField(read_only = True)
 

    class Meta:
        model = Feed
        # depth = 1
        fields = "__all__"

    def get_likeCount(self,obj):
        return obj.is_like.count()

    def get_commentCount(self,obj):
        return obj.parent_comment.count()
        





class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)


    class Meta:
        model = Comment
        depth = 1
        fields = "__all__"

        

    
    
