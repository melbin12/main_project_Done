from django.shortcuts import render
import cart
from cart.models import Cart
from shopp_app.models import Catagory, Catagory_Type2,Product
from django.shortcuts import render, redirect


# Create your views here.
def category_page(request,id):
    user1 = request.user
    cart=Cart.objects.filter(user=user1.id)
    l=len(cart)
    category=Catagory.objects.all()
    product=Product.objects.filter(category_id=id)
    cat=Catagory.objects.get(id=id)
    c=Catagory_Type2.objects.filter(name='M')
    if(cat.Type.name=='pestiside'):
     c=Catagory_Type2.objects.filter().exclude(name='M')
    data={'category':category,'product':product,'l':l,'cat':c}
    return render(request,'category.html',data)


def category_page1(request,id):
    user1 = request.user
    cart=Cart.objects.filter(user=user1.id)
    l=len(cart)
    category=Catagory.objects.all()
    type1=Catagory_Type2.objects.get(id=id)
    product=Product.objects.filter(category_id=id,Type1=type1)
    # cat=Catagory.objects.get(id=id)
    c=Catagory_Type2.objects.filter(name='M')
    # if(cat.Type.name=='pestiside'):
    #  c=Catagory_Type2.objects.filter().exclude(name='M')
    data={'category':category,'product':product,'l':l,'cat':c}
    return render(request,'category.html',data)
