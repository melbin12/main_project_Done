from django.db import models
from Accounts.models import Account, user_address
from shopp_app.models import Product

# Create your models here.

#Cart Table
class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    
    
    def get_product_price(self):
        price=[self.product.price]
        return sum(price)


#whishlist
class Wishlist(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
#payment order table

class orders(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,verbose_name='Email')
    address = models.ForeignKey(user_address, on_delete=models.CASCADE, null=True)
    amount=models.FloatField(blank=True,null=True)
    ra_o_id=models.CharField(max_length=40,null=True)
    ra_p_id=models.CharField(max_length=40,null=True)
    ra_status=models.CharField(max_length=40,null=True)
    created_at=models.DateTimeField()
    paid=models.BooleanField(default=False)

    def __str__(self):
        return (self.user.email)     
    
#order placed table
class orderplaced(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    payment  =models.ForeignKey(orders,on_delete=models.CASCADE)
    quantity =models.IntegerField() 
    is_ordered = True
    

    def __str__(self):
        return (self.product.name)    
    
   