from rest_framework import serializers, viewsets
from .models import Product, ProductCategory, Order, OrderItems
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['cat']
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'category']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = ['owner', 'total_price', 'order_items']

class OrderItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['product', 'quantity']