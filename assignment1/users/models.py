from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import UserManager




class User(AbstractUser):
    username = None
    mobile = models.CharField( max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField( max_length=50)
    is_Hr = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)
    is_Employee = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()

    REQUIRED_FIELDS = []



class EmployeeReferral(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    dob = models.DateField( auto_now=False, auto_now_add=False)
    email_id = models.EmailField(max_length=254)
    contact = models.CharField(max_length=10)
    address = models.TextField()
    position = models.CharField(max_length=50, choices=(('Fresher','Fresher'),('Developer','Developer'),('Tester','Tester'),('Test Lead','Test Lead'),('Manager','Manager')))
    location = models.CharField( max_length=50, choices=(('Bangalore','Bangalore'),('Noida','Noida'),('Chennai','Chennai'),('Hyderbad','Hyderbad')))
    what_relation = models.CharField( max_length=50)
    experience = models.IntegerField()
    profile_photo = models.ImageField( upload_to = 'profileimage', blank=True)
    resume_upload = models.FileField( upload_to = 'resumedocs', blank=True)

    User = models.ForeignKey(User , on_delete=models.CASCADE)


  ##  To autogenerate tokens (Signalsss)
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)