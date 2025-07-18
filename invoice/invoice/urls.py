"""
URL configuration for invoice project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from products import views as product_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_views.product_list, name='home'),
    
    # Routes pour les produits
    path('product_list/', product_views.product_list, name="product-list"),
    path('product_list/<int:id>/', product_views.product_details, name="product-detail"),
    
    # Routes pour les produits - mise à jour prix
    path('products/<int:product_id>/update-price/', product_views.update_product_price, name="update-product-price"),
    
    # Routes pour les factures
    path('invoices/', product_views.invoice_list, name="invoice-list"),
    path('invoices/create/', product_views.invoice_create, name="invoice-create"),
    path('invoices/<int:id>/', product_views.invoice_detail, name="invoice-detail"),
    path('invoices/<int:id>/edit/', product_views.invoice_edit, name="invoice-edit"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)