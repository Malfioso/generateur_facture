from django import forms
from django.forms import inlineformset_factory,modelformset_factory
from .models import Product, Invoice, InvoiceItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date', 'variety','image']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'variety': forms.Select(),
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'notes']


InvoiceItemFormSet = modelformset_factory(
    InvoiceItem,
    fields=('product', 'quantity'),
    extra=1,
    can_delete=True,
)
