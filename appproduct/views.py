from django.shortcuts import render, get_object_or_404

from .models import Product

def product(request, slug):
    product_page = get_object_or_404(Product, slug=slug)
    return render(request, 'appproduct/product.html', {'product': product_page})


