# Generated by Django 4.1.6 on 2023-02-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0005_product_description2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description2',
            field=models.TextField(max_length=800, null=True),
        ),
    ]
