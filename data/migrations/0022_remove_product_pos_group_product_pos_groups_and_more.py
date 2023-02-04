# Generated by Django 4.1.5 on 2023-02-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pos_group',
        ),
        migrations.AddField(
            model_name='product',
            name='pos_groups',
            field=models.ManyToManyField(related_name='product_position_group', to='data.position'),
        ),
        migrations.AlterField(
            model_name='positiongroup',
            name='title',
            field=models.CharField(help_text='position group like loan, teller, open account', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, default='iecvfiuh', max_length=8),
        ),
    ]