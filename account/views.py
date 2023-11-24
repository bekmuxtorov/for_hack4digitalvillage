from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import AccountRegisterSerializers
from .models import Account
from rest_framework.authtoken.models import Token


class AccountRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializers_class = AccountRegisterSerializers

    def post(self, request, format=None):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token = Token.objects.get_or_create(user=user)[0].key()
            request_data = {
                'token': token,
                'user': serializer.data
            }
            return Response(request_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if user:
            user_data = {
                'id': user.id,
                'full_name': user.full_name,
                'farm_name': user.farm_name,
                'phone_number': user.phone_number,
                'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
            }

            return Response(user_data)
        return Response({'error': 'Invalid credentials'}, status=400)
