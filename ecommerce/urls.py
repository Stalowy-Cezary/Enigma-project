from django.urls import path
from rest_framework.routers import DefaultRouter
from ecommerce import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'categories', views.ProductCategoryViewSet, basename='productcategory')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register('order-items', views.OrderItemsViewSet, basename='orderitems')