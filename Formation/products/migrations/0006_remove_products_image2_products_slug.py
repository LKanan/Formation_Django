# Generated by Django 5.0.3 on 2024-04-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image2',
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
