from django.urls import path
from django.views.generic import detail

from blog.views import index, product_detail
urlpatterns = [
    path("index/", index, name="index"),
    path("product-detail/<int:product_id>", product_detail, name="product_detail"),
]