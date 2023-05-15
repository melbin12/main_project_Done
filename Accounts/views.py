
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
import requests

from cart.models import Cart
from .models import Account, user_address
from django.contrib.auth import authenticate
from shopp_app.models import Catagory, Product

#email verification import files
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
import json

# Create your views here.
def index(request):
    category=Catagory.objects.all()
    user1 = request.user
    cart=Cart.objects.filter(user=user1.id)
    l=len(cart)
    trending=Product.objects.filter(trending=1)
    is_featured=Product.objects.filter(is_featured=1)
    data={'category':category,'cart':cart,'l':l,'trending':trending,'is_featured':is_featured}
    return render(request,'index.html',data)
def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone_number=request.POST['tel']
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname,  phone_number=phone_number)
            user.save()
            messages.success(request, 'Thank you for registering with us.')
            messages.success(request, 'Please verify your email for login!')

            #code for email verification also check validate function
            current_site = get_current_site(request)
            message = render_to_string('account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
             #email#
            send_mail(
                'Please activate your account',
                message,
                'growerp189@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('/login/?command=verification&email=' + email)
        # return redirect('login')
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
           
            request.session['email']=email
            if user.is_admin:
                messages.success(request, 'you are logged in.....!')
                return redirect('admin/')
            else:
                messages.success(request, 'you are logged in.....!')
                return redirect('index')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')

def category(request):
    return render(request, 'category.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login')
def profile(request):
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    l=len(cart)
    user_id = request.user.id
    user=Account.objects.get(id=user_id)
    addres=user_address.objects.filter(user_id=request.user.id)
    data={'user':user,'addres':addres,'l':l}
    return render(request,"profile.html",data) 


@login_required(login_url='login')
def address(request):
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    l=len(cart)
    data={'l':l}
    if request.method=='POST':
        fname=request.POST.get('fname');
        lname=request.POST.get('lname');
        email=request.POST.get('email');
        phone = request.POST.get('phone');
        hname = request.POST.get('hname');
        street = request.POST.get('street');
        city = request.POST.get('city');
        district = request.POST.get('district');
        pin = request.POST.get('pin');
        user = request.user.id
        address=user_address(user_id=user,fname=fname,lname=lname,email=email,phone_no=phone,hname=hname,street=street,city=city,district=district,pin=pin)
        address.save()
        messages.success(request, 'Shipping Address Added Successfully...')
        return redirect('profile')
    return render(request,"addres.html",data)
    
    
def profile_update(request):
    user_id = request.user.id
    user=Account.objects.get(id=user_id)
    user1 = request.user
    cart=Cart.objects.filter(user=user1)
    l=len(cart)
    data={'l':l}
    if request.method == "POST":
         fname  = request.POST.get('fname')
         lname  = request.POST.get('lname')
         email = request.POST.get('email')
         phone_number = request.POST.get('phone_number')
       
         user.fname =  fname
         user.lname =  lname
         user.phone_number = phone_number
         user.email = email
         user.save()
         messages.success(request,'Profile Are Successfully Updated. ')
         
         return redirect('profile')
    return render(request,"Edit_profile.html",data)
    

    #forgotpassword

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email

            current_site = get_current_site(request)
            message = render_to_string('ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'grower628@gmail.com',
                [email],
                fail_silently=True,
            )

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'ResetPassword.html') 

#CHANGE PASS Word

def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.Login Now')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('profile')
    return render(request, 'Edit_profile.html')


@login_required(login_url='login')
def de_addres(request,id):
    user_address.objects.get(id=id).delete()
    return redirect('profile')


   
#search 
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(name__icontains=query) | Q( description__icontains=query))
            products = Product.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'product':products})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {})



def wether(request):
    if "location" in request.GET:
        city =request.GET.get('location')       
        url=f"https://api.openweathermap.org/data/2.5/weather?q={ city }&appid=f79972d58fb4b5a3e1573e076c06e49f"
        x = requests.get(url)
        y = x.json()
        context={
            'city_name': f"city_name:{y['name']}",
            'city_tempracher': f"city_tempracher:{y['main']['temp']}",
            'city_pressure': f"city_pressure:{y['main']['pressure']}",
            'city_humidity': f"city_humidity:{y['main']['humidity']}",
            
            
            
        }
        print(context)
        return render(request,'contact.html',context)
        
    return render(request,'contact.html')