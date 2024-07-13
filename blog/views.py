from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from blog.forms import ProductForm, ProductModelForm
from blog.models import Product

# Create your views here.
from django.http import HttpResponse


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'app/index.html', context)


# def index(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()

    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-detail.html', context)


# def add_product(request):
#     form = ProductForm()
#     context = {
#         'form': form
#
#     }
#     return render(request, 'app/add-product.html', context)


class AddProductView(View):
    def get(self, request):
        form = ProductModelForm()
        context = {'form': form}
        return render(request, 'app/add-product.html', context)

    def post(self, request):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {'form': form}
        return render(request, 'app/add-product.html', context)

class UpdateProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        form = ProductModelForm(instance=product)
        context = {'form': form}
        return render(request, 'app/update-product.html', context)
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        form = ProductModelForm(instance=product, data=request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'app/update-product.html', context)
class DeleteProductView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('index')
