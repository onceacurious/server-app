# Generated by Django 4.1.5 on 2023-01-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_alter_position_display_name_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='nrwvyhvi', max_length=8),
        ),
    ]