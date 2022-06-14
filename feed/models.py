from django.db import models
from django.utils import timezone 
from users.models import User
from django.urls import reverse 

# Create your models here.


    # is_dislike = models.BooleanField(default=False,null=True)


class Feed(models.Model):
    description = models.TextField()
    post        = models.FileField(null=True ,upload_to='feed/')
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like     = models.ManyToManyField(User, related_name="LikedUser")
    created_at  = models.DateTimeField(default=timezone.now)
    
            
    class Meta:
        ordering     = ['-created_at'] # - means descending order
        verbose_name = ("Feeds") # verbose name for admin panel
        verbose_name_plural = ("Feeds") # verbose name for admin panel

    def __str__(self): # __str__ method is used to return a string representation of the object
        return str(self.description)

    def get_absolute_url(self):
        return reverse("feed:detail", kwargs={"pk": self.pk})



class Comment(models.Model):
    body       =  models.TextField()
    post       =  models.ForeignKey(Feed,related_name="parent_comment", on_delete=models.CASCADE, null=True) # parent tweet
    username   =  models.ForeignKey(User, on_delete=models.CASCADE) # user who commented
    created_at =  models.DateTimeField(default=timezone.now) # time when comment was created
    edited_at  =  models.DateTimeField(default=timezone.now)    # time when comment was edited
    is_edited  =  models.BooleanField(default=False, blank=True, null=True) # is comment edited

    class Meta:
        ordering     = ['-created_at']
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return str(self.body)

    def get_absolute_url(self):
        return reverse("feed:detail", kwargs={"pk": self.pk})

    

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Feed,on_delete=models.CASCADE, null=True)
    is_like = models.BooleanField(default=False)