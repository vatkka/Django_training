from django.shortcuts import render

from products.models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(request, 'products/products.html', context)
