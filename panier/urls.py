

from django.urls import path

from . import views

app_name = 'panier'

urlpatterns = [
    path('', views.panier_detail, name='panier_detail'),
  
    path('add/<int:product_id>/', views.panier_add, name='panier_add'),
    path('remove/<int:product_id>/', views.panier_remove, name='panier_remove'),
]	