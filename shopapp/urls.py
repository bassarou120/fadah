

from django.urls import path

from . import views

app_name = 'shopapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/',views.product_list,name='product_list'),
    path('product_list/<slug:slug>/',views.product_list,name='product_list_by_category'),
    path('product_detail/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
]