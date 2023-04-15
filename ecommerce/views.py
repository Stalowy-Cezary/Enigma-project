from django.shortcuts import render
from rest_framework import viewsets, filters
# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import permissions
from .models import Product, ProductCategory, Order, OrderItems
from .serializers import UserSerializer, ProductSerializer, ProductCategorySerializer, OrderSerializer, OrderItemsSerializer
from .permissions import IsSellerOrReadOnly

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = []

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSellerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'category', 'price']
    search_fields = ['name','description', 'price', 'category__cat']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsSellerOrReadOnly]

    def perform_create(self, serializer, order=None):
        serializer.save(owner=self.request.user)
#TODO full price
class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = []

