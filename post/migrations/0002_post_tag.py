# Generated by Django 4.1.5 on 2023-02-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='post.tag'),
        ),
    ]
