
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):   # AbstractUser is a built-in Django model
    def get_default():
         return str({}) 
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200) 
    fullname = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    bio = models.TextField(blank=True, default="")
    suggested_topic = ArrayField(models.CharField(
        max_length=100), default=get_default)
    follows = models.ManyToManyField(   
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True    
    ) # user who follows this user
    profession = models.CharField(max_length=200, null=True)       
    avatar = models.FileField( upload_to='UserProfile/avatar/',null = True)
    cover_image = models.FileField( upload_to='UserProfile/cover/',null = True)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'    # username field is email
    
    REQUIRED_FIELDS = ['username']  # required fields for user model

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Users"

    def __str__(self):
        return f'{self.username}'



