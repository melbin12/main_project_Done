# Generated by Django 4.1.6 on 2023-03-07 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0013_alter_product_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory_Type2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Type1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopp_app.catagory_type'),
        ),
    ]
