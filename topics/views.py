
from rest_framework.decorators import api_view
from.models import Topic
from.serializers import TopicSerialzers
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST'])
def get_all_topics(request):
     if request.method == 'GET':
         data  = Topic.objects.all()
         topics =  TopicSerialzers(data,many = True)
         return  Response ({
             "topics":topics.data
         }) 