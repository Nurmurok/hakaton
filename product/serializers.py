from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product, Category, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name','description', 'price', 'quantity', 'created_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product']
