# Generated by Django 4.1.6 on 2023-03-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0019_alter_product_dosage_delete_dosage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dosage',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
