# Generated by Django 4.1.5 on 2023-01-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='sejvafvi', max_length=8),
        ),
    ]
