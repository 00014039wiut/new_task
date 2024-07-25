from django.db.models import Max, Min, Avg, Q, Count
from django.shortcuts import redirect

from blog.models import Product
from customer.models import Customer


def product_list(request):
    products = Product.objects.all()
    number_of_products = products.count()
    phone_category = products.filter(category='phone')
    max_price = products.aggregate(Max('price'), default=0)
    min_price = products.aggregate(Min('price'), default=0)
    average_price = products.aggregate(Avg('price'), default=0)
    high_rating = Count('product', filter=Q(rating__gte=7))
    low_discounted = Count('product', filter=Q(discount__lte=20))
    high_discounted = Count('product', filter=Q(rating__gte=50))

    context = {
        'products': products,
        'number_of_products': number_of_products,
        'phone_category': phone_category,
        'max_price': max_price,
        'min_price': min_price,
        'average_price': average_price,
        'high_rating': high_rating,
        'low_discounted': low_discounted,
        'high_discounted': high_discounted,

    }
    return redirect(request, 'index.html', context)





def customer_list(request):
    customers = Customer.objects.all()
    number_of_customers = customers.count()
    cristiano_ronaldo = customers.filter(email__icontains='cristiano_ronaldo')
    max_age = customers.aggregate(Max('age'), default=0)
    min_age = customers.aggregate(Min('age'), default=0)
    average = customers.aggregate(Avg('age'), default=0)
    samarkand_customers = Count('customer', filter=Q(customer__address__icontain='Samarkand'))
    uzmobile = Count('customer', filter=Q(customer__phone_number__icontains = '+99899'))
    ucell = Count('customer', filter=Q(customer__phone_number__icontains = '+99893'))
    mobiuz = Count('customer', filter=Q(customer__phone_number__icontains = '+99897'))

    context = {
        'customers': customers,
        'number_of_customers': number_of_customers,
        'cristiano_ronaldo': cristiano_ronaldo,
        'max_age': max_age,
        'min_age': min_age,
        'average': average,
        'samarkand_customers': samarkand_customers,
        'uzmobile': uzmobile,
        'ucell': ucell,
        'mobiuz': mobiuz,
    }
    return redirect(request, 'customer-list.html', context)

