from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

from customer.models import Customer


# Create your views here.


def customers(request):
    searched = request.GET.get('searched')
    if searched:
        customer_list = Customer.objects.filter(full_name__icontains=searched)
    else:
        customer_list = Customer.objects.all()
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'customer/customer-list.html', context)


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from customer.forms import LoginForm, RegisterModelForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('customers')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customers')
    else:
        form = RegisterModelForm()

    return render(request, 'auth/register.html', {"form": form})


def logout_page(request):
    logout(request)
    return render(request, 'auth/logout.html')
