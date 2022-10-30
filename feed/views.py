
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from feed.models import Feed,Comment
from feed.serializers import FeedSerializer,CommentSerializer
from users.models import User
# Create your views here.

class FeedListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        pass

    def post(self,request):
        user = request.user
        data = request.data
        description = data['description']
        image = data['image'] 
        Feed.objects.create(author=user,description=description,post=image)
        return Response(status=status.HTTP_201_CREATED)

    def put(self,request):
        user  = User.objects.get(id=request.user.id)
        post_id = request.data['post_id']
        post = Feed.objects.get(id=post_id)
        if user in post.is_like.all():
            post.is_like.remove(user)
        else:
            post.is_like.add(user)
        post.save()

        like_count = post.is_like.count()
        print(like_count,'===================================')
        return Response(like_count, status=status.HTTP_200_OK)
        # return Response()




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_feeds_by_user(request):
    # try:
        feeds = Feed.objects.all()
        serializers = FeedSerializer(feeds,many = True)
        return Response(serializers.data)
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    

 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comment(request,fk):

        comments = Feed.objects.get(id=fk).parent_comment.all()
        print(comments,'===================================')

        if request.GET.get("search"):
            comments = comments.filter(username=request.GET.get("search", ""))

        serializers = CommentSerializer(comments,many = True)
        return Response(serializers.data)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentListView(APIView):
    """
    comments creating and getting all comments
    """

    permission_classes = (IsAuthenticated,)
    def get(self,request):
        pass

    def post(self,request):
        user = request.user
        data = request.data
        com_body = data['comment']
        feed_id = data['parentPost'] 
        parent  = Feed.objects.get(id=feed_id)  
        Comment.objects.create(username=user,body=com_body,post=parent)
        print("comment created successfully")
        return Response(status=status.HTTP_201_CREATED)