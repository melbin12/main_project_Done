# Generated by Django 4.1.6 on 2023-03-07 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0015_alter_product_type1'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory_type2',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopp_app.catagory'),
        ),
    ]
