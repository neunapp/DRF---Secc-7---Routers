from django.shortcuts import render
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class LoginUserView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # login
        user = authenticate(email=email, password=password)
        #
        if user is not None and user.is_active:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            #
            exipired = timezone.now() + timedelta(minutes=3)
            user.token_expired = exipired
            user.save()
            return Response({'Token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'Erorr': 'credenciales no validas'}, status=status.HTTP_401_UNAUTHORIZED)