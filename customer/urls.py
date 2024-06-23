from django.urls import path
from django.views.generic import detail

from blog.views import index, product_detail, add_product
from customer.views import customers, login, register, logout, login_page

urlpatterns = [
  path('customer-list/', customers, name='customers'),
  path('login/', login_page, name='login'),
  path('register/', register, name='register'),
  path('logout/', logout, name='logout'),

]