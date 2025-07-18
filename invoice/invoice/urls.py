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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # route to products page
    path('product_list/', product_views.product_list,name="product-list"),  # route to about page
    path('product_list/<int:id>/', product_views.product_details, name="product-detail"),
    path('cart', product_views.cart_view, name="cart"),
    path('invoice/add/<int:product_id>/', product_views.add_to_invoice, name='add-to-invoice'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
