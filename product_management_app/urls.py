from django.urls import path

from product_management_app import views

urlpatterns = [
    path("productadd",views.product_add,name="productadd"),
    path('hello',views.helloworld,name='helloworld'),
    path('product_view',views.product_view,name='product_view'),
    path("delete_data/<int:id>/",views.delete_data,name="delete_data"),
    path("update_data/<int:id>/",views.update_data,name="update_data"),
    path("useradd",views.customer_register,name="useradd"),
    path("selladd",views.seller_register, name="selladd"),
    path("",views.login_view,name="loginview"),
    path('adminbase',views.admin_base,name="adminbase"),
    path('customerbase',views.customer_base,name="customerbase"),
    path('sellerbase',views.seller_base,name="sellerbase"),
    path('sellerproductview',views.seller_productview,name="sellerproductview"),
    path('customerproductview',views.customer_productview,name="customerproductview"),
    path('custadmin',views.customer_all,name="custadmin"),
    path('selleradmin',views.seller_all,name="selleradmin"),
    path('logoutview',views.logout_view,name="logoutview")


]