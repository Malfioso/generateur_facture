from django import forms
from django.forms import inlineformset_factory
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
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notes optionnelles'}),
        }

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1}),
        }

# Formset pour gérer plusieurs items dans une facture
InvoiceItemFormSet = inlineformset_factory(
    Invoice, 
    InvoiceItem,
    form=InvoiceItemForm,
    extra=3,  # Nombre de formulaires vides à afficher
    can_delete=True,  # Permet de supprimer des items
    min_num=1,  # Au moins un item requis
    validate_min=True
)