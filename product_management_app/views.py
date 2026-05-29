from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from product_management_app.form import loginRegister, Customerform, Productform, sellerform
from product_management_app.models import Product, seller


# Create your views here.
def product_add(request):
    user = request.user
    print(user.id)
    seller_data = seller.objects.get(user=user.id)
    print(seller_data)

    form = Productform()

    if request.method == 'POST':
        form_data =Productform(request.POST)
        if form_data.is_valid():
            obj= form_data.save(commit=False)
            obj.user=seller_data
            obj.save()
    return render(request,'product_add.html',{'form':form})

def helloworld(request):
    return render(request,'hello.html')

def product_view(request):
    user1 = request.user
    seller_data = seller.objects.get(user=user1)
    data = Product.objects.filter(user=seller_data)
    print(data)

    return render(request,'product_view.html',{'data':data})
def delete_data(request,id):
    obj= Product.objects.get(id=id)
    obj.delete()
    return redirect("product_view")
def update_data(request,id):
    obj= Product.objects.get(id=id)
    form = Productform(instance=obj)
    if request.method == 'POST':
        form_data= Productform(request.POST,request.FILES,instance=obj)
        if form_data.is_valid():
            form_data.save()
            return redirect("product_view")
    return render(request,'product_update.html',{'form':form})


def customer_register(request):
    form1= loginRegister()
    form2= Customerform()
    if request.method == 'POST':
        form1 = loginRegister (request.POST)
        form2 = Customerform (request.POST)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj1.is_customer = True
            obj1.save()
            obj2 = form2.save(commit=False)
            obj2.user=obj1
            obj2.save()
            print("registeration successfull")
    return render(request,"customer_register.html",{'form1':form1,'form2':form2})

def seller_register(request):
    form1= loginRegister()
    form2 = sellerform()
    if request.method == 'POST':
        form1 = loginRegister (request.POST)
        form2 = sellerform (request.POST)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj1.is_seller = True
            obj1.save()
            obj2 = form2.save(commit=False)
            obj2.user=obj1
            obj2.save()
            print("registration successfull")
    return render(request,"seller_register.html",{'form1':form1,'form2':form2})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                print("admin")
                return redirect("adminbase")
            if user.is_customer:
                print("Customer")
                return redirect("customerproductview")
            elif user.is_seller:
               print("Seller")
               return redirect("sellerbase")
        else:
            messages.info(request,"Invalid Credentials")
    return render(request,"login.html")


def admin_base(request):

      return render(request,'admin_base.html')


def customer_base(request):
    return render(request, 'customer_base.html')


def seller_base(request):
    return render(request, 'seller_base.html')


def seller_productview(request):
    user1 = request.user
    seller_data = seller.objects.get(user=user1)
    data = Product.objects.filter(user=seller_data)
    print(data)
    return render(request, 'seller_productview.html')



def customer_productview(request):
    data = Product.objects.all()
    print(data)
    return render(request,'customer_productview.html',{'data':data})