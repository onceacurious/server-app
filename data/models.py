from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

class UserLevel(models.Model):
    title = models.CharField(max_length=150, blank=True, unique=True)
    level = models.IntegerField(default=1, blank= True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}:{self.level}'

class UserGroup(models.Model):
    display_name = models.CharField(max_length=150, blank=True)
    company_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.company_name}_{self.display_name}"


class User(AbstractUser):
    password = models.CharField(max_length=8, blank=True, default = ''.join(random.choice(string.ascii_lowercase) for i in range(8)))
    company = models.ForeignKey(
        UserGroup, on_delete=models.CASCADE, related_name="user_company"
    )
    position = models.ForeignKey('data.Position', on_delete=models.CASCADE, related_name="user_position")
    level = models.ForeignKey('data.UserLevel', on_delete=models.CASCADE, related_name="user_level")


    def __str__(self):
        return f"{self.username}-{self.level}:{self.company}"


class Position(models.Model):
    display_name = models.CharField(max_length=150)
    group = models.ForeignKey(
        "data.PositionGroup", on_delete=models.CASCADE, related_name="position_group"
    )

    def __str__(self):
        return self.display_name


class PositionGroup(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=150)
    pos_group = models.ForeignKey(
        'data.PositionGroup', on_delete=models.CASCADE, related_name="product_position_group"
    )
    prod_group = models.ForeignKey(
        "data.ProductGroup", on_delete=models.CASCADE, related_name="product_group"
    )

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Que(models.Model):
    value = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="queued_product"
    )
    is_called = models.BooleanField(default=False, blank=True)
    called_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_caller", null=True
    )
    consumer_level = models.ForeignKey('data.Userlevel', on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True, blank=True)

    @property
    def display_value(self):
        number = str(self.value).zfill(3)
        char = str.lstrip(self.product)[0]
        return f"{char}-{number}"
