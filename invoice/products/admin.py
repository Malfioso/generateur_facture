from django.contrib import admin

# Product registering.

from products.models import Product, Invoice, InvoiceItem

class ProductAdmin(admin.ModelAdmin):  
    list_display = ('name', 'price', 'expiration_date') # tuple n-uplet of fields that we want to show in admin mode

admin.site.register(Product,ProductAdmin)

# Invoice registering

class InvoiceItemInline(admin.TabularInline):  # ou StackedInline si tu veux plus gros
    model = InvoiceItem
    extra = 1  # nombre de lignes vides affichées par défaut

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]
    list_display = ('id', 'customer_name', 'created_at', 'display_total_price')

    def display_total_price(self, obj):
        return f"{obj.total_price():.2f} €"
    display_total_price.short_description = "Total"

admin.site.register(Invoice, InvoiceAdmin)