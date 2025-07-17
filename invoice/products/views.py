# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

products = Product.objects.all()

def product_list(request):
    #dictionnaire contextuel 'products', abligatoire pour permettre à notre cabarit de capter ce qu'il se passe
    return render(request,'products/product_list.html',{'products': products})

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request,'products/product_details.html',
         {'product': product})
