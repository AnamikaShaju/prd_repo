from django.urls import path

from product_management_app import views

urlpatterns = [
    path("productadd",views.product_add,name="product_add"),
    path('hello',views.helloworld,name='helloworld'),
    path('product_view',views.product_view,name='product_view'),
    path("delete_data/<int:id>/",views.delete_data,name="delete_data"),
    path("update_data/<int:id>/",views.update_data,name="update_data"),
]