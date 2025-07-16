from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def invoice_list(request):
    return HttpResponse('<h1>PAGE DES FACTURES</h1>')