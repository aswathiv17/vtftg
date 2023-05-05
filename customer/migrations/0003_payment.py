# Generated by Django 4.1.7 on 2023-03-28 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_alter_product_battery_alter_product_price_and_more'),
        ('customer', '0002_alter_cart_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=200)),
                ('acholdername', models.CharField(max_length=100)),
                ('accno', models.IntegerField()),
                ('ifsc', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_payment', to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]