# Generated by Django 5.0.7 on 2024-08-04 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_stock_product_stockquantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product',
            new_name='productId',
        ),
    ]
