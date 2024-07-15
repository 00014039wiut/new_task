import csv
import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from customer.models import Customer
import openpyxl


# Create your views here.
class CustomerListView(ListView):
    model = Customer
    paginate_by = 10
    template_name = 'customer/customer-list.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        searched = self.request.GET.get('searched')
        if searched:
            customer_list = Customer.objects.filter(full_name__icontains=searched)
        else:
            customer_list = Customer.objects.all()
        return customer_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searched = self.request.GET.get('searched')
        context['searched'] = searched
        return context


# def customers(request):
#     searched = request.GET.get('searched')
#     if searched:
#         customer_list = Customer.objects.filter(full_name__icontains=searched)
#     else:
#         customer_list = Customer.objects.all()
#         paginator = Paginator(customer_list, 4)
#         page = request.GET.get('page')
#
#         try:
#             customer_list = paginator.page(page)
#         except PageNotAnInteger:
#             customer_list = paginator.page(1)
#         except EmptyPage:
#             customer_list = paginator.page(paginator.num_pages)
#     context = {
#         'customer_list': customer_list,
#     }
#     return render(request, 'customer/customer-list.html', context)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer-detail.html'

    context_object_name = 'customer'


# def customer_detail(request, id):
#     customer = Customer.objects.get(id=id)
#     context = {"customer": customer}
#     return render(request, 'customer/customer-detail.html', context)


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from customer.forms import LoginForm, RegisterModelForm, CustomerModelForm


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


def export_data(request):
    response = None
    format = request.GET.get('format', 'csv')
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customers.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'Full Name', 'Email', 'Phone Number', 'Address'])
        for customer in Customer.objects.all():
            writer.writerow([customer.id, customer.full_name, customer.email, customer.phone_number, customer.address])


    elif format == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('full_name', 'email', 'phone_number', 'address'))
        # response.content = json.dumps(data, indent=4)
        response.write(json.dumps(data, indent=4))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
    elif format == 'xlsx':
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Customers.xlsx"'

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = 'My Data'

        # Write header row
        header = ['Id', 'Full Name', 'Email', 'Phone Number', 'Address']
        for col_num, column_title in enumerate(header, 1):
            cell = worksheet.cell(row=1, column=col_num)
            cell.value = column_title

        # Write data rows
        queryset = Customer.objects.all().values_list('id', 'full_name', 'email', 'phone_number', 'address')
        for row_num, row in enumerate(queryset, 1):
            for col_num, cell_value in enumerate(row, 1):
                cell = worksheet.cell(row=row_num + 1, column=col_num)
                cell.value = cell_value

        workbook.save(response)

        return response
    else:
        response = HttpResponse(status=404)
        response.content = 'Bad request'

    return response


# class AddCustomerView(View):
#     def get(self, request):
#         form = CustomerModelForm()
#         return render(request, 'customer/add-customer.html', {'form': form})
#
#     def post(self, request):
#         form = CustomerModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             customer = form.save(commit=False)
#             customer.save()
#             return redirect('customers')
#         return render(request, 'customer/add-customer.html', {'form': form})

class AddCustomerView(CreateView):
    model = Customer
    form_class = CustomerModelForm
    template_name = 'customer/add-customer.html'
    success_url = reverse_lazy('customers')


class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = CustomerModelForm
    template_name = 'customer/update-customer.html'
    success_url = reverse_lazy('customers')


class DeleteCustomerView(View):
    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return redirect('customers')
