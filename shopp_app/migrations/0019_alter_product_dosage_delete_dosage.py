# Generated by Django 4.1.6 on 2023-03-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0018_brand_dosage_units_remove_product_description2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dosage',
            field=models.TextField(default='1', max_length=100),
        ),
        migrations.DeleteModel(
            name='dosage',
        ),
    ]
