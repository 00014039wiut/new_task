from django.shortcuts import render

from blog.forms import ProductForm
from blog.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()

    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-detail.html', context)


def add_product(request):
    form = ProductForm()
    context = {
        'form': form

    }
    return render(request, 'app/add-product.html', context)
