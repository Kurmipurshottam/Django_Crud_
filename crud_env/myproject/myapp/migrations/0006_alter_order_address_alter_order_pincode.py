# Generated by Django 5.0.1 on 2024-05-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
