from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from .models import Tyre, Company, Customer, Order
from .forms import New_CompanyForm, New_CustomerForm, New_TyreForm, Update_TyreForm, Update_CustomerForm, Order_New

rooms =[
    # {'id':1,'name': 'add new'},
    # {'id':2,'name': 'Check status'},
    # {'id':3,'name': 'bill out'},
    # {'id':4,'name': 'update'},
]
def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:    
            messages.error(request,'User doesnot exist')

        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request,'Username or Password does not exist')

     

    context = {}
    return render(request,'base/login.html',context)
                            
    
def home(request):
    
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}        
    return render(request,'base/room.html',context)
  
 
def Update(request):
    context = {}
    return render(request,'base/update.html', context)

def CheckStatus(request):
    context = {}
    return render(request,'base/checkstatus.html', context)


def Add_new(request):
    context = {}
    return render(request,'base/add_new.html', context)

def Tyre_new(request):
    form = New_TyreForm()
    if request.method == 'POST':
        form = New_TyreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tyre_status')
    context = {'form': form}
    return render(request,'base/tyre_new.html', context)

def Tyre_status(request):
    if 'q' in request.GET:
        q = request.GET['q']
        tyre = Tyre.objects.filter(name__icontains = q )
    else:    
        tyre = Tyre.objects.all()
    context = {'tyre':  tyre}
    return render(request,'base/tyre_status.html', context)

def Customer_new(request):
   form = New_CustomerForm()
   if request.method == 'POST':
        form = New_CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
   
   context = {'form':form}
   return render(request,'base/customer_new.html', context)
def Company_new(request):
    form = New_CompanyForm()
    if request.method == 'POST':
        form = New_CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form }
    return render(request,'base/company_new.html',context) 

def Tyre_update(request):
    if 'q' in request.GET:
        q = request.GET['q']
        tyre = Tyre.objects.filter(name__icontains= q)
    else:
        tyre = Tyre.objects.all()

    context = {'tyre': tyre}
    return render(request,'base/tyre_update.html', context)



def Customer_update(request):
    if 'q' in request.GET:
        q = request.GET['q']
        customer = Customer.objects.filter(name__icontains = q)
    else:    
        customer = Customer.objects.all()
    form = Update_CustomerForm()
    if request.method == 'POST':
        form = Update_CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'customer':  customer}
    return render(request,'base/customer_update.html', context)

def Tyre_Edit(request , q):
    tyre = Tyre.objects.get(id = q)
    form = New_TyreForm(instance = tyre)

    if request.method == 'POST':
        form = New_TyreForm(request.POST, instance = tyre)
        if form.is_valid():
            form.save()
            return redirect('tyre_update')

    context = {'tyre':tyre, 'form': form }
    return render(request, 'base/tyre_new.html', context)    


def Order_new(request):
    form = Order_New()
    if request.method == 'POST':
        form = Order_New(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_status')
    context = {'form': form}
    return render(request,'base/order.html', context)

def Customer_profile(request):
    if 'q' in request.GET:
        q = request.GET['q']
        customer = Customer.objects.filter(name__icontains = q)
    else:    
        customer = Customer.objects.all()
    context = {'customer':  customer}
    return render(request,'base/customer_profile.html', context)

def Customer_Edit(request , a):
    customer = Customer.objects.get(id = a)
    form = New_CustomerForm(instance = customer)

    if request.method == 'POST':
        form = New_CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save()
            return redirect('customer_update')

    context = {'customer':customer, 'form': form }
    return render(request, 'base/customer_new.html', context) 

def Customer_profile_page(request, q):
    customer = Customer.objects.get(id=q)
    # orders = Order.objects.filter(customer_mobile_number =mobile_number )
    context = {'customer':  customer}
    return render(request,'base/customer_profile_page.html', context)

def Order_status(request):
    if 'q' in request.GET:
        q = request.GET['q']
        order = Order.objects.filter(customer_name__icontains = q)
    else:    
        order = Order.objects.all()
    context = {'order':  order}
    return render(request,'base/order_status.html', context)
