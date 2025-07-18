
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import InvoiceForm, InvoiceItemFormSet
from django.contrib.auth.decorators import user_passes_test
import json
from products.models import Product, Invoice, InvoiceItem
from .forms import InvoiceItemFormSet, ProductForm

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

# Affichage du détail d'une facture
def invoice_detail(request, id):
    invoice = get_object_or_404(Invoice, pk=id)
    items = InvoiceItem.objects.filter(invoice=invoice)
    return render(request, 'products/invoice_detail.html', {
        'invoice': invoice,
        'items': items
    })


from django.forms import modelformset_factory

def create_invoice(request):
    extra_forms = int(request.GET.get('extra', 1))

    # Définir le FormSet globalement AVANT le if
    InvoiceItemFormSet = modelformset_factory(
        InvoiceItem,
        fields=('product', 'quantity'),
        extra=extra_forms,
        can_delete=True
    )

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)

        if invoice_form.is_valid() and formset.is_valid():
            invoice = invoice_form.save()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    item = form.save(commit=False)
                    item.invoice = invoice
                    item.save()
            messages.success(request, "OUH OUH AH AH ! Facture créée avec plein de bananes 🍌🐒")
            return redirect('invoice-detail', id=invoice.id)
    else:
        invoice_form = InvoiceForm()
        formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none())

    return render(request, 'products/invoice_form.html', {
        'invoice_form': invoice_form,
        'formset': formset,
        'extra_forms': extra_forms
    })
