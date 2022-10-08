from django.contrib.auth.models import User
from rest_framework import  permissions
from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from product.models import Cart
from .models import Account
from .permissions import AnonPermissionOnly
from .serializers import RegisterSerializer, UpdateSerializer, MyTokenObtainPairSerializer


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # parser_classes = [JSONParser]
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                first_name=request.data['first_name'],
                second_name=request.data['second_name'],
                phone=request.data['phone'],
                is_vendor=request.data['is_vendor']

            )
            account.save()
            cart = Cart.objects.create(
                user=user
            )
            cart.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


