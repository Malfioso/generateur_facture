
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'expiration_date', 'variety']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'variety': forms.Select(),
        }