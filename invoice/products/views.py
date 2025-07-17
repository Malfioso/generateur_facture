# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

def products_list(request):
    return HttpResponse('<h1>PAGE DES PRODUITS</h1>')


def about(request):
    products = Product.objects.all()
    #dictionnaire contextuel 'products', abligatoire pour permettre à notre cabarit de capter ce qu'il se passe
    return render(request,'products/hello.html',{'products': products})