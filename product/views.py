from django.contrib.auth.models import User
from django.db.migrations import serializer
from django.http import Http404

from rest_framework.parsers import JSONParser
from django.db.models import Q
from rest_framework.response import Response


from .models import Product, Category,Cart
from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializer, CartSerializer
from rest_framework import permissions, status, pagination, viewsets, generics, filters
from django.core.paginator import Paginator

class ProductListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,request):
        products=Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CartCreateAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self,request):
#         serializer=CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetCartAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]
    def get(self,request,id):
        cart=Cart.objects.get(user_id=id)
        product=cart.product.all()
        serializer2=ProductSerializer(product, many=True)
        serializer=CartSerializer(cart)
        data=serializer.data
        data['product']=serializer2.data

        return Response(data)

# class UpdateCart(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def get_object(self, id):
#         try:
#             return Product.objects.get(id=id)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def put(self, requests, id):
#         product = self.get_object(id)
#         serializer = ProductSerializer(product, data=requests.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)