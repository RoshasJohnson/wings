
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
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
    )    
    avatar = models.ImageField(default='', upload_to='UserProfile/avatar/')
    cover_image = models.ImageField(default="", upload_to='UserProfile/cover/')
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # requred for creating user
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Users"

    def __str__(self):
        return f'{self.username}'


# class Profile(models.Model):
#     def get_default():
#         return str("")

   
#     suggested_topic = ArrayField(models.CharField(
#         max_length=100), default=get_default)
#     follows = models.ManyToManyField(
#         "self",
#         related_name="followed_by",
#         symmetrical=False,
#         blank=True    
#     )    

#     def __str__(self):
#         return self.user.username
