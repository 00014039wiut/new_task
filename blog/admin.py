from django.contrib import admin
from blog.models import Product
from blog.models import Image, Attribute, AttributeValue, ProductAttribute



# Register your models here.
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
