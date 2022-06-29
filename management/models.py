
from django.db import models

# Create your models here.

class Management(models.Model):
    """
    managing the question and answer
    and feeds of the users from get report 
    """

    reporter = models.ForeignKey('users.User', on_delete=models.CASCADE)
    accused_peron  = models.ForeignKey('users.User', on_delete=models.CASCADE)
    accesed_content = models.IntegerField(null= True)
    accesed_type    = models.CharField(max_length=20)
    accused_reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_accepted = models.BooleanField(default=False, null=True)
    is_rejected = models.BooleanField(default=False, null=True)
    is_ignored = models.BooleanField(default=False, null=True)
    report_limit = models.IntegerField(default=0, null=True)


    
