from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

from customer.models import Customer


# Create your views here.


def customers(request):
    customer_list = Customer.objects.all()
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'customer/customer-list.html', context)


def login(request):
    return render(request, 'customer/login.html')


def register(request):
    return render(request, 'customer/register.html')


def logout(request):
    return render(request, 'customer/logout.html')
