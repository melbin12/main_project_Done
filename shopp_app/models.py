from django.db import models
import datetime
import os

# Create your models here.
class Catagory_Type(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False,unique=True)
    def __str__(self):
        return self.name



# Create your models here.
class Catagory_Type2(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False,unique=True)
    def __str__(self):
        return self.name


# Create your models here.
class Catagory(models.Model):
    Type=models.ForeignKey(Catagory_Type, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=False, blank=False,unique=True)
    category_image = models.ImageField(upload_to="uploads", null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    brand = models.CharField(max_length=100,null=True, blank=True,unique=True)
    def _str_(self):
        return self.brand
    
    
class units(models.Model):
    units = models.CharField(max_length=100,null=True, blank=True,unique=True)
    def _str_(self):
        return self.units
    
    
class Product(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    Type1=models.ForeignKey(Catagory_Type2, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, editable=False)
    product_image = models.ImageField(upload_to="uploads", null=True, blank=True)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    units = models.ForeignKey(units,on_delete=models.CASCADE,null=True)
    dosage = models.CharField(max_length=100, null=False, blank=False,default='1')
    description = models.TextField(max_length=500, null=False, blank=False)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now=True)
    trending = models.BooleanField(default=False, help_text="0=default,1-Trending")
    modified_date = models.DateTimeField(auto_now=True)
    percentage=models.IntegerField(default=1)
  

    def __str__(self):
        return '{}' .format(self.name)
    # def calculate_sum(self):
    #     self.percentage = 100-((self.selling_price/self.original_price)*100)
    #     self.save()
    
    

    
class Productgallery(models.Model):
    product=models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='store/products', max_length=255)

    def _str_(self):
        return self.product.product_name

    class Meta:
        verbose_name='Product Gallery'
        verbose_name_plural='Product gallery'