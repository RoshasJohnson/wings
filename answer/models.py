from xml.parsers.expat import model
from django.db import models
from users.models import User
from questions.models import Question



class Answer(models.Model):
    """
    People  answer the question  
    """
    respondent    = models.ForeignKey(User,on_delete=models.CASCADE)
    question      = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer        = models.TextField()
    attached_file = models.FileField(default="file.jpg",null=True)
    vote          = models.IntegerField(default= 0)
    """
    people  vote the corresponding answer which questioner asked 
    """
    def __str__(self):
        return str(self.answer)



class Replay_Answer(models.Model):
    """
    people  reply the answer
    """
    replier       =  models.ForeignKey(User,on_delete=models.CASCADE) 
    reply_answer  =  models.ForeignKey(Answer, on_delete=models.CASCADE)
    reply         =  models.TextField(null=True)
    attached_files=  models.FileField(default="file.jpg",null=True)
    
    def __str__(self):
        return str(self.reply)

