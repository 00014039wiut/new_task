from django.urls import path
from django.views.generic import detail

from blog.views import index, product_detail, add_product
from customer.views import customers, login, register, logout

urlpatterns = [
  path('customer-list/', customers, name='customers'),
  path('login/', login, name='login'),
  path('register/', register, name='register'),
  path('logout/', logout, name='logout'),
]