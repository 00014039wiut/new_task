from django.contrib import admin
from blog.models import Product
from blog.models import Image

# Register your models here.
admin.site.register(Image)
admin.site.register(Product)
