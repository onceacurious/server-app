from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  company = models.ForeignKey(UserGroup,
                              on_delete=models.CASCADE,
                              related_name="user_company")

  def __str__(self):
    return f'{self.username}-{self.company}'


class UserGroup(models.Model):
  display_name = models.CharField(max_length=150, blank=True)
  company_name = models.CharField(max_length=150, blank=True)

  def __str__(self):
    return f'{self.display_name}_{self.company_name}'


class Position(models.Model):
  description = models.CharField(max_length=150)
  group = models.ForeignField(PositionGroup,
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

  def __str__(self):
    return self.name


class ProductGroup(models.Model):
  title = models.CharField(max_length=150)

  def __str__(self):
    return self.title


class Que(models.Model):
  target_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

  @property
  def value(self):
    return self.target_group.count()
