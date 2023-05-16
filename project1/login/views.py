from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def post(request):
    serializer =ReferralSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data= serializer.data, status= status.HTTP_201_CREATED )
    return Response(data=serializer.errors, status= status. HTTP_400_BAD_REQUEST)

