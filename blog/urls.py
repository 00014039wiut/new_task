from django.urls import path
from django.views.generic import detail

from blog.views import product_detail, ProductListView, AddProductView, DeleteProductView, UpdateProductView

urlpatterns = [
    path("index/", ProductListView.as_view(), name="index"),
    path("product-detail/<int:product_id>", product_detail, name="product_detail"),
    path("add-product/", AddProductView.as_view(), name="add_product"),
    path("delete-product/<int:product_id>", DeleteProductView.as_view(), name="delete_product"),
    path("update-product/<int:product_id>", UpdateProductView.as_view(), name="update_product"),
]