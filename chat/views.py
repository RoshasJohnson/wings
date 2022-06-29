
from rest_framework.response import Response
from chat.models import Conversation
from users.models import User
from.serializers import ConversationSerializer
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_chats(request):
    chats  = Conversation.objects.filter(Q(user1 = request.user.id)|Q(user2 = request.user.id))
    
    print(request.user,'==========================')
    serailzers= ConversationSerializer(chats, many = True)
    return Response(serailzers.data)
