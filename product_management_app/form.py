from django.forms import ModelForm

from product_management_app.models import Product


class Productform(ModelForm):
    class Meta:
        model = Product
        fields =['product_name','price','stock_quantity']
