# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

def products_list(request):
    return HttpResponse('<h1>PAGE DES PRODUITS</h1>')


def about(request):
    products = Product.objects.all() 
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes fruits préférés sont :<p>
        <ul>
            <li>{products[0].name}</li>
            <li>{products[1].name}</li>
        </ul>
""")