from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name="product_group", null=True   )

    def __str__(self):
        return self.name