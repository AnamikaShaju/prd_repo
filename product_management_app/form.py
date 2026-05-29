from django import forms
from django.contrib.auth.forms import UserCreationForm


from product_management_app.models import Product, Customer, seller, Login_data


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields =['product_name','price','stock_quantity','image_url']



class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
    class Meta:
        model = Login_data
        fields =('username','password1','password2')


class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','phone_number','address']

class sellerform(forms.ModelForm):
    class Meta:
        model =seller
        fields =['name','email','phone_number']





