from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Accounts.models import Account, user_address
from cart.models import Cart, Wishlist, orderplaced, orders
from django.shortcuts import render, redirect
from cart.utils import render_to_pdf
import razorpay
import datetime
from shopp_app.models import Catagory, Product


    


#Add to Cart.
@login_required(login_url='login')
def addcart(request,id):
    user = request.user
    item=Product.objects.get(id=id) 
    if item.stock>0:
        if Cart.objects.filter(user_id=user,product_id=item).exists():
            return redirect(cart)
        else:
            product_qty=1
            price=item.selling_price * product_qty
            new_cart=Cart(user_id=user.id,product_id=item.id,product_qty=product_qty,price=price)
            new_cart.save()
            return redirect('/')


# View Cart Page
@login_required(login_url='login')
def cart(request):
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    l=len(cart)
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.selling_price * i.product_qty 
    w_count=0
    category=Catagory.objects.all()
    data={'category':category,'cart':cart,'total':total,'w_count':w_count,'l':l}
    return render(request,'cart.html',data)


# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)

# Cart Quentity Plus Settings
def plusqty(request,id):
    cart=Cart.objects.filter(id=id) 
    for cart in cart:   
        if cart.product.stock > cart.product_qty:
            cart.product_qty +=1
            cart.price=cart.product_qty * cart.product.selling_price
            cart.save()
            return redirect('cart')
        # messages.success(request, 'Out of Stock')
        return redirect('cart')



# Cart Quentity minuse Settings
def minusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product_qty > 1 :
            cart.product_qty -=1
            cart.price=cart.product_qty * cart.product.selling_price
            cart.save()
            return redirect('cart')
        return redirect('cart')
    
    
    

#wishlist
@login_required(login_url='login')
def view_wishlist(request): 
    category=Catagory.objects.all()
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    l=len(cart) 
    user = request.user
    wlist=Wishlist.objects.filter(user_id=user.id)
    wishlist=Wishlist.objects.filter(user_id=request.user.id)
    w_count=0
    for i in wishlist:
        w_count=w_count+1 
    return render(request,"wishlist.html",{'wlist':wlist,'w_count':w_count,'l':l,'category':category})

@login_required(login_url='login')
def add_wishlist(request,id):
    item=Product.objects.get(id=id)
    user = request.user     
    if Wishlist.objects.filter( user_id =user.id,product_id=item.id).exists():
        return redirect('view_wishlist')        
    else:
        new_wishlist=Wishlist(user_id=user.id,product_id=item.id)
        new_wishlist.save()
        return redirect('view_wishlist')
    messages.success(request, 'Sign in..!!')
    return redirect(login)    


@login_required(login_url='login')
def de_wishlist(request,id):
    Wishlist.objects.get(id=id).delete()
    return redirect('view_wishlist') 


@login_required(login_url='login')
def checkout(request):
    # user = request.user
    # cart=Cart.objects.filter(user_id=user)
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    total=0
    for i in cart:
        total += i.product.selling_price * i.product_qty
    gst=12/100 *total
    grandtotal=total+gst
    stotal=grandtotal*100
    l=len(cart)
    category=Catagory.objects.all()
    product=Product.objects.all()
    wishlist=Wishlist.objects.filter(user_id=request.user.id)
    address=user_address.objects.filter(user_id=request.user.id)

    id = request.user.id
    # user=Account.objects.get(id=id)
    # user=Account.objects.all()
    w_count=0
    
    
    
    client = razorpay.Client(auth=("rzp_test_7S55yXWHAiay49", "9Yx9RXpBNG2Im1PlxeFOs7oe"))

    DATA = {
        "amount": 100,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
    }
    client.order.create(data=DATA)
    
    
    payment=client.order.create(data=DATA)
    amount=payment['amount']
    oid=payment['id']
    request.session['order_id']=oid
    add=user_address.objects.get(id=2)
    status=payment['status']
    time=datetime.datetime.now()
    New_p=orders(user=user1,address=add,amount=amount,ra_o_id=oid,ra_status=status,created_at=time)
    New_p.save()
    
    
    for i in wishlist:
        w_count=w_count+1 
    data={'user':user1,'len':l,'id':id,'cart':cart,
          'total':total,'category':category,'w_count':w_count,
          'address':address,'stotal':stotal,'gst':gst,'grandtotal':grandtotal}    
    return render(request,"checkout.html",data) 



def payment_done(request):
    order_id=request.session['order_id']
    payment_id = request.GET.get('payment_id')
    print(payment_id)

    payment=orders.objects.get(ra_o_id = order_id)

    payment.paid = True
    payment.ra_p_id = payment_id
    payment.save()
    # customer=Address_Book.objects.get(user=request.user,status=True)

    cart=Cart.objects.filter(user=request.user)
    # item = Product.objects.get(product=product, id=item_id)

    for c in cart:
        orderplaced(user=request.user,product=c.product,quantity=c.product_qty,payment=payment).save()
        pro=Product.objects.get(id=c.product.id)
        pro.stock=pro.stock-c.product_qty
        pro.save()
        c.delete()
    return redirect('paymenrsuccess')



def paymenrsuccess(request):
    category=Catagory.objects.all()
    product=Product.objects.all()
    wishlist=Wishlist.objects.filter(user_id=request.user.id)
    w_count=0
    for i in wishlist:
        w_count=w_count+1  
    return render(request,"paymentsucces.html",{'category':category,'product':product,'w_count':w_count})



@login_required(login_url='login')
def de_addres_ch(request,id):
    user_address.objects.get(id=id).delete()
    return redirect('checkout')


@login_required(login_url='login')
def orders_list(request):
    user = request.user
    item=orderplaced.objects.filter(user_id=user)
    data={'item':item}
    return render(request,"orders.html",data)


def get(request,id,*args, **kwargs,):
        
        place = orderplaced.objects.get(id=id)
        date=place.payment.created_at

        orders=orderplaced.objects.filter(user_id=request.user.id,payment__created_at=date)
        total=0
        for o in orders:
            total=total+(o.product.selling_price*o.quantity)
        addrs=user_address.objects.filter(user_id=request.user.id)
        gst=12/100 *total
        grandtotal=total+gst
        
        data = {
            'gst':gst,
            "grandtotal":grandtotal,
            "orders":orders,
            "shipping":addrs,
        
        }
        pdf = render_to_pdf('report.html',data)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            # filename = "Report_for_%s.pdf" %(data['id'])
            filename = "Bill"

            content = "inline; filename= %s" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Page Not Found")