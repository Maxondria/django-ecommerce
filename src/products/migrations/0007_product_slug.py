# Generated by Django 3.0.3 on 2020-02-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
    ]
