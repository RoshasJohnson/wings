

from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.contrib.auth.password_validation import validate_password
from.models import User





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = "__all__"


    def create(self, data):
        user = User.objects.create(
            email=data['email'],
            username=data['username'],
    
        )
        user.set_password(data['password'])
        user.save()

        return user
    def get(self):
        user =  self.request.user
        print(user,"---------------------------------------------------------")






