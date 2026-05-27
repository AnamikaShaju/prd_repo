from django.contrib import admin

from product_management_app import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Login_data)
admin.site.register(models.Customer)
admin.site.register(models.seller)