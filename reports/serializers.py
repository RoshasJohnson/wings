from rest_framework import serializers
from.models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        
        depth = 1
        model = Report
        fields ="__all__"
        
