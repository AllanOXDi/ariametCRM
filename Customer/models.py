from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


class User(AbstractUser):
    pass


class Customer(models.Model):
    """ first_name = models.CharField(max_length=30)\n"
        last_name = models.CharField(max_length=30)\n"
        address = models.CharField(max_length=100)\n"
        phone_number = models.BooleanField(default=False)")
        email = models.EmailField(max_length=100)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Offers(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Transaction(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
