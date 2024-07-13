from django.urls import path

from customer.views import customers, register, logout_page, login_page, export_data, customer_detail, \
  AddCustomerView

urlpatterns = [
  path('customer-list/', customers, name='customers'),
  path('login/', login_page, name='login'),
  path('register/', register, name='register'),
  path('logout/', logout_page, name='logout'),
  path('export-data/', export_data, name='export_data'),
  path("customer-detail/<int:id>", customer_detail, name="customer-detail"),
  path("add-customer/", AddCustomerView.as_view(), name="add_customer"),

]