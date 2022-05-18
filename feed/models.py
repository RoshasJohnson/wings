from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.


    # is_dislike = models.BooleanField(default=False,null=True)


class Feed(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    post        = models.FileField(null=True)
    author      = models.ForeignKey(User,on_delete=models.CASCADE)
    is_like     = models.ForeignKey("Like",on_delete=models.CASCADE )
    is_dislike  = models.ForeignKey("Like",related_name='dislikes',on_delete=models.CASCADE)
    created_at  = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering     = ['-created_at']
        verbose_name = ("Feeds")
        verbose_name_plural = ("Feeds")

    def __str__(self):
        return str(self.title)



class Comment(models.Model):
    body       =  models.TextField()
    post       =  models.ForeignKey(Feed,  related_name="parent_tweet", on_delete=models.CASCADE, null=True)
    username   =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(default=timezone.now)
    edited_at  =  models.DateTimeField(default=timezone.now)
    is_edited  =  models.BooleanField(default=False, blank=True, null=True)




class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Feed,on_delete=models.CASCADE, null=True)
    is_like = models.BooleanField(default=False)