from django.shortcuts import render
from cart.models import Cart

from shopp_app.models import Catagory, Product, Productgallery

def product_d(request,id):
    category=Catagory.objects.all()
    user1 = request.user
    cart=Cart.objects.filter(user=user1.id)
    l=len(cart)
    product=Product.objects.get(id=id)
    product_gallery=Productgallery.objects.filter(product_id=product.id)
    result=100-(product.selling_price/product.original_price*100)
    data={'product':product,'l':l,'product_gallery':product_gallery,'category':category,'result':result}
    return render(request, 'product.html',data)
    

# Create your views here.
