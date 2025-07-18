
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
    remove_index = request.GET.get('remove_index')

    # Définir le FormSet globalement AVANT le if
    InvoiceItemFormSet = modelformset_factory(
        InvoiceItem,
        fields=('product', 'quantity'),
        extra=extra_forms,
        can_delete=True
    )

    if request.method == 'POST':
        # Si c'est une soumission normale (création de facture)
        if 'create_invoice' in request.POST:
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
        
        # Si c'est un ajout de produit, on garde les données existantes
        else:
            invoice_form = InvoiceForm(request.POST)
            formset = InvoiceItemFormSet(request.POST)
            
            # Récupérer tous les produits pour les prix
            products = Product.objects.all()
            
            return render(request, 'products/invoice_form.html', {
                'invoice_form': invoice_form,
                'formset': formset,
                'extra_forms': extra_forms,
                'products': products
            })
    
    # GET request - gestion des paramètres URL pour persistance
    else:
        # Récupérer les données depuis les paramètres GET
        initial_invoice_data = {}
        if request.GET.get('customer_name'):
            initial_invoice_data['customer_name'] = request.GET.get('customer_name')
        if request.GET.get('notes'):
            initial_invoice_data['notes'] = request.GET.get('notes')
        
        # Créer le formulaire invoice avec les données initiales
        invoice_form = InvoiceForm(initial=initial_invoice_data)
        
        # Récupérer les données des produits depuis les paramètres GET
        initial_formset_data = []
        form_index = 0
        
        while True:
            product_key = f'form-{form_index}-product'
            quantity_key = f'form-{form_index}-quantity'
            
            if product_key in request.GET and request.GET.get(product_key):
                try:
                    product_id = int(request.GET.get(product_key))
                    quantity = int(request.GET.get(quantity_key, 1))
                    
                    # Si on supprime un produit, on vérifie si c'est celui à exclure
                    if remove_index is not None:
                        remove_idx = int(remove_index)
                        # On ne compte que les formulaires qui ont des données
                        current_data_index = len(initial_formset_data)
                        if current_data_index == remove_idx:
                            form_index += 1
                            continue
                    
                    initial_formset_data.append({
                        'product': product_id,
                        'quantity': quantity
                    })
                except (ValueError, TypeError):
                    pass
            else:
                break
            
            form_index += 1
        
        # Ajuster le nombre de formulaires extra si on supprime
        if remove_index is not None and extra_forms > 0:
            extra_forms = max(1, extra_forms)  # Garder au moins 1 formulaire
        
        # Créer le formset avec les données initiales
        formset = InvoiceItemFormSet(queryset=InvoiceItem.objects.none(), initial=initial_formset_data)

    # Récupérer tous les produits pour les prix
    products = Product.objects.all()

    return render(request, 'products/invoice_form.html', {
        'invoice_form': invoice_form,
        'formset': formset,
        'extra_forms': extra_forms,
        'products': products
    })