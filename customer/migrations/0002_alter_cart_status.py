# Generated by Django 4.1.7 on 2023-03-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='carted', max_length=100),
        ),
    ]
