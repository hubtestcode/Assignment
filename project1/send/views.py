from django.shortcuts import render
from django.http import HttpResponse
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def one(request):
    subject = 'Subject'
    html_message = render_to_string('refer_template.html')
    plain_message = strip_tags(html_message)
    from_email = 'dummyabc17@gmail.com'
    to = 'pojened365@syinxun.com'

    mail.send_mail(subject,plain_message,from_email,[to],html_message=html_message)
    return HttpResponse('Mail Sent')
