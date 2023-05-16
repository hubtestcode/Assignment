from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import  User
from .manager import *



class User(AbstractUser):
    username = None
    email = models.CharField( max_length=50, unique= True)
    is_verified = models.BooleanField(default= False)
    otp = models.CharField(max_length=5)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    objects = UserManager()


class Verify(models.Model):
        email = models.CharField( max_length=50)
        otp = models.CharField(max_length=5)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)