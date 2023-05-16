from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email must be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user



    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=54, unique= True)
    phone_no = models.CharField( max_length=10)
    is_Hr = models.BooleanField(default=False)
    is_Admin = models.BooleanField(default=False)
    is_Employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    objects = UserManager()

    

class Referral(models.Model):
   
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
