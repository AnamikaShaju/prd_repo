from django.shortcuts import render, redirect

from product_management_app.form import Productform
from product_management_app.models import Product


# Create your views here.
def product_add(request):
    form = Productform()
    if request.method == 'POST':
        form_data =Productform(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("product_view")
    return render(request,'product_add.html',{'form':form})

def helloworld(request):
    return render(request,'hello.html')
def product_view(request):
    data  = Product.objects.all()
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