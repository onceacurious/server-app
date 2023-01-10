from django.db import models
from django.contrib.auth.models import AbstractUser


class UserGroup(models.Model):
  display_name = models.CharField(max_length=150, blank=True)
  company_name = models.CharField(max_length=150, blank=True)

  def __str__(self):
    return f'{self.display_name}_{self.company_name}'


class User(AbstractUser):
  company = models.ForeignKey(UserGroup,
                              on_delete=models.CASCADE,
                              related_name="user_company")

  def __str__(self):
    return f'{self.username}-{self.company}'


class Position(models.Model):
  display_name = models.CharField(max_length=150)
  group = models.ForeignKey('data_context.PositionGroup',
                            on_delete=models.CASCADE,
                            related_name="position_group")

  def __str__(self):
    return self.description


class PositionGroup(models.Model):
  title = models.CharField(max_length=150)

  def __str__(self):
    return self.title


class Product(models.Model):
  name = models.CharField(max_length=150)
  pos_group = models.ForeignKey(Position,
                                on_delete=models.CASCADE,
                                related_name="position_group")
  prod_group = models.ForeignKey('data_context.ProductGroup',
                                 on_delete=models.CASCADE,
                                 related_name="product_group")

  def __str__(self):
    return self.name


class ProductGroup(models.Model):
  title = models.CharField(max_length=150)

  def __str__(self):
    return self.title


class Que(models.Model):
  value = models.IntegerField()
  product = models.ForeignKey(Product,
                              on_delete=models.CASCADE,
                              related_name="queued_product")
  called = models.BooleanField(default=False, blank=True)
  called_by = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="user_caller")
  generated_at = models.DateTimeField(auto_now=True, blank=True)
  transaction_date = models.DateTimeField(auto_now_add=True, blank=True)

  @property
  def value_name(self):
    number = str(self.value).zfill(3)
    char = str.lstrip(self.product)[0]
    return f'{char}-{number}'
