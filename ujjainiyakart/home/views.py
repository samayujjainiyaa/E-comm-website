from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

def index(request):
    data=Product.objects.all()
    print(data)
    return render(request,'index.html',{'data':data})

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pwd=request.POST['pwd']
        pwd1=request.POST['pwd1']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already taken')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email already taken')
        elif pwd!=pwd1:
            messages.info(request,'passwords missmatched')
        else:
            user=User.objects.create_user(username=username,email=email,password=pwd)
            user.save()
            messages.info(request,'sucessfully signed up')
        return redirect("/signin")
    else:
        return render(request,'signin.html')


def ulogin(request):
    if request.method=='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            data=Product.objects.all()
            cdt=Cart.objects.all()
            count=Cart.objects.all().count()
            return render(request,'card.html',{'data':data,'cdt':cdt,'count':count})
        else:
            messages.info(request,'Invalid username and password')
            return render(request,'ulogin.html')    
    else:
        return render(request,'ulogin.html')
def logout(request):
    auth.logout(request)
    data=Product.objects.all()
    print(data)
    return render(request,'home.html',{'data':data})

def cardpage(request):
    charges=30
    pid=request.GET['id']
    prodt=Product.objects.get(id=pid)
    Cart(item=prodt).save()
    data=Product.objects.all()
    cdt=Cart.objects.all()
    count=Cart.objects.all().count()
    total_amount = 0
    for i in cdt:
        total_amount=total_amount+i.item.price+charges
    return render(request,'card.html',{'data':data,'cdt':cdt,'count':count,'total_amount':total_amount})
    
def deletecart(request):
    did=request.GET['id']
    cdt=Cart.objects.all()
    Cart.objects.get(id=did).delete()
    data=Product.objects.all()
    cdt=Cart.objects.all()
    total_amount = 0
    for i in cdt:
        total_amount=total_amount+i.item.price
    count=Cart.objects.all().count()

    return render(request,'card.html',{'data':data,'cdt':cdt,'count':count,'total_amount':total_amount})


