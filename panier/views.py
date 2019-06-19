from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shopapp.models import Product
from .panier import Panier
from .forms import PanierAddProductForm


@require_POST
def panier_add(request, product_id):
    cart = Panier(request)  # create a new cart object passing it the request object 
    product = get_object_or_404(Product, id=product_id) 
    form = PanierAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('panier:panier_detail')


def panier_remove(request, product_id):
    cart = Panier(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('panier:panier_detail')


def panier_detail(request):
    cart = Panier(request)
    for item in cart:
        item['update_quantity_form'] = PanierAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'panier/detail.html', {'cart': cart})
