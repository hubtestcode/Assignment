from django.core.mail import send_mail
import random
from django.conf import settings

from .models import *


def send_otp(email):
    subject = 'your verification mail'
    otp = random.randint(1000, 9999)
    message = f'your opt is {otp}'
    from_email = 'dummyabc17@gmail.com'
    to = 'nopixe6639@dekaps.com'
    send_mail(subject, message, from_email, [to] )

    user_obj = User.objects.get(email = email)
    user_obj.otp =otp
    user_obj.save()
    

