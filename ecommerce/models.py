from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    modyfikacja defaultowego usera, dodaje pole "role" do wyboru
    """
    ROLES = [
        ('sprzedawca', 'sprzedawca'),
        ('klient', 'klient'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='klient')

class ProductCategory(models.Model):
    cat = models.CharField(max_length=40)

    def __str__(self):
        return self.cat

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #address = models.ForeignKey('Address', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_items = models.ManyToManyField('OrderItems')
    #payment_deadline = models.DateTimeField()

    def __str__(self):
        return str(self.owner)

class OrderItems(models.Model):
    """
    oddzielny model dla produktow z koszyka pozwala na wprowadzenie dodatkowych modyfikacjji, tj. ilosc
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Address(models.Model):
    street = models.CharField(max_length=40)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=40)




