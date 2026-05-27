from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.



class Login_data(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Customer(models.Model):
    user = models.OneToOneField(Login_data, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.TextField(max_length=100)


class seller(models.Model):
    user = models.OneToOneField(Login_data, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()


class Product(models.Model):
    user = models.ForeignKey(seller, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()