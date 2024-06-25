from django.urls import path

from customer.views import customers, register, logout_page, login_page

urlpatterns = [
  path('customer-list/', customers, name='customers'),
  path('login/', login_page, name='login'),
  path('register/', register, name='register'),
  path('logout/', logout_page, name='logout'),

]