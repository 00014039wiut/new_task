from django.contrib import admin

from customer.models import Customer


# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'joined', 'address')
    search_fields = ('joined', 'full_name')
    list_filter = ('joined', 'address')
