
from django.utils import timezone
from django.db import models
from users.models import User


# Create your models here.


class Questions(models.Model):
    """
        People asks the question and also answered the corresponding question 
        clarifying to other what type of quetion is asked
        A question may ask from science, tech, or social

    """

    questioner    = models.ForeignKey(User,on_delete=models.CASCADE)
    question_type = models.CharField(max_length=200,null=True)
    question      = models.TextField()
    attached_file = models.FileField(default="file.jpg",null=True)
    created_at    = models.DateTimeField(auto_now=timezone.now)
    right_answer  = models.IntegerField(null= True)


    def __str__(self):
        return f'{self.question}'



