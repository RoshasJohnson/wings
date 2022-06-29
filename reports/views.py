
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from reports.serializers import ReportSerializer
from users.models import User
from.models import Report
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from users.utils import get_tokens_for_user
from rest_framework.decorators import api_view, permission_classes
from questions.models import Question
from answer.models import Answer

# Create your views here.

@api_view(['POST'])
def report_item(request):
    data = request.data
    reported_item = data['reported_item']
    report_item_id = data['report_item_id']
    reason = data['reason']
    user = User.objects.filter(id=request.user.id)
    if Report.objects.filter(reported_item=reported_item,reported_item_id =report_item_id ).exists():
        item =  Report.objects.get(reported_item=reported_item,reported_item_id =report_item_id )
        if item.report_count > 3:
            answer = Answer.objects.get(id = report_item_id)
            answer.is_report = True
        else:    
            item.report_count  +=1
            print(item.report_count)
            item.save()
    else:
        Report.objects.create(reported_item =reported_item, reported_item_id = report_item_id,reporter = request.user ,report_count =1,report_reason = reason)
    return Response(status=status.HTTP_200_OK)  

class ReportVIew(APIView):

    def get(self,request):
        item = Report.objects.all()
        serializers = ReportSerializer(item,many = True)
        return Response(serializers.data)