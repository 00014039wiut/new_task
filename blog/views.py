from django.shortcuts import render

from blog.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)