from django.db import models

from users.models import User

# Create your models here.


class notifications(models.Model):
    user_sender = models.ForeignKey(
    User, null=True, blank=True, related_name='user_sender', on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(
    User, null=True, blank=True, related_name='user_revoker', on_delete=models.CASCADE)
    status = models.CharField(max_length=264, null=True,
                            blank=True, default="unread")
    type_of_notification = models.CharField(max_length=264, null=True, blank=True)

    def __str__(self):
        return f'{self.user_sender} to  {self.user_revoker}'