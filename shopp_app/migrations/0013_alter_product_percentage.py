# Generated by Django 4.1.6 on 2023-03-04 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0012_alter_product_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='percentage',
            field=models.IntegerField(default=1),
        ),
    ]
