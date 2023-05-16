
from django.urls import path
from .views import *

urlpatterns = [
    path('login', loginAPI.as_view()),
    path('verify', Verifyemail.as_view())
]
