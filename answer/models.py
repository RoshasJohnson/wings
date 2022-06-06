from xml.parsers.expat import model
from django.db import models
from users.models import User
from questions.models import Question
from django.utils import timezone

class Answer(models.Model):
    """
    People  answer the question  
    """
    respondent = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    attached_file = models.FileField(upload_to='QnA/answers/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_edited = models.BooleanField(default=False, null=True)
    """
    people  vote the corresponding answer which questioner asked 
    """

    def __str__(self):
        return str(self.answer)



class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    vote = models.IntegerField(default=0,null= True)