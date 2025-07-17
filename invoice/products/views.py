# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product
from .forms import ProductForm

products = Product.objects.all()

form = ProductForm()
def product_list(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')  # évite les doublons en cas de F5

    return render(request, 'products/product_list.html', {
        'products': products,
        'form': form
    })

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request,'products/product_details.html',
         {'product': product})
