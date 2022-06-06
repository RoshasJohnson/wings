
from django.utils import timezone
from django.db import models
from topics.models import Topic
from users.models import User


# Create your models here.
class NonStrippingCharField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingCharField, self).formfield(**kwargs)


class Question(models.Model):

    questioner = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.TextField(null=True)
    question_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    question    = models.TextField(null=True)
    attached_file = models.FileField(upload_to='QnA/answers/', null=True)
    created_at = models.DateTimeField(auto_now=timezone.now)
    right_answer = models.IntegerField(null=True,default=0) 

    def __str__(self):
        return f'{self.question_title}'
