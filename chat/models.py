from django.db import models

# Create your models here.


class Conversation(models.Model):
    user1 = models.ForeignKey('users.User', related_name="user1", on_delete=models.CASCADE)
    user2 = models.ForeignKey('users.User',related_name="user2", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return f'{self.user1} and {self.user2}'


