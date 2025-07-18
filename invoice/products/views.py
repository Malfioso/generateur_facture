from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
import json
from products.models import Product, Invoice, InvoiceItem
from .forms import ProductForm, InvoiceForm, InvoiceItemFormSet

def product_list(request):
    products = Product.objects.all()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès !')
            return redirect('product-list')
    else:
        form = ProductForm()
    
    return render(request, 'products/product_list.html', {
        'products': products,
        'form': form
    })

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request,'products/product_details.html',
         {'product': product})

@user_passes_test(lambda u: u.is_superuser)
def update_product_price(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        try:
            new_price = float(request.POST.get('price', 0))
            if new_price <= 0:
                messages.error(request, 'Prix invalide')
                return redirect('product-list')

            product.price = new_price
            product.save()
            messages.success(request, f"Prix du produit '{product.name}' mis à jour à {product.price}€ !")
        except ValueError:
            messages.error(request, 'Format de prix invalide')

    return redirect('product-list')
def invoice_list(request):
    """Affiche la liste des factures"""
    invoices = Invoice.objects.all().order_by('-created_at')
    return render(request, 'products/invoice_list.html', {
        'invoices': invoices
    })

def invoice_create(request):
    """Crée une nouvelle facture"""
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            # Sauvegarde de la facture
            invoice = form.save()
            
            # Sauvegarde des items
            formset.instance = invoice
            formset.save()
            
            messages.success(request, 'Facture créée avec succès !')
            return redirect('invoice-detail', id=invoice.id)
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()
    
    return render(request, 'products/invoice_create.html', {
        'form': form,
        'formset': formset
    })

def invoice_detail(request, id):
    """Affiche les détails d'une facture"""
    invoice = get_object_or_404(Invoice, id=id)
    items = invoice.invoiceitem_set.all()
    
    return render(request, 'products/invoice_detail.html', {
        'invoice': invoice,
        'items': items
    })

def invoice_edit(request, id):
    """Modifie une facture existante"""
    invoice = get_object_or_404(Invoice, id=id)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            
            messages.success(request, 'Facture modifiée avec succès !')
            return redirect('invoice-detail', id=invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)
    
    return render(request, 'products/invoice_edit.html', {
        'form': form,
        'formset': formset,
        'invoice': invoice
    })