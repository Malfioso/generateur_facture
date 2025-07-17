# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product


def product_list(request):
    products = Product.objects.all()
    #dictionnaire contextuel 'products', abligatoire pour permettre à notre cabarit de capter ce qu'il se passe
    return render(request,'products/product_list.html',{'products': products})