"""
URL configuration for invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from invoices import views as invoice_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # route to products page
    path('products/', product_views.products_list),
    path('about/', product_views.about),  # route to about page

    # route to invoices page
    path('invoices/', invoice_views.invoice_list),  # Default route to products page

]
