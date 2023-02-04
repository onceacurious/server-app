from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    tag = models.ManyToManyField(Tag, related_name="tag", blank=True)

    def __str__(self):
        return self.title
