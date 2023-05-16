from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from . models import EmployeeReferral
from . serializers import *




@api_view(['GET'])
def show(request):
    a= EmployeeReferral.objects.all()
    serializer = EmployeeReferralSerializer(a,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = EmployeeReferralSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({'msg':'successfully created'},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@csrf_exempt
@api_view(['POST'])

def login(request):
    email= request.data.get('email')
    password = request.data.get('password')
   
    return Response()