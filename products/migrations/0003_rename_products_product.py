# Generated by Django 4.2 on 2024-04-15 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_created_at_products_updated_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
