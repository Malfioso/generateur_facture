# ~/projects/generateur_facture/invoice/products/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product, Invoice, InvoiceItem
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductForm

products = Product.objects.all()

form = ProductForm()
def product_list(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')  # évite les doublons en cas de F5
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

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': product.price * quantity
            })
            total += product.price * quantity
        except Product.DoesNotExist:
            continue

    return render(request, 'products/cart.html', {
        'cart_items': products,
        'total': total
    })

def add_to_invoice(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        invoice_id = request.POST.get('invoice_id')
        quantity = int(request.POST.get('quantity', 1))

        invoice = get_object_or_404(Invoice, id=invoice_id)

        # Soit on met à jour, soit on crée un nouvel item
        item, created = InvoiceItem.objects.get_or_create(
            invoice=invoice,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            item.quantity += quantity
            item.save()

        return redirect('invoice-detail', invoice_id=invoice.id)  # vers la page de détail