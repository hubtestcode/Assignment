from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *

class loginAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                return Response({
                    'msg':'registration successful',
                    'data':serializer.data,})
            
            return Response({
                'msg':'please entry details',
                'data' :serializer.errors
                })
        except Exception as e:
            print(e)

class Verifyemail(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'msg':'not valid user',
                        'data' : 'invalid email'
                        })
                
                if not user[0].otp == otp:
                    return Response({
                        'msg':'invalid otp',
                        'data' : 'wrong otp'
                    })
                

                user[0].is_verified = True
                user[0].save()
                return Response({
                    'msg' :'account verified',
                    
                })
            return Response({
              'msg':'invalid otp',
              'data' : serializer.errors
            })
        except Exception as e:
            print(e)