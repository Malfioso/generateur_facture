# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render

def products_list(request):
    return HttpResponse('<h1>PAGE DES PRODUITS</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')