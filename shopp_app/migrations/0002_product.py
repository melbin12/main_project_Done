# Generated by Django 4.1.6 on 2023-02-16 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('trending', models.BooleanField(default=False, help_text='0=default,1-Trending')),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopp_app.catagory')),
            ],
        ),
    ]