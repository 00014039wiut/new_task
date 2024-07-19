from django.urls import path

from customer.views import CustomerListView, logout_page, export_data, \
  AddCustomerView, CustomerDetailView, UpdateCustomerView, DeleteCustomerView, LoginPageView, \
  LoginPage, RegisterFormView, sending_email, successful_email, register, activate

app_name = 'customer'
urlpatterns = [
  path('customer-list/', CustomerListView.as_view(), name='customers'),
  path('login/', LoginPageView.as_view(), name='login'),
  path('register/', register, name='register'),
  path('logout/', logout_page, name='logout'),
  path('export-data/', export_data, name='export_data'),
  path("customer-detail/<int:pk>", CustomerDetailView.as_view(), name="customer-detail"),
  path("add-customer/", AddCustomerView.as_view(), name="add_customer"),
  path("<int:pk>/edit", UpdateCustomerView.as_view(), name="customer-edit"),
  path("<int:pk>/delete", DeleteCustomerView.as_view(), name="customer-delete"),
  path("email-sending/", sending_email, name="sending_email"),
  path('successful_email/', successful_email, name='successful_email'),
  path('activate/<uidb64>/<token>', activate, name='activate')

]