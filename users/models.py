
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=200,unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    status  = models.BooleanField(default=True)
    following = models.ManyToManyField("self",symmetrical=False,related_name="followed" ,blank=True)
    bio = models.TextField(blank=True ,default="")
    avatar = models.ImageField(default='default.jpg', upload_to='avatars')
    cover_image = models.ImageField(default='cover.jpg', upload_to='avatars')
    created_at = models.DateTimeField(default=timezone.now)
   

    USERNAME_FIELD = 'email'
    #requred for creating user
    REQUIRED_FIELDS = ['username','avatar']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural="Custom Users"

    def __str__(self):
        return f'{self.username}'

    