# Generated by Django 4.1.5 on 2023-02-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_product_description_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='bpivhrbg', max_length=8),
        ),
    ]
