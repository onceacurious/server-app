# Generated by Django 4.1.5 on 2023-01-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_user_password_alter_usergroup_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='bodfmqfp', max_length=8),
        ),
    ]
