from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from blog.models import Product
from root.settings import BASE_DIR
import json


@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    print(f"{instance} is deleted")
    deleted_products_url = os.path.join(BASE_DIR, 'deleted_products.json')
    with open(deleted_products_url, 'w') as f:
        json.dump([instance], f)
