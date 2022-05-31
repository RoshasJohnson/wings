from django.db import models
# from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Topic(models.Model):
    
    def get_default():
        return ""
    topics  =  models.CharField(max_length=100,default="")
    def __str__(self):
        
        return str(self.topics)


