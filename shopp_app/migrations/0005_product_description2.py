# Generated by Django 4.1.6 on 2023-02-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0004_catagory_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description2',
            field=models.TextField(max_length=500, null=True),
        ),
    ]